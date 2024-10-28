def function_12():
    global belief_set
    agent_coords = belief_set['agent']['coordinates']
    delivery_coords = [cell['cell_coordinates'] for cell in belief_set[
        'map']['grid'] if 'delivery' in cell['cell_type']]
    if delivery_coords[0][0] > agent_coords[0]:
        function_2()
    elif delivery_coords[0][0] < agent_coords[0]:
        function_1()
    elif delivery_coords[0][1] > agent_coords[1]:
        function_4()
    elif delivery_coords[0][1] < agent_coords[1]:
        function_3()
    else:
        function_6()
