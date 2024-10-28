def function_7():
    global belief_set
    agent_pos = belief_set['agent']['coordinates']
    key_pos = belief_set['keys'][1]['coordinates']
    while agent_pos != key_pos:
        if agent_pos[0] < key_pos[0]:
            function_2()
        elif agent_pos[0] > key_pos[0]:
            function_1()
        elif agent_pos[1] < key_pos[1]:
            function_4()
        elif agent_pos[1] > key_pos[1]:
            function_3()
        agent_pos = belief_set['agent']['coordinates']
    function_5()
    door_pos = min(belief_set['doors'].values(), key=lambda x: abs(x[
        'coordinates'][0] - agent_pos[0]) + abs(x['coordinates'][1] -
        agent_pos[1]))['coordinates']
    while agent_pos != door_pos:
        if agent_pos[0] < door_pos[0]:
            function_2()
        elif agent_pos[0] > door_pos[0]:
            function_1()
        elif agent_pos[1] < door_pos[1]:
            function_4()
        elif agent_pos[1] > door_pos[1]:
            function_3()
        agent_pos = belief_set['agent']['coordinates']
    function_6()
