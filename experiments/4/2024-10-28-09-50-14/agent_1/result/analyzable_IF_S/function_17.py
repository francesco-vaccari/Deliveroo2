def function_17():
    global belief_set
    agent = belief_set['agents'][1]
    if not agent['has_key']:
        nearest_key_location = min(belief_set['keys'], key=lambda k: abs(
            agent['coordinates'][0] - belief_set['keys'][k]['coordinates'][
            0]) + abs(agent['coordinates'][1] - belief_set['keys'][k][
            'coordinates'][1]))
        nearest_key_location = belief_set['keys'][nearest_key_location][
            'coordinates']
        previous_location = agent['coordinates'].copy()
        while agent['coordinates'] != nearest_key_location:
            if agent['coordinates'][0] < nearest_key_location[0]:
                function_2()
            elif agent['coordinates'][0] > nearest_key_location[0]:
                function_1()
            if agent['coordinates'][1] < nearest_key_location[1]:
                function_4()
            elif agent['coordinates'][1] > nearest_key_location[1]:
                function_3()
            if agent['coordinates'] == previous_location:
                break
            previous_location = agent['coordinates'].copy()
        if agent['coordinates'] == nearest_key_location:
            function_5()
