def function_16():
    global belief_set
    agent_coords = belief_set['agent'][1]['coordinates']
    parcel_spawn_coords = [cell['cell_coordinates'] for cell in belief_set[
        'map']['grid'] if cell['cell_type'] == 'parcels_spawn'][0]
    delivery_coords = [cell['cell_coordinates'] for cell in belief_set[
        'map']['grid'] if cell['cell_type'] == 'delivery_cell'][0]
    while agent_coords != parcel_spawn_coords:
        if parcel_spawn_coords[0] < agent_coords[0]:
            function_1()
        elif parcel_spawn_coords[0] > agent_coords[0]:
            function_2()
        elif parcel_spawn_coords[1] < agent_coords[1]:
            function_3()
        elif parcel_spawn_coords[1] > agent_coords[1]:
            function_4()
        agent_coords = belief_set['agent'][1]['coordinates']
    function_5()
    while agent_coords != delivery_coords:
        if delivery_coords[0] < agent_coords[0]:
            function_1()
        elif delivery_coords[0] > agent_coords[0]:
            function_2()
        elif delivery_coords[1] < agent_coords[1]:
            function_3()
        elif delivery_coords[1] > agent_coords[1]:
            function_4()
        agent_coords = belief_set['agent'][1]['coordinates']
    function_6()
