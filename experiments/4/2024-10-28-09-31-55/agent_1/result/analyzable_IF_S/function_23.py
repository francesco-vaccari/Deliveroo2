def function_23():
    global belief_set
    delivery_cells = [cell['cell_coordinates'] for cell in belief_set['map'
        ]['grid'] if 'delivery' in cell['cell_type']]
    agent_coords = belief_set['agent']['coordinates']
    nearest_delivery_cell = min(delivery_cells, key=lambda x: abs(x[0] -
        agent_coords[0]) + abs(x[1] - agent_coords[1]))
    while agent_coords != nearest_delivery_cell:
        if agent_coords[0] < nearest_delivery_cell[0]:
            function_2()
        elif agent_coords[0] > nearest_delivery_cell[0]:
            function_1()
        if agent_coords[1] < nearest_delivery_cell[1]:
            function_4()
        elif agent_coords[1] > nearest_delivery_cell[1]:
            function_3()
        agent_coords = belief_set['agent']['coordinates']
    function_6()
