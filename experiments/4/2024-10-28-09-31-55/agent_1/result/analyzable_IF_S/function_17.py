def function_17():
    global belief_set
    agent_position = belief_set['agent']['coordinates']
    for cell in belief_set['map']['grid']:
        if cell['cell_type'] == 'delivery_cell' or cell['cell_type'
            ] == 'double_points_delivery_cell':
            delivery_position = cell['cell_coordinates']
            break
    if agent_position[0] > delivery_position[0]:
        function_1()
    elif agent_position[0] < delivery_position[0]:
        function_2()
    elif agent_position[1] > delivery_position[1]:
        function_3()
    elif agent_position[1] < delivery_position[1]:
        function_4()
    else:
        function_6()
