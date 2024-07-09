# def get_two(number):
#     return number*2

# function = """def add_two(number):\n    number = number + get_two(number)\n    return number"""

# local_scope = {}
# global_scope = {"get_two": get_two}
# exec(function, global_scope, local_scope)

# func = local_scope["add_two"]
# print(func(2))

import actions.test_functions as test_functions

print(getattr(test_functions, "function_3"))