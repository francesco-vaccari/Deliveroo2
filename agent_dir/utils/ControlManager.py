import ast
import json
import astor
import importlib

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
        self.intentions = {} # id -> Intention
        self.intentions_graph = {} # id -> [id] the function id contains calls to the functions [id]
        self.desires = {} # id -> Desire
        self.logger = logger
        folder_path = 'agent_dir/functions'
        self.functions_file = folder_path + "/functions.py"
        self.load_actions(folder_path + "/actions.json")
    
    def load_actions(self, actions_path):
        actions = json.load(open(actions_path))["actions"]
        for action in actions:
            function_name = action["function_name"]
            description = action["description"]
            function_string = ""
            function_string += f"def {function_name}(belief_set):\n"
            function_string += f"    global plan\n"
            function_string += f"    plan.append('{action["action_name"]}')\n\n"
            self.intentions[self.intention_id] = Intention(self.intention_id, function_name, function_string, description)
            self.intentions_graph[self.intention_id] = []
            self.intention_id += 1
    
    def check_if_desire_triggered(self, belief_set):
        for id, desire in self.desires.items():
            if desire.executable and desire.trigger_function_string is not None:
                if self.run_desire_trigger(id, belief_set):
                    return id
        return None
    
    def test_intention(self, function_string, belief_set):
        error = self.is_valid_function(function_string)
        if error is not None:
            return error
        
        working_functions_names, _ = self.test_implemented_intentions(belief_set)
        
        extracted_calls = self.extract_function_calls(function_string)
        for function_called in extracted_calls:
            if function_called not in working_functions_names:
                return f"The function called {function_called} can no longer be used. Do not use {function_called}."

        import agent_dir.functions.functions as functions
        importlib.reload(functions)

        global_scope = {}
        for function_name in working_functions_names:
            global_scope[function_name] = getattr(functions, function_name)
        
        try:
            local_scope = {}
            exec(function_string, global_scope, local_scope)
            function_name = self.get_function_name(function_string)
            func = local_scope[function_name]
            func(belief_set)
        except Exception as e:
            return f"Error: {e}"
        
        return None

    def test_implemented_intentions(self, belief_set):
        f = open(self.functions_file, "w")
        f.write("plan = []\n")

        working_functions_names = []

        
        for id, intention in self.intentions.items():
            if intention.executable:
                import agent_dir.functions.functions as functions
                importlib.reload(functions)

                global_scope = {}
                for function_name in working_functions_names:
                    global_scope[function_name] = getattr(functions, function_name)

                try:
                    local_scope = {}
                    exec(intention.function_string, global_scope, local_scope)
                    func = local_scope[intention.function_name]
                    func(belief_set)
                    
                    f.write("\n")
                    f.write(intention.function_string)
                    f.write("\n")
                    working_functions_names.append(intention.function_name)
                except Exception as e:
                    self.invalidate_intention(id)
        
        f.close()
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

        return self.intention_id - 1
    
    def run_intention(self, id, belief_set):
        function_string = self.intentions[id].function_string

        working_functions_names = self.test_implemented_intentions(belief_set)

        if not self.intentions[id].executable:
            return None

        import agent_dir.functions.functions as functions
        importlib.reload(functions)

        global_scope = {}
        for function_name in working_functions_names:
            global_scope[function_name] = getattr(functions, function_name)
        
        try:
            local_scope = {}
            exec(function_string, global_scope, local_scope)
            function_name = self.get_function_name(function_string)
            func = local_scope[function_name]
            func(belief_set)
            return functions.plan
        except Exception as e:
            self.invalidate_intention(id)
            return None

    def invalidate_intention(self, id):
        self.intentions[id].executable = False
        for intention_id, intention_calls in self.intentions_graph.items():
            if id in intention_calls:
                self.invalidate_intention(intention_id)

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
        self.desire_id += 1
        return self.desire_id - 1

    def run_desire(self, id, belief_set):
        if id is None:
            return None
        concat_plans = []
        for intention in self.desires[id].intentions:
            plan = self.run_intention(intention.id, belief_set)
            if plan is None:
                return None
            concat_plans += plan
        return concat_plans
    
    def add_trigger_function(self, desire_id, function_string):
        self.desires[desire_id].trigger_function_string = function_string
        self.desires[desire_id].executable = True

    def test_trigger_function(self, function_string, prior, current):
        error = self.is_valid_function(function_string)
        if error is not None:
            return error
        
        function_name = self.get_function_name(function_string)

        local_vars = {}
        try:
            exec(function_string, {}, local_vars)
            func = local_vars[function_name]
            res = func(prior)
            if not (isinstance(res, bool) and res):
                return "The function does not return the boolean True for the prior belief set."
        except Exception as e:
            return f"Error: {e}"

        local_vars = {}
        try:
            exec(function_string, {}, local_vars)
            func = local_vars[function_name]
            res = func(current)
            if not isinstance(res, bool):
                raise Exception("The function does not return a boolean.")
        except Exception as e:
            return f"Error: {e}"
        
        return None

    def run_desire_trigger(self, id, belief_set):
        function_string = self.desires[id].trigger_function_string
        function_name = self.get_function_name(function_string)
        
        local_vars = {}
        try:
            exec(function_string, {}, local_vars)
            func = local_vars[function_name]
            return func(belief_set)
        except Exception as e:
            self.desires[id].executable = False
            return False
    
    def is_valid_function(self, function_string):
        try:
            tree = ast.parse(function_string)

            if len(tree.body) != 1:
                return "The code does not contain exactly one function definition."
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

    def get_library(self):
        intentions = {}
        for id, intention in self.intentions.items():
            if intention.executable:
                intentions[id] = intention
        return intentions
