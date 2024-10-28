def function_7():
    global belief_set
    agent = belief_set['agent']
    keys = belief_set['keys']
    doors = belief_set['doors']
    if not agent['has_key']:
        nearest_key = min(keys.values(), key=lambda k: abs(k['coordinates']
            [0] - agent['coordinates'][0]) + abs(k['coordinates'][1] -
            agent['coordinates'][1]))
        if agent['coordinates'][0] > nearest_key['coordinates'][0]:
            function_1()
        elif agent['coordinates'][0] < nearest_key['coordinates'][0]:
            function_2()
        elif agent['coordinates'][1] > nearest_key['coordinates'][1]:
            function_3()
        elif agent['coordinates'][1] < nearest_key['coordinates'][1]:
            function_4()
        function_5()
    nearest_door = min(doors.values(), key=lambda d: abs(d['coordinates'][0
        ] - agent['coordinates'][0]) + abs(d['coordinates'][1] - agent[
        'coordinates'][1]))
    if agent['coordinates'][0] > nearest_door['coordinates'][0]:
        function_1()
    elif agent['coordinates'][0] < nearest_door['coordinates'][0]:
        function_2()
    elif agent['coordinates'][1] > nearest_door['coordinates'][1]:
        function_3()
    elif agent['coordinates'][1] < nearest_door['coordinates'][1]:
        function_4()
