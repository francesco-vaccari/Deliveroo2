def function_8():
    global belief_set
    agent_coordinates = belief_set['agent'][1]['coordinates']
    parcels_coordinates = belief_set['parcels'][1]['coordinates']
    while agent_coordinates[0] < parcels_coordinates[0]:
        function_2()
        agent_coordinates[0] += 1
    while agent_coordinates[0] > parcels_coordinates[0]:
        function_1()
        agent_coordinates[0] -= 1
    while agent_coordinates[1] < parcels_coordinates[1]:
        function_4()
        agent_coordinates[1] += 1
    while agent_coordinates[1] > parcels_coordinates[1]:
        function_3()
        agent_coordinates[1] -= 1
    function_5()
