def function_15():
    global belief_set
    agent_coords = belief_set['agent']['coordinates']
    delivery_cell_coords = [cell['cell_coordinates'] for cell in belief_set
        ['map']['grid'] if cell['cell_type'] == 'delivery_cell'][0]
    if agent_coords[0] < delivery_cell_coords[0]:
        function_2()
    elif agent_coords[0] > delivery_cell_coords[0]:
        function_1()
    elif agent_coords[1] < delivery_cell_coords[1]:
        function_4()
    elif agent_coords[1] > delivery_cell_coords[1]:
        function_3()
