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
        error = self.is_valid_function(function_string)
        if error is not None:
            return error

        function_name = self.get_function_name(function_string)

        for event in test_events:
            local_vars = {}
            try:
                exec(function_string, {}, local_vars)
                func = local_vars[function_name]
                belief_set = func(event, belief_set)
            except Exception as e:
                return f"Error with input event: {event}\nError: {e}"
        
        return None
    
    def run_function(self, type, event, belief_set):
        function_string = self.functions[type][-1].function_string
        function_name = self.get_function_name(function_string)

        local_vars = {}
        try:
            exec(function_string, {}, local_vars)
            func = local_vars[function_name]
            return True, func(event, belief_set)
        except Exception as e:
            return False, None
    
    def add_function(self, type, function_string):
        self.functions[type] = []
        self.functions[type].append(PerceptionFunction(type, function_string))

    def remove_function(self, type):
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