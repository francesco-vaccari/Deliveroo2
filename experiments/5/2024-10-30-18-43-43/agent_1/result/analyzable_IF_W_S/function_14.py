def function_14():
    global belief_set
    spawn_point = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'parcels_spawn'][0]['cell_coordinates']
    delivery_point = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'delivery_cell'][0]['cell_coordinates']
    agent_location = belief_set['agent'][1]['coordinates']
    while agent_location != spawn_point:
        if agent_location[0] < spawn_point[0]:
            function_2()
        elif agent_location[0] > spawn_point[0]:
            function_1()
        elif agent_location[1] < spawn_point[1]:
            function_4()
        else:
            function_3()
        agent_location = belief_set['agent'][1]['coordinates']
    function_5()
    while agent_location != delivery_point:
        if agent_location[0] < delivery_point[0]:
            function_2()
        elif agent_location[0] > delivery_point[0]:
            function_1()
        elif agent_location[1] < delivery_point[1]:
            function_4()
        else:
            function_3()
        agent_location = belief_set['agent'][1]['coordinates']
    function_6()
