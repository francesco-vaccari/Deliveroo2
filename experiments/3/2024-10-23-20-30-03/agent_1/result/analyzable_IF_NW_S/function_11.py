def function_11():
    global belief_set
    agent_id = 1
    agent = belief_set['agents'][agent_id]
    key = [k for k in belief_set['keys'].values() if k['carried_by_id'] is None
        ][0]
    key_coords = key['coordinates']
    iteration_count = 0
    while agent['coordinates'] != key_coords and iteration_count < 100:
        if agent['coordinates'][0] > key_coords[0]:
            function_1()
        elif agent['coordinates'][0] < key_coords[0]:
            function_2()
        elif agent['coordinates'][1] > key_coords[1]:
            function_3()
        elif agent['coordinates'][1] < key_coords[1]:
            function_4()
        agent['coordinates'] = [agent['coordinates'][0] - 1 if agent[
            'coordinates'][0] > key_coords[0] else agent['coordinates'][0] +
            1 if agent['coordinates'][0] < key_coords[0] else agent[
            'coordinates'][0], agent['coordinates'][1] - 1 if agent[
            'coordinates'][1] > key_coords[1] else agent['coordinates'][1] +
            1 if agent['coordinates'][1] < key_coords[1] else agent[
            'coordinates'][1]]
        iteration_count += 1
    function_5()
    if 'has_key' in agent and agent['has_key']:
        door_coords = [d['coordinates'] for d in belief_set['doors'].values()][
            0]
        iteration_count = 0
        while agent['coordinates'] != door_coords and iteration_count < 100:
            if agent['coordinates'][0] > door_coords[0]:
                function_1()
            elif agent['coordinates'][0] < door_coords[0]:
                function_2()
            elif agent['coordinates'][1] > door_coords[1]:
                function_3()
            elif agent['coordinates'][1] < door_coords[1]:
                function_4()
            agent['coordinates'] = [agent['coordinates'][0] - 1 if agent[
                'coordinates'][0] > door_coords[0] else agent['coordinates'
                ][0] + 1 if agent['coordinates'][0] < door_coords[0] else
                agent['coordinates'][0], agent['coordinates'][1] - 1 if 
                agent['coordinates'][1] > door_coords[1] else agent[
                'coordinates'][1] + 1 if agent['coordinates'][1] <
                door_coords[1] else agent['coordinates'][1]]
            iteration_count += 1
