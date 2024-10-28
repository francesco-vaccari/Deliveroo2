def function_14():
    global belief_set
    while belief_set['agents'][1]['has_key'] == False:
        function_9()
        function_5()
    while belief_set['agents'][1]['has_key'] == True:
        function_1()
        function_5()
