def function_7():
    global belief_set
    key_coordinates = belief_set['key'][1]['coordinates']
    agent_coordinates = belief_set['agent']['coordinates']
    while agent_coordinates[0] < key_coordinates[0]:
        function_2()
        agent_coordinates = belief_set['agent']['coordinates']
    while agent_coordinates[0] > key_coordinates[0]:
        function_1()
        agent_coordinates = belief_set['agent']['coordinates']
    while agent_coordinates[1] < key_coordinates[1]:
        function_4()
        agent_coordinates = belief_set['agent']['coordinates']
    while agent_coordinates[1] > key_coordinates[1]:
        function_3()
        agent_coordinates = belief_set['agent']['coordinates']
    function_5()
