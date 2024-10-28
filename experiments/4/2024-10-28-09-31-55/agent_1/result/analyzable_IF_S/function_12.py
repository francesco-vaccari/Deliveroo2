def function_12():
    global belief_set
    iteration_count = 0
    while True:
        iteration_count += 1
        if iteration_count > 100:
            break
        agent_coordinates = belief_set['agent']['coordinates']
        if belief_set['parcels'][1]['coordinates'] == agent_coordinates:
            function_5()
        elif belief_set['parcels'][1]['coordinates'][0] > agent_coordinates[0]:
            function_2()
        elif belief_set['parcels'][1]['coordinates'][0] < agent_coordinates[0]:
            function_1()
        elif belief_set['parcels'][1]['coordinates'][1] > agent_coordinates[1]:
            function_4()
        elif belief_set['parcels'][1]['coordinates'][1] < agent_coordinates[1]:
            function_3()
        if belief_set['agent']['parcels_carried_ids']:
            if belief_set['map']['grid'][12]['cell_coordinates'
                ] == agent_coordinates:
                function_6()
            elif belief_set['map']['grid'][12]['cell_coordinates'][0
                ] > agent_coordinates[0]:
                function_2()
            elif belief_set['map']['grid'][12]['cell_coordinates'][0
                ] < agent_coordinates[0]:
                function_1()
            elif belief_set['map']['grid'][12]['cell_coordinates'][1
                ] > agent_coordinates[1]:
                function_4()
            elif belief_set['map']['grid'][12]['cell_coordinates'][1
                ] < agent_coordinates[1]:
                function_3()
