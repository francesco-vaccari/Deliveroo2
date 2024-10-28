def function_8():
    global belief_set
    agent_coordinates = belief_set['agent']['coordinates']
    delivery_cell_coordinates = [cell['cell_coordinates'] for cell in
        belief_set['map']['grid'] if cell['cell_type'] in ['delivery_cell',
        'double_delivery_cell']][0]
    while agent_coordinates[0] < delivery_cell_coordinates[0]:
        function_2()
        agent_coordinates[0] += 1
    while agent_coordinates[0] > delivery_cell_coordinates[0]:
        function_1()
        agent_coordinates[0] -= 1
    while agent_coordinates[1] < delivery_cell_coordinates[1]:
        function_4()
        agent_coordinates[1] += 1
    while agent_coordinates[1] > delivery_cell_coordinates[1]:
        function_3()
        agent_coordinates[1] -= 1
    function_6()
