def function_10():
    global belief_set
    key_coordinates = None
    for key_id, key_info in belief_set['keys'].items():
        if key_info['carried_by_id'] is None:
            key_coordinates = key_info['coordinates']
            break
    if key_coordinates is None:
        return
    agent_coordinates = belief_set['agents'][1]['coordinates']
    while agent_coordinates[0] != key_coordinates[0]:
        if agent_coordinates[0] > key_coordinates[0]:
            function_1()
        else:
            function_2()
    while agent_coordinates[1] != key_coordinates[1]:
        if agent_coordinates[1] > key_coordinates[1]:
            function_3()
        else:
            function_4()
    function_5()
    door_coordinates = None
    for door_id, door_info in belief_set['doors'].items():
        door_coordinates = door_info['coordinates']
        break
    while agent_coordinates[0] != door_coordinates[0]:
        if agent_coordinates[0] > door_coordinates[0]:
            function_1()
        else:
            function_2()
    while agent_coordinates[1] != door_coordinates[1]:
        if agent_coordinates[1] > door_coordinates[1]:
            function_3()
        else:
            function_4()
