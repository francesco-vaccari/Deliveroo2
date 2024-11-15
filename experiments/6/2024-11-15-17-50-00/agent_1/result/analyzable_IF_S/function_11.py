def function_11():
    global belief_set
    agent = belief_set['agent'][1]
    agent_coords = agent['coordinates']
    if agent['energy'] < 30:
        battery_coords = belief_set['batteries'][1]['coordinates']
        if agent_coords[0] < battery_coords[0]:
            function_2()
        elif agent_coords[0] > battery_coords[0]:
            function_1()
        elif agent_coords[1] < battery_coords[1]:
            function_4()
        else:
            function_3()
    else:
        delivery_coords = [2, 3]
        if agent_coords[0] < delivery_coords[0]:
            function_2()
        elif agent_coords[0] > delivery_coords[0]:
            function_1()
        elif agent_coords[1] < delivery_coords[1]:
            function_4()
        else:
            function_3()
            function_6()
