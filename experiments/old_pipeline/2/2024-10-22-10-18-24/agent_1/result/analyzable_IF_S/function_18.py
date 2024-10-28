def function_18():
    global belief_set
    agent_position = belief_set['agent']['coordinates']
    delivery_cell_position = [cell['cell_coordinates'] for cell in
        belief_set['map']['grid'] if cell['cell_type'] == 'delivery_cell'][0]
    if 'parcel' in belief_set and belief_set['parcel'][1]['coordinates'
        ] == agent_position:
        function_5()
    elif 'key' in belief_set and belief_set['key'][1]['coordinates'
        ] == agent_position:
        function_5()
    elif agent_position[0] < delivery_cell_position[0]:
        function_2()
    elif agent_position[0] > delivery_cell_position[0]:
        function_1()
    elif agent_position[1] < delivery_cell_position[1]:
        function_4()
    elif agent_position[1] > delivery_cell_position[1]:
        function_3()
