def function_12():
    global belief_set
    delivery_cell = [cell['cell_coordinates'] for cell in belief_set['map']
        ['grid'] if cell['cell_type'] == 'delivery_cell'][0]
    agent_coords = belief_set['agent']['coordinates']
    while agent_coords != delivery_cell:
        if agent_coords[0] < delivery_cell[0]:
            function_2()
        elif agent_coords[0] > delivery_cell[0]:
            function_1()
        elif agent_coords[1] < delivery_cell[1]:
            function_4()
        elif agent_coords[1] > delivery_cell[1]:
            function_3()
        agent_coords = belief_set['agent']['coordinates']
    function_6()