def function_13():
    global belief_set
    agent_coords = belief_set['agent']['coordinates']
    delivery_cells = [cell['cell_coordinates'] for cell in belief_set['map'
        ]['grid'] if 'delivery' in cell['cell_type']]
    destination = min(delivery_cells, key=lambda cell: abs(cell[0] -
        agent_coords[0]) + abs(cell[1] - agent_coords[1]))
    while agent_coords != destination:
        if agent_coords[0] > destination[0]:
            function_1()
        elif agent_coords[0] < destination[0]:
            function_2()
        if agent_coords[1] > destination[1]:
            function_3()
        elif agent_coords[1] < destination[1]:
            function_4()
    function_6()
