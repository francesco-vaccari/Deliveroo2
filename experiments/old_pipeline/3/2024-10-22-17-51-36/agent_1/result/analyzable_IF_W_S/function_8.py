def function_8():
    global belief_set
    while belief_set['agent']['coordinates'] != belief_set['keys'][1][
        'coordinates']:
        if belief_set['agent']['coordinates'][0] < belief_set['keys'][1][
            'coordinates'][0]:
            function_2()
        elif belief_set['agent']['coordinates'][0] > belief_set['keys'][1][
            'coordinates'][0]:
            function_1()
        elif belief_set['agent']['coordinates'][1] < belief_set['keys'][1][
            'coordinates'][1]:
            function_4()
        elif belief_set['agent']['coordinates'][1] > belief_set['keys'][1][
            'coordinates'][1]:
            function_3()
    function_5()
    while belief_set['agent']['coordinates'] != belief_set['doors'][1][
        'coordinates']:
        if belief_set['agent']['coordinates'][0] < belief_set['doors'][1][
            'coordinates'][0]:
            function_2()
        elif belief_set['agent']['coordinates'][0] > belief_set['doors'][1][
            'coordinates'][0]:
            function_1()
        elif belief_set['agent']['coordinates'][1] < belief_set['doors'][1][
            'coordinates'][1]:
            function_4()
        elif belief_set['agent']['coordinates'][1] > belief_set['doors'][1][
            'coordinates'][1]:
            function_3()
    function_6()
