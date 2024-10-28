def function_14():
    global belief_set
    key_coordinates = belief_set['key'][1]['coordinates']
    agent_coordinates = belief_set['agent']['coordinates']
    while agent_coordinates != key_coordinates:
        if agent_coordinates[0] < key_coordinates[0]:
            function_2()
        elif agent_coordinates[0] > key_coordinates[0]:
            function_1()
        elif agent_coordinates[1] < key_coordinates[1]:
            function_4()
        elif agent_coordinates[1] > key_coordinates[1]:
            function_3()
    function_5()
