def function_19():
    global belief_set
    key_coordinates = belief_set['keys'][1]['coordinates']
    agent_coordinates = belief_set['agent'][1]['coordinates']
    while agent_coordinates[0] > key_coordinates[0]:
        function_1()
        agent_coordinates = belief_set['agent'][1]['coordinates']
    while agent_coordinates[0] < key_coordinates[0]:
        function_2()
        agent_coordinates = belief_set['agent'][1]['coordinates']
    while agent_coordinates[1] > key_coordinates[1]:
        function_3()
        agent_coordinates = belief_set['agent'][1]['coordinates']
    while agent_coordinates[1] < key_coordinates[1]:
        function_4()
        agent_coordinates = belief_set['agent'][1]['coordinates']
    function_5()
    function_4()
