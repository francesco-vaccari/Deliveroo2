def function_9():
    global belief_set
    key_coordinates = belief_set['keys'][1]['coordinates']
    agent_coordinates = belief_set['agent']['coordinates']
    while agent_coordinates != key_coordinates:
        if key_coordinates[0] < agent_coordinates[0]:
            function_1()
        elif key_coordinates[0] > agent_coordinates[0]:
            function_2()
        elif key_coordinates[1] < agent_coordinates[1]:
            function_3()
        elif key_coordinates[1] > agent_coordinates[1]:
            function_4()
    function_5()
    door_coordinates = belief_set['doors'][1]['coordinates']
    while agent_coordinates != door_coordinates:
        if door_coordinates[0] < agent_coordinates[0]:
            function_1()
        elif door_coordinates[0] > agent_coordinates[0]:
            function_2()
        elif door_coordinates[1] < agent_coordinates[1]:
            function_3()
        elif door_coordinates[1] > agent_coordinates[1]:
            function_4()
    function_6()
