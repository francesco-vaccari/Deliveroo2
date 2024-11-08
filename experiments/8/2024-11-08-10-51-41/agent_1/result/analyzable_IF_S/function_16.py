def function_16():
    global belief_set
    agent = belief_set['agent'][1]
    battery_location = belief_set['batteries'][1]['coordinates']
    while agent['coordinates'] != battery_location:
        if agent['coordinates'][0] < battery_location[0]:
            function_2()
            agent['coordinates'][0] += 1
        elif agent['coordinates'][0] > battery_location[0]:
            function_1()
            agent['coordinates'][0] -= 1
        if agent['coordinates'][1] < battery_location[1]:
            function_4()
            agent['coordinates'][1] += 1
        elif agent['coordinates'][1] > battery_location[1]:
            function_3()
            agent['coordinates'][1] -= 1
    function_5()
