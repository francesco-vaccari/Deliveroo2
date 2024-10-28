def function_11():
    global belief_set
    key_coordinates = belief_set['keys'][1]['coordinates']
    agent_coordinates = belief_set['agent']['coordinates']
    counter = 0
    while agent_coordinates != key_coordinates and counter < 100:
        if agent_coordinates[0] < key_coordinates[0]:
            function_2()
        elif agent_coordinates[0] > key_coordinates[0]:
            function_1()
        if agent_coordinates[1] < key_coordinates[1]:
            function_4()
        elif agent_coordinates[1] > key_coordinates[1]:
            function_3()
        agent_coordinates = belief_set['agent']['coordinates']
        counter += 1
    if agent_coordinates == key_coordinates:
        function_5()
    else:
        return (
            'Error: The agent could not reach the key within the maximum number of moves.'
            )
