def function_11():
    global belief_set
    delivery_cell = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'delivery_cell'][0]['cell_coordinates']
    agent_position = belief_set['agent'][1]['coordinates']
    while agent_position != delivery_cell:
        if agent_position[0] < delivery_cell[0]:
            function_2()
        elif agent_position[0] > delivery_cell[0]:
            function_1()
        elif agent_position[1] < delivery_cell[1]:
            function_4()
        elif agent_position[1] > delivery_cell[1]:
            function_3()
        agent_position = belief_set['agent'][1]['coordinates']
    function_6()
