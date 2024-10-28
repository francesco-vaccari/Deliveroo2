def function_17():
    global belief_set
    delivery_cells = [cell['cell_coordinates'] for cell in belief_set['map'
        ]['grid'] if 'delivery' in cell['cell_type']]
    agent_position = belief_set['agent']['coordinates']
    delivery_cells.sort(key=lambda x: abs(x[0] - agent_position[0]) + abs(x
        [1] - agent_position[1]))
    nearest_delivery_cell = delivery_cells[0]
    while belief_set['agent']['coordinates'] != nearest_delivery_cell:
        if belief_set['agent']['coordinates'][0] < nearest_delivery_cell[0]:
            function_2()
        elif belief_set['agent']['coordinates'][0] > nearest_delivery_cell[0]:
            function_1()
        elif belief_set['agent']['coordinates'][1] < nearest_delivery_cell[1]:
            function_4()
        elif belief_set['agent']['coordinates'][1] > nearest_delivery_cell[1]:
            function_3()
    function_6()
