def function_21():
    global belief_set
    agent = belief_set['agent'][1]
    if agent['has_key']:
        door_coordinates = belief_set['doors'][1]['coordinates']
        if agent['coordinates'][0] < door_coordinates[0]:
            function_2()
        elif agent['coordinates'][0] > door_coordinates[0]:
            function_1()
        elif agent['coordinates'][1] < door_coordinates[1]:
            function_4()
        else:
            function_3()
    else:
        key_coordinates = belief_set['keys'][1]['coordinates']
        if agent['coordinates'][0] < key_coordinates[0]:
            function_2()
        elif agent['coordinates'][0] > key_coordinates[0]:
            function_1()
        elif agent['coordinates'][1] < key_coordinates[1]:
            function_4()
        else:
            function_3()
        function_5()
