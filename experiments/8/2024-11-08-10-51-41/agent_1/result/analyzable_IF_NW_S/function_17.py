def function_17():
    global belief_set
    agent_coords = belief_set['agent'][1]['coordinates']
    key_coords = belief_set['keys'][1]['coordinates']
    has_key = belief_set['agent'][1]['has_key']
    if not has_key:
        if agent_coords[0] > key_coords[0]:
            function_1()
        elif agent_coords[0] < key_coords[0]:
            function_2()
        elif agent_coords[1] > key_coords[1]:
            function_3()
        elif agent_coords[1] < key_coords[1]:
            function_4()
        if agent_coords == key_coords:
            function_5()
    else:
        pass
