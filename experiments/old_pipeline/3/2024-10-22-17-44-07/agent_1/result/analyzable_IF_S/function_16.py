def function_16():
    global belief_set
    current_position = belief_set['agent']['coordinates']
    map_grid = belief_set['map']['grid']
    walkable_cells = [cell['cell_coordinates'] for cell in map_grid if cell
        ['cell_type'] == 'walkable']
    nearest_walkable_cell = min(walkable_cells, key=lambda cell: abs(cell[0
        ] - current_position[0]) + abs(cell[1] - current_position[1]))
    if nearest_walkable_cell[0] < current_position[0]:
        function_1()
    elif nearest_walkable_cell[0] > current_position[0]:
        function_2()
    elif nearest_walkable_cell[1] < current_position[1]:
        function_3()
    elif nearest_walkable_cell[1] > current_position[1]:
        function_4()
