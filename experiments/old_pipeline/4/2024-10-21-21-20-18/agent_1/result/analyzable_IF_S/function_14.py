def function_14():
    global belief_set
    agent = belief_set['agent']
    map_grid = belief_set['map']['grid']
    delivery_cells = [cell for cell in map_grid if cell['cell_type'] in [
        'delivery_cell', 'double_delivery_cell']]
    nearest_delivery_cell = min(delivery_cells, key=lambda cell: abs(cell[
        'cell_coordinates'][0] - agent['coordinates'][0]) + abs(cell[
        'cell_coordinates'][1] - agent['coordinates'][1]))
    while agent['coordinates'] != nearest_delivery_cell['cell_coordinates']:
        if agent['coordinates'][0] < nearest_delivery_cell['cell_coordinates'][
            0]:
            function_2()
        elif agent['coordinates'][0] > nearest_delivery_cell['cell_coordinates'
            ][0]:
            function_1()
        elif agent['coordinates'][1] < nearest_delivery_cell['cell_coordinates'
            ][1]:
            function_4()
        elif agent['coordinates'][1] > nearest_delivery_cell['cell_coordinates'
            ][1]:
            function_3()
    function_6()
