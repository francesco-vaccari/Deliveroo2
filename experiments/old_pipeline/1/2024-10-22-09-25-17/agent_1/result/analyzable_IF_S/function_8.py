def function_8():
    global belief_set
    spawn_point = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'parcels_spawn'][0]['cell_coordinates']
    delivery_point = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'delivery_cell'][0]['cell_coordinates']
    agent_position = belief_set['agent'][1]['coordinates']
    while agent_position != spawn_point:
        if spawn_point[0] < agent_position[0]:
            function_1()
        elif spawn_point[0] > agent_position[0]:
            function_2()
        elif spawn_point[1] < agent_position[1]:
            function_3()
        elif spawn_point[1] > agent_position[1]:
            function_4()
        agent_position = belief_set['agent'][1]['coordinates']
    function_5()
    while agent_position != delivery_point:
        if delivery_point[0] < agent_position[0]:
            function_1()
        elif delivery_point[0] > agent_position[0]:
            function_2()
        elif delivery_point[1] < agent_position[1]:
            function_3()
        elif delivery_point[1] > agent_position[1]:
            function_4()
        agent_position = belief_set['agent'][1]['coordinates']
    function_6()
