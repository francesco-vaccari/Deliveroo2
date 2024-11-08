def function_18():
    global belief_set
    energy_threshold = 30
    energy = belief_set['agent']['energy']
    if energy < energy_threshold:
        function_14()
    else:
        function_1() if belief_set['agent']['coordinates'][0
            ] > 0 else function_2()
        function_3() if belief_set['agent']['coordinates'][1
            ] > 0 else function_4()
