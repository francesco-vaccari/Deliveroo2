def function_8():
    global belief_set
    agent = belief_set['agent']
    keys = belief_set['keys']
    if not agent['has_key'] and keys[1]['carried_by_id'] is None and agent[
        'coordinates'] == keys[1]['coordinates']:
        function_5()
        return
    doors = belief_set['doors']
    door_1 = doors[1]['coordinates']
    door_2 = doors[2]['coordinates']
    if agent['has_key']:
        if abs(agent['coordinates'][0] - door_1[0]) + abs(agent[
            'coordinates'][1] - door_1[1]) < abs(agent['coordinates'][0] -
            door_2[0]) + abs(agent['coordinates'][1] - door_2[1]):
            if agent['coordinates'][0] > door_1[0]:
                function_1()
            elif agent['coordinates'][0] < door_1[0]:
                function_2()
            elif agent['coordinates'][1] > door_1[1]:
                function_3()
            else:
                function_4()
        elif agent['coordinates'][0] > door_2[0]:
            function_1()
        elif agent['coordinates'][0] < door_2[0]:
            function_2()
        elif agent['coordinates'][1] > door_2[1]:
            function_3()
        else:
            function_4()
        return
