def function_12():
    global belief_set
    agent = belief_set['agents'][1]
    delivery_cells = [cell for cell in belief_set['map']['grid'] if 
        'delivery' in cell['cell_type']]
    min_distance = float('inf')
    target_cell = None
    for cell in delivery_cells:
        distance = abs(agent['coordinates'][0] - cell['cell_coordinates'][0]
            ) + abs(agent['coordinates'][1] - cell['cell_coordinates'][1])
        if distance < min_distance:
            min_distance = distance
            target_cell = cell
    if target_cell:
        if agent['coordinates'][0] > target_cell['cell_coordinates'][0]:
            function_1()
        elif agent['coordinates'][0] < target_cell['cell_coordinates'][0]:
            function_2()
        elif agent['coordinates'][1] > target_cell['cell_coordinates'][1]:
            function_3()
        elif agent['coordinates'][1] < target_cell['cell_coordinates'][1]:
            function_4()
        else:
            function_6()
