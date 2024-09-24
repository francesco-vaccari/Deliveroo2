import sys
import os
import ast
import time
import json
import astor
import importlib
import subprocess

class Intention:
    def __init__(self, id, function_name, function_string, description):
        self.id = id
        self.function_name = function_name
        self.function_string = function_string
        self.description = description
        self.executable = True

class Desire:
    def __init__(self, id, description):
        self.id = id
        self.description = description
        self.intentions = []
        self.trigger_function_string = None
        self.executable = False

class ControlManager:
    def __init__(self, logger):
        self.intention_id = 1
        self.desire_id = 1
        self.timeout = 4
        self.intentions = {} # id -> Intention
        self.intentions_graph = {} # id -> [id] the function id contains calls to the functions [id]
        self.desires = {} # id -> Desire
        self.logger = logger
        self.base_actions_max_id = 0
        self.functions_file_path = 'agent_dir/functions'
        self.plan_file = self.functions_file_path + "/plan.txt"
        self.load_base_actions(self.functions_file_path + "/actions.json")
    
    def load_base_actions(self, actions_path):
        self.logger.log_info(f"Loading actions from {actions_path} ...")
        actions = json.load(open(actions_path))["actions"]
        for action in actions:
            # function_name = action["function_name"]
            function_name = f"function_{self.intention_id}"
            description = action["description"]
            function_string = f"""def {function_name}(belief_set):\n    with open('{self.plan_file}', 'a') as f:\n        f.write('{action["action_name"]}\\n')\n        f.close()\n\n"""
            self.intentions[self.intention_id] = Intention(self.intention_id, function_name, function_string, description)
            self.intentions_graph[self.intention_id] = []
            self.base_actions_max_id = self.intention_id
            self.intention_id += 1
        self.logger.log_info(f"Actions loaded: {self.get_printable_intentions()}")
    
    def check_if_desire_triggered(self, belief_set):
        self.logger.log_info(f"Checking if a desire has been triggered ...\nDesires: {self.get_printable_desires()}")
        for id, desire in self.desires.items():
            if desire.executable and desire.trigger_function_string is not None:
                if self.run_desire_trigger(id, belief_set):
                    self.logger.log_info(f"Desire {id} has been triggered.")
                    return id
        return None
    
    def test_intention(self, function_string, belief_set):
        self.logger.log_info(f"Testing intention \n{function_string}")
        error = self.is_valid_function(function_string)
        if error is not None:
            self.logger.log_error("Intention is invalid.")
            return error
        
        working_functions_names_before = self.get_implemented_intentions_names()
        working_functions_names = self.test_implemented_intentions(belief_set, test=True)
        self.logger.log_info(f"Tested implemented intentions. {self.get_printable_intentions()}")
        
        extracted_calls = self.extract_function_calls(function_string)
        for function_called in extracted_calls:
            if function_called in working_functions_names_before:
                if function_called not in working_functions_names:
                    self.logger.log_error(f"Intention is invalid. Contains call to broken functions.")
                    return f"The function called {function_called} can no longer be used. Do not use {function_called}."

        functions_file_name = self.functions_file_path + "/test_functions.py"

        belief_set_file = self.functions_file_path + "/belief_set.txt"
        with open(belief_set_file, 'w') as f:
            f.write(str(belief_set))
            f.close()

        try:
            with open(functions_file_name, "a") as f:
                f.write("\n")
                f.write(function_string)
                f.write("\n")
                f.write("\n")
                f.write(f"""with open('{belief_set_file}', 'r') as f:\n""")
                f.write("""    belief_set = eval(f.read())\n""")
                f.write("""    f.close()\n""")
                f.write("\n")
                f.write("\n")
                f.write(f"{self.get_function_name(function_string)}(belief_set)\n")
                f.close()

            process = subprocess.Popen(['python3', functions_file_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = process.communicate(timeout=5)
            if stderr != b'':
                raise Exception(stderr)
        except Exception as e:
            process.kill()
            self.logger.log_error(f"Intention is invalid. Error: {e}")
            return f"Error: {e}"
        
        self.logger.log_info("The intention is valid.")
        return None

    def test_implemented_intentions(self, belief_set, test):
        if test:
            functions_file_name = self.functions_file_path + "/test_functions.py"
        else:
            functions_file_name = self.functions_file_path + "/functions.py"

        working_functions_names = []

        with open(functions_file_name, "w") as f:
            f.write("\n")
            f.close()
        
        belief_set_file = self.functions_file_path + "/belief_set.txt"
        with open(belief_set_file, 'w') as f:
            f.write(str(belief_set))
            f.close()
        
        for id, intention in self.intentions.items():
            if intention.executable:
                try:
                    with open(functions_file_name, "r") as f:
                        content = f.read()
                        f.close()
                    with open(functions_file_name, "w") as f:
                        f.write(content)
                        f.write("\n")
                        f.write(intention.function_string)
                        f.write("\n")
                        f.write("\n")
                        f.write(f"""with open('{belief_set_file}', 'r') as f:\n""")
                        f.write("""    belief_set = eval(f.read())\n""")
                        f.write("""    f.close()\n""")
                        f.write("\n")
                        f.write("\n")
                        f.write(f"{intention.function_name}(belief_set)\n")
                        f.close()
                    
                    process = subprocess.Popen(['python3', functions_file_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    stdout, stderr = process.communicate(timeout=5)
                    if stderr == b'':
                        with open(functions_file_name, "w") as f:
                            f.write(content)
                            f.write("\n")
                            f.write(f"{intention.function_string}")
                            f.write("\n")
                            f.close()
                        working_functions_names.append(intention.function_name)
                    else:
                        raise Exception(stderr)
                except Exception as e:
                    process.kill()
                    self.invalidate_intention(id)
        
        return working_functions_names
    
    def add_intention(self, desire_id, description, function_string):
        new_function_name = f'function_{self.intention_id}'
        function_string = self.rename_function(function_string, new_function_name)

        intention = Intention(self.intention_id, new_function_name, function_string, description)
        self.intentions[self.intention_id] = intention
        self.intentions_graph[self.intention_id] = []
        
        functions_called = self.extract_function_calls(function_string)
        for function_called in functions_called:
            for id, intention in self.intentions.items():
                if intention.function_name == function_called:
                    self.intentions_graph[self.intention_id].append(id)

        self.desires[desire_id].intentions.append(intention)

        self.intention_id += 1

        self.logger.log_info(f"Intention added to desire {desire_id}")
        return self.intention_id - 1
    
    def run_intention(self, id, belief_set):
        if not self.intentions[id].executable:
            return None
        
        self.logger.log_info(f"Running intention {id} ...")

        working_functions_names = self.test_implemented_intentions(belief_set, test=False)
        self.logger.log_info(f"Tested implemented intentions. {self.get_printable_intentions()}")

        if not self.intentions[id].executable:
            return None
        
        functions_file_name = self.functions_file_path + "/functions.py"

        belief_set_file = self.functions_file_path + "/belief_set.txt"
        with open(belief_set_file, 'w') as f:
            f.write(str(belief_set))
            f.close()

        
        with open(self.plan_file, 'w') as f:
            f.write("")
            f.close()
        
        try:
            with open(functions_file_name, "a") as f:
                f.write("\n")
                f.write(self.intentions[id].function_string)
                f.write("\n")
                f.write("\n")
                f.write(f"""with open('{belief_set_file}', 'r') as f:\n""")
                f.write("""    belief_set = eval(f.read())\n""")
                f.write("""    f.close()\n""")
                f.write("\n")
                f.write("\n")
                f.write(f"{self.intentions[id].function_name}(belief_set)\n")
                f.close()

            process = subprocess.Popen(['python3', functions_file_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = process.communicate(timeout=5)
            if stderr != b'':
                raise Exception(stderr)

            self.logger.log_info(f"Intention {id} has been executed.")

            return self.get_plan_from_file(self.plan_file)
        except Exception as e:
            process.kill()
            self.invalidate_intention(id)
            self.logger.log_error(f"Intention {id} is invalid. Error: {e}")
            return None
    
    def get_plan_from_file(self, file_path):
        plan = []
        with open(file_path, 'r') as f:
            plan = f.read().splitlines()
            f.close()
        return plan

    def invalidate_intention(self, id):
        self.logger.log_info(f"Invalidating intention {id} ...")
        if id > self.base_actions_max_id:
            self.intentions[id].executable = False
            for intention_id, intention_calls in self.intentions_graph.items():
                if id in intention_calls:
                    self.invalidate_intention(intention_id)
        else:
            self.logger.log_info(f"Intention {id} is a base action. It cannot be invalidated.")

    def extract_function_calls(self, function_string):
        tree = ast.parse(function_string)
        
        class FunctionCallVisitor(ast.NodeVisitor):
            def __init__(self):
                self.calls = []
            
            def visit_Call(self, node):
                if isinstance(node.func, ast.Name):
                    self.calls.append(node.func.id)
                self.generic_visit(node)
        
        visitor = FunctionCallVisitor()
        visitor.visit(tree)
        
        return visitor.calls
    
    def add_desire(self, description):
        self.desires[self.desire_id] = Desire(self.desire_id, description)
        self.logger.log_info(f"Desire added: {self.desire_id}. Desires:{self.get_printable_desires()}")
        self.desire_id += 1
        return self.desire_id - 1

    def run_desire(self, id, belief_set):
        if id is None:
            return None
        self.logger.log_info(f"Generating plan for desire {id} ...")
        if True: # get the plan by executing only last intention
            intention = self.desires[id].intentions[-1]
            plan = self.run_intention(intention.id, belief_set)
            if plan is None:
                self.desires[id].executable = False
                self.logger.log_error(f"Desire {id} is now invalid.")
                return None
            self.logger.log_info(f"Desire {id} plan has been generated.")
            return plan
        else: # get the plan by executing all intentions and concatenating the plans [WRONG]
            concat_plans = []
            for intention in self.desires[id].intentions:
                plan = self.run_intention(intention.id, belief_set)
                if plan is None:
                    self.desires[id].executable = False
                    self.logger.log_error(f"Desire {id} is now invalid.")
                    return None
                concat_plans += plan
            self.logger.log_info(f"Desire {id} plan has been generated.")
            return concat_plans
    
    def add_trigger_function(self, desire_id, function_string):
        self.desires[desire_id].trigger_function_string = function_string
        self.desires[desire_id].executable = True
        self.logger.log_info(f"Trigger function added to desire {desire_id}.")

    def test_trigger_function(self, function_string, prior, current):
        self.logger.log_info(f"Testing trigger function \n{function_string}")
        error = self.is_valid_function(function_string)
        if error is not None:
            self.logger.log_error("Trigger function is invalid.")
            return error
        
        function_name = self.get_function_name(function_string)

        local_vars = {}
        try:
            exec(function_string, {}, local_vars)
            func = local_vars[function_name]
            res = func(prior)
            if not (isinstance(res, bool) and res):
                self.logger.log_error("Trigger function does not return the boolean True for the prior belief set.")
                return "The function does not return the boolean True for the prior belief set."
        except Exception as e:
            self.logger.log_error(f"Trigger function is invalid. Error: {e}")
            return f"Error: {e}"

        local_vars = {}
        try:
            exec(function_string, {}, local_vars)
            func = local_vars[function_name]
            res = func(current)
            if not isinstance(res, bool):
                self.logger.log_error("Trigger function does not return a boolean.")
                raise Exception("The function does not return a boolean.")
        except Exception as e:
            self.logger.log_error(f"Trigger function is invalid. Error: {e}")
            return f"Error: {e}"
        
        self.logger.log_info("The trigger function is valid.")
        return None

    def run_desire_trigger(self, id, belief_set):
        function_string = self.desires[id].trigger_function_string
        function_name = self.get_function_name(function_string)
        self.logger.log_info(f"Running trigger function for desire {id} ...")
        
        local_vars = {}
        try:
            exec(function_string, {}, local_vars)
            func = local_vars[function_name]
            res = func(belief_set)
            self.logger.log_info(f"Trigger function for desire {id} has been executed. Result: {res}")
            return res
        except Exception as e:
            self.desires[id].executable = False
            self.logger.log_error(f"Trigger function for desire {id} is invalid. Error: {e}")
            return False
    
    def invalidate_desire(self, id):
        self.logger.log_info(f"Invalidating desire {id} ...")
        self.desires[id].executable = False
    
    def is_valid_function(self, function_string):
        try:
            tree = ast.parse(function_string)
            
            if not isinstance(tree.body[0], ast.FunctionDef):
                return "The code does not contain a function definition."
            if not tree.body[0].name:
                return "The function does not have a name."
            
            return None
        except SyntaxError as e:
            return f"Syntax error: {e}"

    def get_function_name(self, function_string):
        tree = ast.parse(function_string)
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                return node.name
    
    def get_implemented_intentions_names(self):
        return [intention.function_name for intention in self.intentions.values() if intention.executable]

    def rename_function(self, function_string, new_name):
        tree = ast.parse(function_string)
        
        function_def = tree.body[0]
        old_name = function_def.name
        function_def.name = new_name

        class FunctionRenamer(ast.NodeTransformer):
            def visit_Call(self, node):
                if isinstance(node.func, ast.Name) and node.func.id == old_name:
                    node.func.id = new_name
                return self.generic_visit(node)

        renamer = FunctionRenamer()
        renamer.visit(tree)

        new_func_str = astor.to_source(tree)
        return new_func_str

    def get_library(self, stateless_intention_generation):
        intentions = {}
        for id, intention in self.intentions.items():
                if intention.executable:
                    intentions[id] = intention
                if stateless_intention_generation:
                    if id == self.base_actions_max_id:
                        break
        return intentions
    
    def get_desires_descriptions(self):
        descriptions = []
        for desire in self.desires.values():
            if desire.executable:
                descriptions.append(desire.description)
        return descriptions

    def get_intentions_called_by(self, id):
        intentions_called_ids = self.intentions_graph[id]
        for intention_id in intentions_called_ids:
            more_ids = self.get_intentions_called_by(intention_id)
            intentions_called_ids += more_ids
        return set(intentions_called_ids)

    def get_printable_intentions(self):
        out = "\n"
        for id, intention in self.intentions.items():
            out += f"[{id}]\n"
            out += f"Executable: {intention.executable}\n"
            out += f"Description: {intention.description}\n"
            out += self.add_tab(intention.function_string, 2)
            out += "\n"
        return out
    
    def get_printable_desires(self):
        if not bool(self.desires):
            return "Empty"
        out = "\n"
        for id, desire in self.desires.items():
            out += f"Desire {id}: {desire.description}\n"
            for intention in desire.intentions:
                out += f"    Intention ID: [{intention.id}]\n"
                out += f"    Executable: {intention.executable}\n"
                out += f"    Description: {intention.description}\n"
                out += self.add_tab(intention.function_string, 4)
                out += "\n"
        return out

    def get_printable_intentions_graph(self):
        if not bool(self.intentions_graph):
            return "Empty"
        out = "\n"
        for id, calls in self.intentions_graph.items():
            out += f"    - [{id}] calls : {calls}\n"
        return out
    
    def add_tab(self, string, n_tabs):
        return "\n".join(["    " * n_tabs + line for line in string.split("\n")])