def function_12():
    global belief_set
    delivery_cell_coordinates = [cell['cell_coordinates'] for cell in
        belief_set['map']['grid'] if cell['cell_type'] == 'delivery_cell'][0]
    agent_coordinates = belief_set['agent']['coordinates']
    while agent_coordinates != delivery_cell_coordinates:
        if agent_coordinates[0] < delivery_cell_coordinates[0]:
            function_2()
        elif agent_coordinates[0] > delivery_cell_coordinates[0]:
            function_1()
        elif agent_coordinates[1] < delivery_cell_coordinates[1]:
            function_4()
        else:
            function_3()
    function_6()
