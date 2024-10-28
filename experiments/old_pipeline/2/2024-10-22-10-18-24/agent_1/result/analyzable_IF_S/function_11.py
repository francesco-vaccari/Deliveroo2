def function_11():
    global belief_set
    delivery_cell_coords = next(cell['cell_coordinates'] for cell in
        belief_set['map']['grid'] if cell['cell_type'] == 'delivery_cell')
    agent_coords = belief_set['agent']['coordinates']
    while agent_coords != delivery_cell_coords:
        if agent_coords[0] < delivery_cell_coords[0]:
            function_2()
        elif agent_coords[0] > delivery_cell_coords[0]:
            function_1()
        elif agent_coords[1] < delivery_cell_coords[1]:
            function_4()
        elif agent_coords[1] > delivery_cell_coords[1]:
            function_3()
        agent_coords = belief_set['agent']['coordinates']
    function_6()
