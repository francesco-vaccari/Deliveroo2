def function_9():
    global belief_set
    delivery_cell = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'delivery_cell'][0]['cell_coordinates']
    agent_position = belief_set['agent']['coordinates']
    if delivery_cell[0] < agent_position[0]:
        function_1()
    elif delivery_cell[0] > agent_position[0]:
        function_2()
    elif delivery_cell[1] < agent_position[1]:
        function_3()
    elif delivery_cell[1] > agent_position[1]:
        function_4()
    else:
        function_6()
