def function_12():
    global belief_set
    agent = belief_set['agent']
    parcels = belief_set['parcel']
    map_grid = belief_set['map']['grid']
    delivery_cells = [cell['cell_coordinates'] for cell in map_grid if cell
        ['cell_type'] in ['delivery_cell', 'double_delivery_cell']]
    min_distance = float('inf')
    nearest_delivery_cell = None
    for cell in delivery_cells:
        distance = abs(agent['coordinates'][0] - cell[0]) + abs(agent[
            'coordinates'][1] - cell[1])
        if distance < min_distance:
            min_distance = distance
            nearest_delivery_cell = cell
    while agent['coordinates'] != nearest_delivery_cell:
        if agent['coordinates'][0] < nearest_delivery_cell[0]:
            function_2()
        elif agent['coordinates'][0] > nearest_delivery_cell[0]:
            function_1()
        if agent['coordinates'][1] < nearest_delivery_cell[1]:
            function_4()
        elif agent['coordinates'][1] > nearest_delivery_cell[1]:
            function_3()
    function_6()
