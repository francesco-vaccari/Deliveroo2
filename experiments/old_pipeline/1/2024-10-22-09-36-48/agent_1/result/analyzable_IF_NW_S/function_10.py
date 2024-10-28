def function_10():
    global belief_set
    delivery_cell = [cell['cell_coordinates'] for cell in belief_set['map']
        ['grid'] if cell['cell_type'] == 'delivery_cell'][0]
    agent_position = belief_set['agent'][1]['coordinates']
    if agent_position[0] < delivery_cell[0]:
        function_2()
    elif agent_position[0] > delivery_cell[0]:
        function_1()
    elif agent_position[1] < delivery_cell[1]:
        function_4()
    elif agent_position[1] > delivery_cell[1]:
        function_3()
    else:
        function_6()
