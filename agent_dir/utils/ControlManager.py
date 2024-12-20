import sys
import os
import ast
import time
import json
import astor
import importlib
import subprocess
import threading
import random

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
    def __init__(self, logger, agent_folder):
        self.intention_id = 1
        self.desire_id = 1
        self.dtf_number = 1
        self.timeout = 15
        self.intentions = {} # id -> Intention
        self.intentions_graph = {} # id -> [id] the function id contains calls to the functions [id]
        self.desires = {} # id -> Desire
        self.logger = logger
        self.base_actions_max_id = 0
        if not os.path.exists("agent_dir/functions/" + agent_folder):
            os.makedirs("agent_dir/functions/" + agent_folder)
        self.functions_file = "agent_dir/functions/" + agent_folder + "/functions.py"
        self.belief_set_file = "agent_dir/functions/" + agent_folder + "/belief_set.txt"
        self.plan_file = "agent_dir/functions/" + agent_folder + "/plan.txt"
        self.continue_file = "agent_dir/functions/" + agent_folder + "/continue.txt"
        self.load_base_actions("agent_dir/actions.json")
    
    def load_base_actions(self, actions_path):
        self.logger.log_info(f"Loading actions from {actions_path} ...")
        actions = json.load(open(actions_path))["actions"]
        self.base_actions_names = []
        for action in actions:
            # function_name = action["function_name"]
            self.base_actions_names.append(action["action_name"])
            function_name = f"function_{self.intention_id}"
            description = action["description"]
            function_string = f"""def {function_name}():\n    with open('{self.plan_file}', 'a') as f:\n        f.write('{action["action_name"]}\\n')\n        f.close()\n    wait()\n\n"""
            self.intentions[self.intention_id] = Intention(self.intention_id, function_name, function_string, description)
            self.intentions_graph[self.intention_id] = []
            self.base_actions_max_id = self.intention_id
            self.intention_id += 1
        self.logger.log_info(f"Actions loaded: {self.get_printable_intentions()}")
    
    def check_if_desire_triggered(self, belief_set):
        self.logger.log_info(f"Checking if a desire has been triggered ...\nDesires: {self.get_printable_desires()}")
        desires_triggered = []
        for id, desire in self.desires.items():
            if desire.executable and desire.trigger_function_string is not None:
                if self.run_desire_trigger(id, belief_set):
                    self.logger.log_info(f"Desire {id} could be triggered. Adding it to the list...")
                    desires_triggered.append(id)
        self.logger.log_info(f"Desires triggered: {desires_triggered}. Now randomly choosing which one to run.")
        if len(desires_triggered) == 0:
            self.logger.log_info("No desire has been triggered.")
            return None
        else:
            id = random.choice(desires_triggered)
            self.logger.log_info(f"Desire {id} was randomly chosen. Desire {id} has been triggered.")
            return id
    
    def test_intention(self, function_string):
        self.logger.log_info(f"Testing intention \n{function_string}")

        error = self.is_valid_function(function_string)
        if error is not None:
            self.logger.log_error(f"The intention is invalid. Error: {error}")
            return f"Error: {error}"
        
        self.logger.log_info("The intention is valid.")
        return None

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
                    if self.intention_id != id: # avoid recursive calls in graph
                        self.intentions_graph[self.intention_id].append(id)

        self.desires[desire_id].intentions.append(intention)

        self.intention_id += 1

        self.logger.log_info(f"Intention added to desire {desire_id}")
        return self.intention_id - 1
    
    def run_intention(self, id, get_belief_set, execute_action):
        self.logger.log_info(f"Running intention {id} ...")

        with open(self.functions_file, 'w') as f:
            f.write("")
            f.close()
        
        with open(self.belief_set_file, 'w') as f:
            f.write("")
            f.close()
        
        with open(self.continue_file, 'w') as f:
            f.write("True")
            f.close()
        
        with open(self.plan_file, 'w') as f:
            f.write("")
            f.close()
        
        with open(self.functions_file, 'a') as f:
            f.write(f"import time\n")
            f.write(f"import copy\n\n")
            f.write(f"belief_set = None\n\n")
            f.write(f"def wait():\n")
            f.write(f"    with open('{self.continue_file}', 'w') as file:\n")
            f.write(f"        file.write('False')\n")
            f.write(f"        file.close()\n")
            f.write(f"    content = False\n")
            f.write(f"    while not content:\n")
            f.write(f"        with open('{self.continue_file}', 'r') as file:\n")
            f.write(f"            try:\n")
            f.write(f"                content = eval(file.read())\n")
            f.write(f"            except Exception as e:\n")
            f.write(f"                pass\n")
            f.write(f"            file.close()\n")
            f.write(f"        time.sleep(0.02)\n\n")
            
            f.write(f"import threading\n")
            f.write(f"thread_alive = True\n")
            f.write(f"def update_belief_set():\n")
            f.write(f"    global belief_set\n")
            f.write(f"    global thread_alive\n")
            f.write(f"    while thread_alive:\n")
            f.write(f"        with open('{self.belief_set_file}', 'r') as file:\n")
            f.write(f"            try:\n")
            f.write(f"                belief_set = eval(file.read())\n")
            f.write(f"            except Exception as e:\n")
            f.write(f"                pass\n")
            f.write(f"            file.close()\n")
            f.write(f"        time.sleep(0.02)\n")
            f.write(f"thread = threading.Thread(target=update_belief_set)\n")
            f.write(f"thread.start()\n")
            f.write(f"time.sleep(0.2)\n")

            for _, intention in self.intentions.items():
                f.write("\n")
                f.write(intention.function_string)
                f.write("\n")
            
            f.write(f"\n")
            f.write(f"{self.intentions[id].function_name}()\n")
            f.write(f"\n")
            f.write(f"thread_alive = False\n")
            f.write(f"thread.join()\n")
        
        self.last_content = ""
        self.thread_alive = True
        self.plan = []
        self.events = []

        thread1 = threading.Thread(target=self.belief_set_thread, args=(get_belief_set,))
        thread1.start()
        thread2 = threading.Thread(target=self.plan_thread, args=(execute_action,))
        thread2.start()

        error = None

        self.logger.log_info(f"Started subprocess...")
        self.logger.log_info(f"Belief set before intention {id} execution:\n{get_belief_set()}")

        try:
            process = subprocess.Popen(['python3', self.functions_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = process.communicate(timeout=self.timeout)
            if stderr != b'':
                raise Exception(stderr)
        except Exception as e:
            process.kill()
            error = e
            self.logger.log_error(f"Error during intention {id} execution. Intention {id} will be invalidated. Error: {e}")
        
        self.thread_alive = False
        thread1.join()
        thread2.join()

        self.logger.log_info(f"Intention {id} execution has finished. Threads and subprocess terminated. Plan: {self.plan}. Events: {self.events}")
        self.logger.log_info(f"Belief set after intention {id} execution:\n{get_belief_set()}")

        if error is not None:
            return error, self.plan, self.events
        
        return None, self.plan, self.events
    
    def plan_thread(self, execute_action):
        self.logger.log_info(f"Plan thread started ...")
        while self.thread_alive:
            with open(self.plan_file, "r") as file:
                plan = file.read()
                file.close()
            
            if plan != self.last_content:
                self.last_content = plan
                plan = plan.replace("\n", " ").split()
                action = plan[-1]
                self.logger.log_info(f"Executing action {action} ...")

                events = execute_action(action) # waits 0.2 to receive the events
                self.logger.log_info(f"Action {action} executed. Events received: {events}")
                self.plan.append(action)
                self.events.append(events)
                
                time.sleep(0.2) # make sure that the belief set integrates the events received with perception functions

                with open(self.continue_file, "w") as file:
                    file.write("True")
                    file.close()
            
            time.sleep(0.02)
        self.logger.log_info(f"Plan thread terminated.")

    def belief_set_thread(self, get_belief_set):
        self.logger.log_info(f"Belief set thread started ...")
        while self.thread_alive:
            with open(self.belief_set_file, "w") as file:
                file.write(str(get_belief_set()))
                file.close()
            time.sleep(0.02)
        self.logger.log_info(f"Belief set thread terminated.")
        
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

    def run_desire(self, id, get_belief_set, execute_action):
        if id is None:
            self.logger.log_info("No desire triggered.")
            return "No desire triggered.", None, None
        self.logger.log_info(f"Desire {id} is about to be executed ...")
        if False: # execute only last intention
            self.logger.log_info(f"Executing only last intention for desire {id} ...")
            if not self.desire_has_executable_intentions(id):
                self.logger.log_info(f"Desire {id} has no executable intentions.")
                self.desires[id].executable = False
                return f"Desire {id} has no executable intentions.", None, None
            intention = self.desires[id].intentions[-1]
            error, plan, events = self.run_intention(intention.id, get_belief_set, execute_action)
            if error is None:
                self.logger.log_info(f"Desire {id} plan has been executed.")
            else:
                self.desires[id].executable = False
                self.invalidate_intention(intention.id)
                self.logger.log_error(f"Error during plan execution of desire {id}. Desire {id} is now invalid and last intention has been invalidated.")
            return error, plan, events
        if True: # execute all valid intentions
            self.logger.log_info(f"Executing all valid intentions for desire {id} ...")
            if not self.desire_has_executable_intentions(id):
                self.logger.log_info(f"Desire {id} has no executable intentions.")
                self.desires[id].executable = False
                return f"Desire {id} has no executable intentions.", None, None
            final_plan = []
            final_events = []
            for intention in self.desires[id].intentions:
                if intention.executable:
                    self.logger.log_info(f"Executing intention {intention.id} ...")
                    error, plan, events = self.run_intention(intention.id, get_belief_set, execute_action)
                    if error is None:
                        self.logger.log_info(f"Intention {intention.id} has been executed with plan {plan} and events {events}.")
                        for action in plan:
                            final_plan.append(action)
                        for event in events:
                            final_events.append(event)
                    else:
                        self.desires[id].executable = False
                        self.invalidate_intention(intention.id)
                        self.logger.log_error(f"Error during intention {intention.id} execution. Desire {id} is now invalid and intention {intention.id} has been invalidated.")
                        return error, final_plan, final_events
            return None, final_plan, final_events
        if False: # execute all intentions
            self.logger.log_info(f"Executing all intentions for desire {id} ...")
            for intention in self.desires[id].intentions:
                self.logger.log_info(f"Executing intention {intention.id} ...")
                error, plan, events = self.run_intention(intention.id, get_belief_set, execute_action)
                if error is None:
                    self.logger.log_info(f"Intention {intention.id} has been executed with plan {plan} and events {events}.")
                else:
                    self.desires[id].executable = False
                    self.invalidate_intention(intention.id)
                    self.logger.log_error(f"Error during intention {intention.id} execution. Desire {id} is now invalid and intention {intention.id} has been invalidated.")
                    return error, plan, events
    
    def add_trigger_function(self, desire_id, function_string):
        function_string = self.rename_function(function_string, f"function_dtf_{self.dtf_number}")
        self.dtf_number += 1
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
            
            function_defs = [node for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
            if len(function_defs) != 1:
                return "The code contains more than one function definition."
            
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

    def desire_has_executable_intentions(self, id):
        for intention in self.desires[id].intentions:
            if intention.executable:
                return True
        return False

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

    def get_desire_description(self, id):
        return self.desires[id].description

    def get_intentions_called_by(self, id):
        intentions_called_ids = self.intentions_graph[id]
        for intention_id in intentions_called_ids:
            more_ids = self.get_intentions_called_by(intention_id)
            intentions_called_ids += more_ids
        return set(intentions_called_ids)
    
    def get_base_actions_list(self):
        return self.base_actions_names

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
            out += f"Executable: {desire.executable}\n"
            out += f"Trigger function:\n{desire.trigger_function_string}\n"
            out += "\n\n"
        return out

    def get_printable_intentions_graph(self):
        if not bool(self.intentions_graph):
            return "Empty"
        out = "\n"
        for id, calls in self.intentions_graph.items():
            out += f"    - [{id}] calls : {calls}\n"
        return out
    
    def get_analyzable_intentions_functions(self):
        all = ""
        intentions = {}
        all_working = ""
        working_intentions = {}
        all_not_working = ""
        not_working_intentions = {}
        for _, intention in self.intentions.items():
            all += intention.function_string
            all += "\n"
            intentions[intention.function_name] = intention.function_string
            if intention.executable:
                all_working += intention.function_string
                all_working += "\n"
                working_intentions[intention.function_name] = intention.function_string
            else:
                all_not_working += intention.function_string
                all_not_working += "\n"
                not_working_intentions[intention.function_name] = intention.function_string
        return all, all_working, all_not_working, intentions, working_intentions, not_working_intentions

    def get_analyzable_desires_trigger_functions(self):
        string = ""
        dtfs = {}
        for _, desire in self.desires.items():
            if desire.trigger_function_string is not None:
                string += desire.trigger_function_string
                string += "\n\n"
                dtfs[self.get_function_name(desire.trigger_function_string)] = desire.trigger_function_string
        return string, dtfs

    def get_number_desires(self):
        working = 0
        not_working = 0
        for desire in self.desires.values():
            if desire.executable:
                working += 1
            else:
                not_working += 1
        return working, not_working
    
    def get_number_intentions(self):
        working = 0
        not_working = 0
        for intention in self.intentions.values():
            if intention.executable:
                working += 1
            else:
                not_working += 1
        return working, not_working

    def add_tab(self, string, n_tabs):
        return "\n".join(["    " * n_tabs + line for line in string.split("\n")])