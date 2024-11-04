def function_7():
    global belief_set
    agent_position = belief_set['agent']['coordinates']
    key_position = belief_set['keys'][0]['coordinates']
    while agent_position[0] != key_position[0]:
        if agent_position[0] > key_position[0]:
            function_1()
        else:
            function_2()
    while agent_position[1] != key_position[1]:
        if agent_position[1] > key_position[1]:
            function_3()
        else:
            function_4()
    function_5()
    door_position = belief_set['doors'][0]['coordinates']
    while agent_position[0] != door_position[0]:
        if agent_position[0] > door_position[0]:
            function_1()
        else:
            function_2()
    while agent_position[1] != door_position[1]:
        if agent_position[1] > door_position[1]:
            function_3()
        else:
            function_4()
