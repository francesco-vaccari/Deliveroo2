def function_9():
    global belief_set
    current_coords = belief_set['agent']['coordinates']
    new_coords = [current_coords[0] - 1, current_coords[1]]
    for cell in belief_set['map']['grid']:
        if cell['cell_coordinates'] == new_coords and cell['cell_type'
            ] == 'walkable':
            if belief_set['agent']['energy'] > 10:
                function_1()
                break
