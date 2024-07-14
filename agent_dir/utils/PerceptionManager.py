import ast

class PerceptionFunction:
    def __init__(self, type, function_string):
        self.type = type
        self.function_string = function_string

class PerceptionManager:
    def __init__(self, logger):
        self.functions = {} # type -> [PerceptionFunction]
        self.logger = logger

    def test_function(self, function_string, belief_set, test_events):
        self.logger.log_info(f"Testing function: {function_string}")
        error = self.is_valid_function(function_string)
        if error is not None:
            self.logger.log_error(f"Function is invalid. Error: {error}")
            return error

        function_name = self.get_function_name(function_string)

        for event in test_events:
            local_vars = {}
            try:
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

    def is_function_ready(self, type):
        if type in self.functions:
            if self.functions[type][-1] is not None:
                return True
        return False
    
    def get_printable_functions(self):
        out = "\n"
        for type in self.functions:
            out += f"Type: {type}\n"
            for function in self.functions[type]:
                if function is not None:
                    out += f"{function.function_string}\n"
        return out