def function_14():
    global belief_set
    key_coordinates = belief_set['keys'][1]['coordinates']
    agent_coordinates = belief_set['agent']['coordinates']
    if agent_coordinates[0] > key_coordinates[0]:
        function_1()
    elif agent_coordinates[0] < key_coordinates[0]:
        function_2()
    elif agent_coordinates[1] > key_coordinates[1]:
        function_3()
    elif agent_coordinates[1] < key_coordinates[1]:
        function_4()
    else:
        function_5()
        door_coordinates = belief_set['doors'][1]['coordinates']
        if agent_coordinates[0] > door_coordinates[0]:
            function_1()
        elif agent_coordinates[0] < door_coordinates[0]:
            function_2()
        elif agent_coordinates[1] > door_coordinates[1]:
            function_3()
        elif agent_coordinates[1] < door_coordinates[1]:
            function_4()
