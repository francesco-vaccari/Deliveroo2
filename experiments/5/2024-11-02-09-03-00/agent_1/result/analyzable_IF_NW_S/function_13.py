def function_13():
    global belief_set
    agent = belief_set['agent'][1]
    while agent['coordinates'] != [0, 0]:
        if agent['coordinates'][0] > 0:
            function_1()
        elif agent['coordinates'][1] > 0:
            function_3()
    function_5()
    while agent['coordinates'] != [1, 3]:
        if agent['coordinates'][0] < 1:
            function_2()
        elif agent['coordinates'][1] < 3:
            function_4()
    function_6()
