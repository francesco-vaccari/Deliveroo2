def function_7():
    global belief_set
    agent_pos = belief_set['agent']['coordinates']
    key_pos = belief_set['keys'][1]['coordinates']
    while agent_pos != key_pos:
        if agent_pos[0] > key_pos[0]:
            function_1()
        elif agent_pos[0] < key_pos[0]:
            function_2()
        if agent_pos[1] > key_pos[1]:
            function_3()
        elif agent_pos[1] < key_pos[1]:
            function_4()
    function_5()
