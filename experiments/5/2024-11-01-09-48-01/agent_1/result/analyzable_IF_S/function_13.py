def function_13():
    global belief_set
    while True:
        if belief_set['agent'][1]['coordinates'] == belief_set['parcels'][16][
            'coordinates']:
            function_5()
        elif belief_set['agent'][1]['coordinates'] == [belief_set['map'][
            'grid'][7]['cell_coordinates'][0], belief_set['map']['grid'][7]
            ['cell_coordinates'][1]]:
            function_6()
        elif belief_set['agent'][1]['coordinates'][0] > belief_set['parcels'][
            16]['coordinates'][0] and belief_set['map']['grid'][(belief_set
            ['agent'][1]['coordinates'][0] - 1) * belief_set['map']['width'
            ] + belief_set['agent'][1]['coordinates'][1]]['cell_type'
            ] == 'walkable':
            function_1()
        elif belief_set['agent'][1]['coordinates'][0] < belief_set['parcels'][
            16]['coordinates'][0] and belief_set['map']['grid'][(belief_set
            ['agent'][1]['coordinates'][0] + 1) * belief_set['map']['width'
            ] + belief_set['agent'][1]['coordinates'][1]]['cell_type'
            ] == 'walkable':
            function_2()
        elif belief_set['agent'][1]['coordinates'][1] > belief_set['parcels'][
            16]['coordinates'][1] and belief_set['map']['grid'][belief_set[
            'agent'][1]['coordinates'][0] * belief_set['map']['width'] + (
            belief_set['agent'][1]['coordinates'][1] - 1)]['cell_type'
            ] == 'walkable':
            function_3()
        elif belief_set['agent'][1]['coordinates'][1] < belief_set['parcels'][
            16]['coordinates'][1] and belief_set['map']['grid'][belief_set[
            'agent'][1]['coordinates'][0] * belief_set['map']['width'] + (
            belief_set['agent'][1]['coordinates'][1] + 1)]['cell_type'
            ] == 'walkable':
            function_4()
        else:
            break
