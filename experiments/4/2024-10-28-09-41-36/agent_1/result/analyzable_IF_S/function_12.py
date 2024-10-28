def function_12():
    global belief_set
    delivery_cells = [cell for cell in belief_set['map']['grid'] if 
        'delivery' in cell['cell_type']]
    agent_position = belief_set['agent']['coordinates']
    nearest_delivery_cell = min(delivery_cells, key=lambda cell: abs(cell[
        'cell_coordinates'][0] - agent_position[0]) + abs(cell[
        'cell_coordinates'][1] - agent_position[1]))
    while agent_position != nearest_delivery_cell['cell_coordinates']:
        if agent_position[0] < nearest_delivery_cell['cell_coordinates'][0]:
            function_2()
        elif agent_position[0] > nearest_delivery_cell['cell_coordinates'][0]:
            function_1()
        elif agent_position[1] < nearest_delivery_cell['cell_coordinates'][1]:
            function_4()
        elif agent_position[1] > nearest_delivery_cell['cell_coordinates'][1]:
            function_3()
        if agent_position == belief_set['agent']['coordinates']:
            break
        agent_position = belief_set['agent']['coordinates']
    function_6()
