def function_14():
    global belief_set
    agent_coordinates = belief_set['agent']['coordinates']
    delivery_cell_coordinates = [cell['cell_coordinates'] for cell in
        belief_set['map']['grid'] if cell['cell_type'] in ['delivery_cell',
        'double_delivery_cell']]
    for coordinate in delivery_cell_coordinates:
        if agent_coordinates[0] < coordinate[0]:
            function_2()
        elif agent_coordinates[0] > coordinate[0]:
            function_1()
        if agent_coordinates[1] < coordinate[1]:
            function_4()
        elif agent_coordinates[1] > coordinate[1]:
            function_3()
    function_6()
