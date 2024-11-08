def function_28():
    global belief_set
    agent_coordinates = belief_set['agent']['coordinates']
    key_coordinates = [item['coordinates'] for item in belief_set['keys'].
        values()]
    door_coordinates = [item['coordinates'] for item in belief_set['doors']
        .values()]
    if belief_set['agent']['has_key'] == False:
        if key_coordinates:
            target_key_coordinates = key_coordinates[0]
            if target_key_coordinates[0] < agent_coordinates[0]:
                function_1()
            elif target_key_coordinates[0] > agent_coordinates[0]:
                function_2()
            elif target_key_coordinates[1] < agent_coordinates[1]:
                function_3()
            elif target_key_coordinates[1] > agent_coordinates[1]:
                function_4()
            else:
                function_5()
    elif door_coordinates:
        target_door_coordinates = door_coordinates[0]
        if target_door_coordinates[0] < agent_coordinates[0]:
            function_1()
        elif target_door_coordinates[0] > agent_coordinates[0]:
            function_2()
        elif target_door_coordinates[1] < agent_coordinates[1]:
            function_3()
        elif target_door_coordinates[1] > agent_coordinates[1]:
            function_4()
