def function_8():
    global belief_set
    delivery_cell = next(cell for cell in belief_set['map']['grid'] if cell
        ['cell_type'] == 'delivery_cell')
    agent = belief_set['agent'][1]
    while agent['coordinates'] != delivery_cell['cell_coordinates']:
        if agent['coordinates'][0] < delivery_cell['cell_coordinates'][0] and [
            agent['coordinates'][0] + 1, agent['coordinates'][1]] not in [cell
            ['cell_coordinates'] for cell in belief_set['map']['grid'] if 
            cell['cell_type'] == 'non_walkable']:
            function_2()
        elif agent['coordinates'][0] > delivery_cell['cell_coordinates'][0
            ] and [agent['coordinates'][0] - 1, agent['coordinates'][1]
            ] not in [cell['cell_coordinates'] for cell in belief_set['map'
            ]['grid'] if cell['cell_type'] == 'non_walkable']:
            function_1()
        elif agent['coordinates'][1] < delivery_cell['cell_coordinates'][1
            ] and [agent['coordinates'][0], agent['coordinates'][1] + 1
            ] not in [cell['cell_coordinates'] for cell in belief_set['map'
            ]['grid'] if cell['cell_type'] == 'non_walkable']:
            function_4()
        elif agent['coordinates'][1] > delivery_cell['cell_coordinates'][1
            ] and [agent['coordinates'][0], agent['coordinates'][1] - 1
            ] not in [cell['cell_coordinates'] for cell in belief_set['map'
            ]['grid'] if cell['cell_type'] == 'non_walkable']:
            function_3()
    function_6()
