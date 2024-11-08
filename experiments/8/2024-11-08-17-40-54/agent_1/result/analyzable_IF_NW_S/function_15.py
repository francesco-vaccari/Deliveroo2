def function_15():
    global belief_set
    key_position = belief_set['keys'][1]['coordinates']
    agent_position = belief_set['agent']['coordinates']
    while agent_position != key_position:
        if key_position[0] < agent_position[0]:
            function_1()
        elif key_position[0] > agent_position[0]:
            function_2()
        if key_position[1] < agent_position[1]:
            function_3()
        elif key_position[1] > agent_position[1]:
            function_4()
    function_5()
