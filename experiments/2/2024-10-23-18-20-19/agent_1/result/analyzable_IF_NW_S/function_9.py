def function_9():
    global belief_set
    key_coordinates = belief_set['key'][1]['coordinates']
    door_coordinates = belief_set['door'][1]['coordinates']
    max_iterations = 100
    iterations = 0
    while belief_set['agent']['coordinates'
        ] != key_coordinates and iterations < max_iterations:
        if belief_set['agent']['coordinates'][0] < key_coordinates[0]:
            function_2()
        elif belief_set['agent']['coordinates'][0] > key_coordinates[0]:
            function_1()
        elif belief_set['agent']['coordinates'][1] < key_coordinates[1]:
            function_4()
        elif belief_set['agent']['coordinates'][1] > key_coordinates[1]:
            function_3()
        iterations += 1
    function_5()
    while belief_set['agent']['coordinates'
        ] != door_coordinates and iterations < max_iterations:
        if belief_set['agent']['coordinates'][0] < door_coordinates[0]:
            function_2()
        elif belief_set['agent']['coordinates'][0] > door_coordinates[0]:
            function_1()
        elif belief_set['agent']['coordinates'][1] < door_coordinates[1]:
            function_4()
        elif belief_set['agent']['coordinates'][1] > door_coordinates[1]:
            function_3()
        iterations += 1
    belief_set['agent']['has_key'] = False
    belief_set['door'][1]['coordinates'] = None
