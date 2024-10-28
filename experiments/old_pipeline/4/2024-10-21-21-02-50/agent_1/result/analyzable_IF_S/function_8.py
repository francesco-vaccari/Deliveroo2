def function_8():
    global belief_set
    agent_location = belief_set['agents'][1]['coordinates']
    key_location = belief_set['keys'][1]['coordinates']
    while agent_location != key_location:
        if agent_location[0] < key_location[0]:
            function_2()
        elif agent_location[0] > key_location[0]:
            function_1()
        elif agent_location[1] < key_location[1]:
            function_4()
        elif agent_location[1] > key_location[1]:
            function_3()
        agent_location = belief_set['agents'][1]['coordinates']
    function_5()
