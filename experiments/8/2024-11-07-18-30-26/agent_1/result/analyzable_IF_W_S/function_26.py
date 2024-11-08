def function_26():
    global belief_set
    key_coordinates = belief_set['keys'][2]['coordinates']
    agent_coordinates = belief_set['agent'][1]['coordinates']
    while agent_coordinates != key_coordinates:
        if agent_coordinates[0] < key_coordinates[0]:
            function_2()
            agent_coordinates[0] += 1
        elif agent_coordinates[0] > key_coordinates[0]:
            function_1()
            agent_coordinates[0] -= 1
        elif agent_coordinates[1] < key_coordinates[1]:
            function_4()
            agent_coordinates[1] += 1
        else:
            function_3()
            agent_coordinates[1] -= 1
    function_5()
