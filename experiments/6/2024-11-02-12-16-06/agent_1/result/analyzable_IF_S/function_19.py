def function_19():
    global belief_set
    agent_location = belief_set['agent'][1]['coordinates']
    parcels_spawn_location = [cell['cell_coordinates'] for cell in
        belief_set['map']['grid'] if cell['cell_type'] == 'parcels_spawn'][0]
    batteries_spawn_location = [cell['cell_coordinates'] for cell in
        belief_set['map']['grid'] if cell['cell_type'] == 'batteries_spawn'][0]
    delivery_cell_location = [cell['cell_coordinates'] for cell in
        belief_set['map']['grid'] if cell['cell_type'] == 'delivery_cell'][0]
    while agent_location != parcels_spawn_location:
        if agent_location[0] < parcels_spawn_location[0]:
            function_2()
        elif agent_location[0] > parcels_spawn_location[0]:
            function_1()
        elif agent_location[1] < parcels_spawn_location[1]:
            function_4()
        else:
            function_3()
        function_5()
    while agent_location != batteries_spawn_location:
        if agent_location[0] < batteries_spawn_location[0]:
            function_2()
        elif agent_location[0] > batteries_spawn_location[0]:
            function_1()
        elif agent_location[1] < batteries_spawn_location[1]:
            function_4()
        else:
            function_3()
        if belief_set['agent'][1]['energy'] < 50:
            function_5()
    while agent_location != delivery_cell_location:
        if agent_location[0] < delivery_cell_location[0]:
            function_2()
        elif agent_location[0] > delivery_cell_location[0]:
            function_1()
        elif agent_location[1] < delivery_cell_location[1]:
            function_4()
        else:
            function_3()
    function_6()
