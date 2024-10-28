def function_12():
    global belief_set
    agent_coords = belief_set['agent']['coordinates']
    delivery_cells = [c['cell_coordinates'] for c in belief_set['map'][
        'grid'] if 'delivery' in c['cell_type']]
    nearest_delivery_cell = min(delivery_cells, key=lambda c: abs(c[0] -
        agent_coords[0]) + abs(c[1] - agent_coords[1]))
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
