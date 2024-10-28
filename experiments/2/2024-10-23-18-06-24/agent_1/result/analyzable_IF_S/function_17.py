def function_17():
    global belief_set
    delivery_cell_coordinates = next(cell['cell_coordinates'] for cell in
        belief_set['map']['grid'] if cell['cell_type'] == 'delivery_cell')
    agent_coordinates = belief_set['agent']['coordinates']
    while agent_coordinates != delivery_cell_coordinates:
        if agent_coordinates[0] > delivery_cell_coordinates[0]:
            function_1()
        elif agent_coordinates[0] < delivery_cell_coordinates[0]:
            function_2()
        elif agent_coordinates[1] > delivery_cell_coordinates[1]:
            function_3()
        elif agent_coordinates[1] < delivery_cell_coordinates[1]:
            function_4()
        agent_coordinates = belief_set['agent']['coordinates']
    function_6()
