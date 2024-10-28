def function_8():
    global belief_set
    agent_position = belief_set['agent']['coordinates']
    delivery_position = [cell['cell_coordinates'] for cell in belief_set[
        'map']['grid'] if cell['cell_type'] == 'delivery_cell'][0]
    if agent_position[0] < delivery_position[0]:
        function_2()
    elif agent_position[0] > delivery_position[0]:
        function_1()
    elif agent_position[1] < delivery_position[1]:
        function_4()
    elif agent_position[1] > delivery_position[1]:
        function_3()
    else:
        function_6()
