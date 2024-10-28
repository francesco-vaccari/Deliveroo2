def function_16():
    global belief_set
    agent = belief_set['agent']
    delivery_cell = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'delivery_cell'][0]['cell_coordinates']
    while agent['coordinates'] != delivery_cell:
        if agent['coordinates'][0] < delivery_cell[0] and [cell for cell in
            belief_set['map']['grid'] if cell['cell_coordinates'] == [agent
            ['coordinates'][0] + 1, agent['coordinates'][1]]][0]['cell_type'
            ] == 'walkable':
            function_2()
        elif agent['coordinates'][0] > delivery_cell[0] and [cell for cell in
            belief_set['map']['grid'] if cell['cell_coordinates'] == [agent
            ['coordinates'][0] - 1, agent['coordinates'][1]]][0]['cell_type'
            ] == 'walkable':
            function_1()
        elif agent['coordinates'][1] < delivery_cell[1] and [cell for cell in
            belief_set['map']['grid'] if cell['cell_coordinates'] == [agent
            ['coordinates'][0], agent['coordinates'][1] + 1]][0]['cell_type'
            ] == 'walkable':
            function_4()
        elif agent['coordinates'][1] > delivery_cell[1] and [cell for cell in
            belief_set['map']['grid'] if cell['cell_coordinates'] == [agent
            ['coordinates'][0], agent['coordinates'][1] - 1]][0]['cell_type'
            ] == 'walkable':
            function_3()
        else:
            break
    if agent['coordinates'] == delivery_cell:
        function_6()
