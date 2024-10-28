def function_14():
    global belief_set
    agent_coords = belief_set['agent']['coordinates']
    delivery_cells = [cell['cell_coordinates'] for cell in belief_set['map'
        ]['grid'] if 'delivery' in cell['cell_type']]
    for cell in delivery_cells:
        if cell[0] < agent_coords[0]:
            function_1()
        elif cell[0] > agent_coords[0]:
            function_2()
        if cell[1] < agent_coords[1]:
            function_3()
        elif cell[1] > agent_coords[1]:
            function_4()
    if belief_set['agent']['parcels_carried_ids']:
        function_6()
