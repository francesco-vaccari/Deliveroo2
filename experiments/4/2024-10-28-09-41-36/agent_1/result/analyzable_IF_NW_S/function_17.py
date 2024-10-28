def function_17():
    global belief_set
    agent_position = belief_set['agent']['coordinates']
    delivery_cells = [cell['cell_coordinates'] for cell in belief_set['map'
        ]['grid'] if 'delivery' in cell['cell_type']]
    closest_delivery_cell = min(delivery_cells, key=lambda cell: abs(cell[0
        ] - agent_position[0]) + abs(cell[1] - agent_position[1]))
    while agent_position != closest_delivery_cell:
        if agent_position[0] < closest_delivery_cell[0]:
            function_2()
        elif agent_position[0] > closest_delivery_cell[0]:
            function_1()
        elif agent_position[1] < closest_delivery_cell[1]:
            function_4()
        else:
            function_3()
    function_6()
