def function_18():
    global belief_set
    key_coords = belief_set['key'][1]['coordinates']
    agent_coords = belief_set['agent']['coordinates']
    while agent_coords != key_coords:
        if agent_coords[0] < key_coords[0]:
            function_2()
        elif agent_coords[0] > key_coords[0]:
            function_1()
        elif agent_coords[1] < key_coords[1]:
            function_4()
        else:
            function_3()
    function_5()
    door_coords = belief_set['door'][1]['coordinates']
    while agent_coords != door_coords:
        if agent_coords[0] < door_coords[0]:
            function_2()
        elif agent_coords[0] > door_coords[0]:
            function_1()
        elif agent_coords[1] < door_coords[1]:
            function_4()
        else:
            function_3()
    function_6()
