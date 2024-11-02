def function_8():
    global belief_set
    agent_position = belief_set['agent'][1]['coordinates']
    parcel_spawn_location = [cell['cell_coordinates'] for cell in
        belief_set['map']['grid'] if cell['cell_type'] == 'parcels_spawn'][0]
    delivery_cell = [cell['cell_coordinates'] for cell in belief_set['map']
        ['grid'] if cell['cell_type'] == 'delivery_cell'][0]
    max_iterations = 1000
    i = 0
    while agent_position != parcel_spawn_location and i < max_iterations:
        i += 1
        if agent_position[0] < parcel_spawn_location[0]:
            function_2()
            agent_position[0] += 1
        elif agent_position[0] > parcel_spawn_location[0]:
            function_1()
            agent_position[0] -= 1
        elif agent_position[1] < parcel_spawn_location[1]:
            function_4()
            agent_position[1] += 1
        elif agent_position[1] > parcel_spawn_location[1]:
            function_3()
            agent_position[1] -= 1
    function_5()
    i = 0
    while agent_position != delivery_cell and i < max_iterations:
        i += 1
        if agent_position[0] < delivery_cell[0]:
            function_2()
            agent_position[0] += 1
        elif agent_position[0] > delivery_cell[0]:
            function_1()
            agent_position[0] -= 1
        elif agent_position[1] < delivery_cell[1]:
            function_4()
            agent_position[1] += 1
        elif agent_position[1] > delivery_cell[1]:
            function_3()
            agent_position[1] -= 1
    function_6()
