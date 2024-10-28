def function_7():
    global belief_set
    agent_pos = belief_set['agent']['coordinates']
    key_pos = belief_set['keys'][1]['coordinates']
    door_pos = belief_set['doors'][1]['coordinates']
    if agent_pos[0] > key_pos[0]:
        function_1()
    elif agent_pos[0] < key_pos[0]:
        function_2()
    elif agent_pos[1] > key_pos[1]:
        function_3()
    elif agent_pos[1] < key_pos[1]:
        function_4()
    else:
        function_5()
    if belief_set['agent']['has_key'] is True:
        if agent_pos[0] > door_pos[0]:
            function_1()
        elif agent_pos[0] < door_pos[0]:
            function_2()
        elif agent_pos[1] > door_pos[1]:
            function_3()
        elif agent_pos[1] < door_pos[1]:
            function_4()
