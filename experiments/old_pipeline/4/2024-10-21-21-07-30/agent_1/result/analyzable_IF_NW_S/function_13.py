def function_13():
    global belief_set
    agent_coords = belief_set['agent']['coordinates']
    for cell in belief_set['map']['grid']:
        if cell['cell_type'] == 'double_delivery_cell':
            delivery_coords = cell['cell_coordinates']
            break
    if agent_coords[0] < delivery_coords[0] and belief_set['map']['grid'][
        agent_coords[0] + 1][agent_coords[1]]['cell_type'] != 'non_walkable':
        function_2()
    elif agent_coords[0] > delivery_coords[0] and belief_set['map']['grid'][
        agent_coords[0] - 1][agent_coords[1]]['cell_type'] != 'non_walkable':
        function_1()
    elif agent_coords[1] < delivery_coords[1] and belief_set['map']['grid'][
        agent_coords[0]][agent_coords[1] + 1]['cell_type'] != 'non_walkable':
        function_4()
    elif agent_coords[1] > delivery_coords[1] and belief_set['map']['grid'][
        agent_coords[0]][agent_coords[1] - 1]['cell_type'] != 'non_walkable':
        function_3()
    if agent_coords == delivery_coords:
        function_6()
