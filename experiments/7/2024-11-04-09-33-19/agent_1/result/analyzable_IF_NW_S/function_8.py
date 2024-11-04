def function_8():
    global belief_set
    target_key = belief_set['keys'][0]['coordinates']
    target_door = belief_set['doors'][0]['coordinates']
    agent_position = belief_set['agent']['coordinates']
    max_iterations = 1000
    while agent_position != target_key and max_iterations > 0:
        if agent_position[0] < target_key[0]:
            function_2()
        elif agent_position[0] > target_key[0]:
            function_1()
        elif agent_position[1] < target_key[1]:
            function_4()
        elif agent_position[1] > target_key[1]:
            function_3()
        agent_position = belief_set['agent']['coordinates']
        max_iterations -= 1
    function_5()
    while agent_position != target_door and max_iterations > 0:
        if agent_position[0] < target_door[0]:
            function_2()
        elif agent_position[0] > target_door[0]:
            function_1()
        elif agent_position[1] < target_door[1]:
            function_4()
        elif agent_position[1] > target_door[1]:
            function_3()
        agent_position = belief_set['agent']['coordinates']
        max_iterations -= 1
