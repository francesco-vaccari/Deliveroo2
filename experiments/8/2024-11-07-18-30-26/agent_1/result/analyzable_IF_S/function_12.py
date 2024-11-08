def function_12():
    global belief_set
    agent = belief_set['agent'][1]
    battery = belief_set['batteries'][1]
    while agent['coordinates'] != battery['coordinates']:
        if agent['coordinates'][0] < battery['coordinates'][0]:
            function_2()
        elif agent['coordinates'][0] > battery['coordinates'][0]:
            function_1()
        if agent['coordinates'][1] < battery['coordinates'][1]:
            function_4()
        elif agent['coordinates'][1] > battery['coordinates'][1]:
            function_3()
    function_5()
