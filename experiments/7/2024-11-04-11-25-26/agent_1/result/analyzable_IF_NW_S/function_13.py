def function_13():
    global belief_set
    agent = belief_set['agent'][1]
    batteries = belief_set['batteries']
    delivery_cell = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'delivery_cell'][0]
    max_movements = 10
    movement_count = 0
    while agent['coordinates'] != batteries[0]['coordinates'
        ] and movement_count < max_movements:
        if agent['coordinates'][0] > batteries[0]['coordinates'][0
            ] and belief_set['map']['grid'][agent['coordinates'][0] - 1][agent
            ['coordinates'][1]]['cell_type'] != 'non_walkable':
            function_1()
        elif agent['coordinates'][0] < batteries[0]['coordinates'][0
            ] and belief_set['map']['grid'][agent['coordinates'][0] + 1][agent
            ['coordinates'][1]]['cell_type'] != 'non_walkable':
            function_2()
        elif agent['coordinates'][1] > batteries[0]['coordinates'][1
            ] and belief_set['map']['grid'][agent['coordinates'][0]][agent[
            'coordinates'][1] - 1]['cell_type'] != 'non_walkable':
            function_3()
        elif agent['coordinates'][1] < batteries[0]['coordinates'][1
            ] and belief_set['map']['grid'][agent['coordinates'][0]][agent[
            'coordinates'][1] + 1]['cell_type'] != 'non_walkable':
            function_4()
        agent['coordinates'] = [agent['coordinates'][0] + i[0], agent[
            'coordinates'][1] + i[1]]
        movement_count += 1
    if agent['coordinates'] == batteries[0]['coordinates']:
        function_5()
    while agent['coordinates'] != delivery_cell['cell_coordinates'
        ] and movement_count < max_movements:
        if agent['coordinates'][0] > delivery_cell['cell_coordinates'][0
            ] and belief_set['map']['grid'][agent['coordinates'][0] - 1][agent
            ['coordinates'][1]]['cell_type'] != 'non_walkable':
            function_1()
        elif agent['coordinates'][0] < delivery_cell['cell_coordinates'][0
            ] and belief_set['map']['grid'][agent['coordinates'][0] + 1][agent
            ['coordinates'][1]]['cell_type'] != 'non_walkable':
            function_2()
        elif agent['coordinates'][1] > delivery_cell['cell_coordinates'][1
            ] and belief_set['map']['grid'][agent['coordinates'][0]][agent[
            'coordinates'][1] - 1]['cell_type'] != 'non_walkable':
            function_3()
        elif agent['coordinates'][1] < delivery_cell['cell_coordinates'][1
            ] and belief_set['map']['grid'][agent['coordinates'][0]][agent[
            'coordinates'][1] + 1]['cell_type'] != 'non_walkable':
            function_4()
        agent['coordinates'] = [agent['coordinates'][0] + i[0], agent[
            'coordinates'][1] + i[1]]
        movement_count += 1
    if agent['coordinates'] == delivery_cell['cell_coordinates']:
        function_6()
