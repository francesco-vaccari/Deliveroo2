def function_14():
    global belief_set
    safety_counter = 0
    while belief_set['agent']['coordinates'] != belief_set['batteries'][1
        ] and safety_counter < 100:
        if belief_set['agent']['coordinates'][0] > belief_set['batteries'][1][0
            ]:
            function_1()
        elif belief_set['agent']['coordinates'][0] < belief_set['batteries'][1
            ][0]:
            function_2()
        elif belief_set['agent']['coordinates'][1] > belief_set['batteries'][1
            ][1]:
            function_3()
        elif belief_set['agent']['coordinates'][1] < belief_set['batteries'][1
            ][1]:
            function_4()
        safety_counter += 1
    if belief_set['agent']['coordinates'] == belief_set['batteries'][1]:
        function_5()
