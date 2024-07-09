import ast
import astor
import importlib


def test_perception_function(function_string, events_list, belief_set):
    is_valid, function_name = is_valid_function(function_string)
    if not is_valid:
        return False, ValueError("Function is not valid.")
    
    try:
        local_scope = {}
        exec(function_string, {}, local_scope)
        func = local_scope[function_name]
        if events_list is not None:
            for event in events_list:
                func(event, belief_set)
    except Exception as e:
        return False, e
    
    return True, None


def test_control_function(function_string, belief_set, test_file_content, functions_names_list):
    with open("actions/test_functions.py", "w") as file:
        file.write(test_file_content)
    
    import actions.test_functions as test_functions
    global_scope = {}
    for name in functions_names_list:
        importlib.reload(test_functions)
        global_scope[name] = getattr(test_functions, name)
    
    is_valid, function_name = is_valid_function(function_string)
    if not is_valid:
        return False, ValueError("Function is not valid.")
    try:
        local_scope = {}
        exec(function_string, global_scope, local_scope)
        func = local_scope[function_name]
        func(belief_set)
    except Exception as e:
        print(e)
        return False, e

    return True, None


def test_desire_trigger_function(function_string, belief_set_current, belief_set_prior):
    is_valid, function_name = is_valid_function(function_string)
    if not is_valid:
        return False, ValueError("Function is not valid.")
    
    try:
        local_scope = {}
        exec(function_string, {}, local_scope)
        func = local_scope[function_name]
        result = func(belief_set_current)
        if not isinstance(result, bool):
            return False, ValueError("Function must return a boolean.")
        result = func(belief_set_prior)
        if not isinstance(result, bool):
            return False, ValueError("Function must return a boolean.")
    except Exception as e:
        return False, e
    
    return True, None


def is_valid_function(func_str):
    try:
        tree = ast.parse(func_str)
        if len(tree.body) == 1 and isinstance(tree.body[0], ast.FunctionDef):
            return True, tree.body[0].name
        return False, ""
    except SyntaxError:
        return False, ""


def rename_function(func_str, new_name):
    tree = ast.parse(func_str)
    
    if len(tree.body) == 1 and isinstance(tree.body[0], ast.FunctionDef):
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
    else:
        raise ValueError("Input string must contain exactly one function definition")


def get_function_name(func_str):
    tree = ast.parse(func_str)
    
    if len(tree.body) == 1 and isinstance(tree.body[0], ast.FunctionDef):
        function_def = tree.body[0]
        return function_def.name
    else:
        raise ValueError("Input string must contain exactly one function definition")


def check_library_functions(base_test_functions, not_base_test_functions, functions_names, function_to_test, belief_set):
    with open("actions/test_functions.py", "w") as file:
        file.write(base_test_functions + not_base_test_functions)
    
    import actions.test_functions as test_functions
    global_scope = {}
    for name in functions_names:
        importlib.reload(test_functions)
        global_scope[name] = getattr(test_functions, name)
    
    try:
        local_scope = {}
        exec(function_to_test, global_scope, local_scope)
        function_name = get_function_name(function_to_test)
        func = local_scope[function_name]
        func(belief_set)
    except Exception as e:
        return False
    return True
