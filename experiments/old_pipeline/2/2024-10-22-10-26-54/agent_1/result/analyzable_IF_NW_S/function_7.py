def function_7():
    global belief_set
    agent_coordinates = belief_set['agent']['coordinates']
    while belief_set['parcels'][1]['coordinates'] != agent_coordinates:
        if belief_set['parcels'][1]['coordinates'][0] < agent_coordinates[0]:
            function_1()
        elif belief_set['parcels'][1]['coordinates'][0] > agent_coordinates[0]:
            function_2()
        elif belief_set['parcels'][1]['coordinates'][1] < agent_coordinates[1]:
            function_3()
        elif belief_set['parcels'][1]['coordinates'][1] > agent_coordinates[1]:
            function_4()
        agent_coordinates = belief_set['agent']['coordinates']
    function_5()
    while belief_set['map']['grid'][7]['cell_coordinates'
        ] != agent_coordinates:
        if belief_set['map']['grid'][7]['cell_coordinates'][0
            ] < agent_coordinates[0]:
            function_1()
        elif belief_set['map']['grid'][7]['cell_coordinates'][0
            ] > agent_coordinates[0]:
            function_2()
        elif belief_set['map']['grid'][7]['cell_coordinates'][1
            ] < agent_coordinates[1]:
            function_3()
        elif belief_set['map']['grid'][7]['cell_coordinates'][1
            ] > agent_coordinates[1]:
            function_4()
        agent_coordinates = belief_set['agent']['coordinates']
    function_6()
