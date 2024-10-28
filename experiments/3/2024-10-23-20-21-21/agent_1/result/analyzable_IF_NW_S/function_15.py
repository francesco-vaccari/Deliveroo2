def function_15():
    global belief_set
    max_steps = 100
    steps = 0
    while belief_set['agent']['coordinates'] != belief_set['keys'][1][
        'coordinates'] and steps < max_steps:
        if belief_set['agent']['coordinates'][0] > belief_set['keys'][1][
            'coordinates'][0]:
            function_1()
        elif belief_set['agent']['coordinates'][0] < belief_set['keys'][1][
            'coordinates'][0]:
            function_2()
        elif belief_set['agent']['coordinates'][1] > belief_set['keys'][1][
            'coordinates'][1]:
            function_3()
        elif belief_set['agent']['coordinates'][1] < belief_set['keys'][1][
            'coordinates'][1]:
            function_4()
        steps += 1
    function_5()
    steps = 0
    while belief_set['agent']['coordinates'] != belief_set['map']['grid'][0][
        'cell_coordinates'] and steps < max_steps:
        if belief_set['agent']['coordinates'][0] > belief_set['map']['grid'][0
            ]['cell_coordinates'][0]:
            function_1()
        elif belief_set['agent']['coordinates'][0] < belief_set['map']['grid'][
            0]['cell_coordinates'][0]:
            function_2()
        elif belief_set['agent']['coordinates'][1] > belief_set['map']['grid'][
            0]['cell_coordinates'][1]:
            function_3()
        elif belief_set['agent']['coordinates'][1] < belief_set['map']['grid'][
            0]['cell_coordinates'][1]:
            function_4()
        steps += 1
    function_5()
    function_12()
