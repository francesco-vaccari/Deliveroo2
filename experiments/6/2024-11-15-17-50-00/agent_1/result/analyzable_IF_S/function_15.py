def function_15():
    global belief_set
    parcel_spawn_location = [cell['cell_coordinates'] for cell in
        belief_set['map']['grid'] if cell['cell_type'] == 'parcels_spawn'][0]
    agent_location = belief_set['agent'][1]['coordinates']
    while agent_location[0] > parcel_spawn_location[0]:
        function_1()
        agent_location[0] -= 1
    while agent_location[0] < parcel_spawn_location[0]:
        function_2()
        agent_location[0] += 1
    while agent_location[1] > parcel_spawn_location[1]:
        function_3()
        agent_location[1] -= 1
    while agent_location[1] < parcel_spawn_location[1]:
        function_4()
        agent_location[1] += 1
    function_5()
    delivery_cell_location = [cell['cell_coordinates'] for cell in
        belief_set['map']['grid'] if cell['cell_type'] == 'delivery_cell'][0]
    while agent_location[0] > delivery_cell_location[0]:
        function_1()
        agent_location[0] -= 1
    while agent_location[0] < delivery_cell_location[0]:
        function_2()
        agent_location[0] += 1
    while agent_location[1] > delivery_cell_location[1]:
        function_3()
        agent_location[1] -= 1
    while agent_location[1] < delivery_cell_location[1]:
        function_4()
        agent_location[1] += 1
    function_6()
