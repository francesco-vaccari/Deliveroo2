def function_29():
    global belief_set
    agent_coordinates = belief_set['agent']['coordinates']
    key_coordinates = belief_set['keys'][2]['coordinates']
    battery_coordinates = belief_set['batteries'][2]
    if belief_set['agent']['energy'] < 30:
        if battery_coordinates[0] > agent_coordinates[0]:
            function_2()
        elif battery_coordinates[0] < agent_coordinates[0]:
            function_1()
        elif battery_coordinates[1] > agent_coordinates[1]:
            function_4()
        elif battery_coordinates[1] < agent_coordinates[1]:
            function_3()
        function_5()
    else:
        if key_coordinates[0] > agent_coordinates[0]:
            function_2()
        elif key_coordinates[0] < agent_coordinates[0]:
            function_1()
        elif key_coordinates[1] > agent_coordinates[1]:
            function_4()
        elif key_coordinates[1] < agent_coordinates[1]:
            function_3()
        function_5()
