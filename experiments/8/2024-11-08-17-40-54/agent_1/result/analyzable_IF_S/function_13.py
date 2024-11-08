def function_13():
    global belief_set
    agent = belief_set['agent']
    batteries = belief_set['batteries']
    for battery in batteries.values():
        while agent['coordinates'] != battery:
            if agent['coordinates'][0] < battery[0]:
                function_2()
            elif agent['coordinates'][0] > battery[0]:
                function_1()
            if agent['coordinates'][1] < battery[1]:
                function_4()
            elif agent['coordinates'][1] > battery[1]:
                function_3()
        function_5()
