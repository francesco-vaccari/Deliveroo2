def function_11():
    global belief_set
    agent_position = belief_set['agent']['coordinates']
    delivery_cells = [cell['cell_coordinates'] for cell in belief_set['map'
        ]['grid'] if 'delivery' in cell['cell_type']]
    nearest_delivery_cell = min(delivery_cells, key=lambda x: abs(x[0] -
        agent_position[0]) + abs(x[1] - agent_position[1]))
    while agent_position != nearest_delivery_cell:
        if nearest_delivery_cell[0] < agent_position[0]:
            function_1()
            agent_position[0] -= 1
        elif nearest_delivery_cell[0] > agent_position[0]:
            function_2()
            agent_position[0] += 1
        elif nearest_delivery_cell[1] < agent_position[1]:
            function_3()
            agent_position[1] -= 1
        elif nearest_delivery_cell[1] > agent_position[1]:
            function_4()
            agent_position[1] += 1
    function_6()
