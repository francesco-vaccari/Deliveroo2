def function_31():
    global belief_set
    agent = belief_set['agent']
    keys = belief_set['keys']
    doors = belief_set['doors']
    batteries = belief_set['batteries']
    if agent['energy'] < 30:
        function_29()
    elif not agent['has_key'] and keys:
        function_29()
    else:
        nearest_door = min(doors, key=lambda x: abs(doors[x]['coordinates']
            [0] - agent['coordinates'][0]) + abs(doors[x]['coordinates'][1] -
            agent['coordinates'][1]))
        door_x, door_y = doors[nearest_door]['coordinates']
        agent_x, agent_y = agent['coordinates']
        if door_x > agent_x:
            function_2()
        elif door_x < agent_x:
            function_1()
        elif door_y > agent_y:
            function_4()
        else:
            function_3()
