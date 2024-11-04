def function_12():
    global belief_set
    coordinates = belief_set['agent'][1]['coordinates']
    battery_coordinates = belief_set['batteries'][1]['coordinates']
    while coordinates != battery_coordinates:
        if coordinates[0] < battery_coordinates[0]:
            function_2()
        elif coordinates[0] > battery_coordinates[0]:
            function_1()
        elif coordinates[1] < battery_coordinates[1]:
            function_4()
        elif coordinates[1] > battery_coordinates[1]:
            function_3()
        coordinates = belief_set['agent'][1]['coordinates']
    function_5()
    coordinates = belief_set['agent'][1]['coordinates']
    key_coordinates = belief_set['keys'][1]['coordinates']
    while coordinates != key_coordinates:
        if coordinates[0] < key_coordinates[0]:
            function_2()
        elif coordinates[0] > key_coordinates[0]:
            function_1()
        elif coordinates[1] < key_coordinates[1]:
            function_4()
        elif coordinates[1] > key_coordinates[1]:
            function_3()
        coordinates = belief_set['agent'][1]['coordinates']
    function_5()
