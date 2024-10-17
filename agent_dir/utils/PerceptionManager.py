import ast
import astor

class PerceptionFunction:
    def __init__(self, type, function_string):
        self.type = type
        self.function_string = function_string

class PerceptionManager:
    def __init__(self, logger):
        self.functions = {} # type -> [PerceptionFunction]
        self.logger = logger
        self.function_ids = 1

    def test_function(self, function_string, belief_set, test_events):
        self.logger.log_info(f"Testing function:\n{function_string}")
        error = self.is_valid_function(function_string)
        if error is not None:
            self.logger.log_error(f"Function is invalid. Error: {error}")
            return error

        function_name = self.get_function_name(function_string)

        for event in test_events:
            try:
                local_vars = {}
                exec(function_string, {}, local_vars)
                func = local_vars[function_name]
                belief_set = func(event, belief_set)
            except Exception as e:
                self.logger.log_error(f"Function is invalid. Error event: {event}\nError: {e}")
                return f"Error with input event: {event}\nError: {e}"
        
        self.logger.log_info("Function is valid.")
        return None
    
    def run_function(self, type, event, belief_set):
        self.logger.log_info(f"Running function for type: {type}")
        function_string = self.functions[type][-1].function_string
        function_name = self.get_function_name(function_string)

        local_vars = {}
        try:
            exec(function_string, {}, local_vars)
            func = local_vars[function_name]
            res = func(event, belief_set)
            self.logger.log_info(f"Function ran successfully. Result:\n{res}")
            return True, res
        except Exception as e:
            self.logger.log_error(f"Error running function. Error: {e}")
            return False, None
    
    def add_function(self, type, function_string):
        self.logger.log_info(f"Adding function for type: {type}")
        function_string = self.rename_function(function_string, f"function_{self.function_ids}")
        self.function_ids += 1
        if type not in self.functions:
            self.functions[type] = []
            self.functions[type].append(PerceptionFunction(type, function_string))
        else:
            if self.functions[type][-1] is None:
                self.functions[type][-1] = PerceptionFunction(type, function_string)
            else:
                self.functions[type].append(PerceptionFunction(type, function_string))
        self.logger.log_info(f"Functions: {self.get_printable_functions()}")

    def remove_function(self, type):
        self.logger.log_info(f"Removing function for type: {type}")
        self.functions[type].append(None)
    
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

    def is_function_ready(self, type):
        if type in self.functions:
            if self.functions[type][-1] is not None:
                return True
        return False
    
    def initialize_function(self, type):
        if type not in self.functions:
            self.functions[type] = []
            self.functions[type].append(None)
    
    def get_printable_functions(self):
        if not bool(self.functions):
            return "Empty"
        out = "\n"
        for type in self.functions:
            out += f"Type: {type}\n"
            for function in self.functions[type]:
                if function is not None:
                    out += f"{function.function_string}\n"
        out += "\n"
        return out

    def get_analyzable_perception_functions(self):
        all = ""
        functions = {}
        for type, pf_list in self.functions.items():
            for function in pf_list:
                if function is not None:
                    all += function.function_string + "\n\n"
                    functions[self.get_function_name(function.function_string)] = function.function_string
        return all, functions

    def get_number_perception_functions(self):
        count = 0
        for type, pf_list in self.functions.items():
            for function in pf_list:
                if function is not None:
                    count += 1
        return count