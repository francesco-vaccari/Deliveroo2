def function_7():
    global belief_set
    agent_coords = belief_set['agent'][1]['coordinates']
    parcel_coords = belief_set['parcels'][1]['coordinates']
    while agent_coords[0] != parcel_coords[0]:
        if agent_coords[0] > parcel_coords[0]:
            function_1()
            agent_coords[0] -= 1
        else:
            function_2()
            agent_coords[0] += 1
    while agent_coords[1] != parcel_coords[1]:
        if agent_coords[1] > parcel_coords[1]:
            function_3()
            agent_coords[1] -= 1
        else:
            function_4()
            agent_coords[1] += 1
    function_5()
    for cell in belief_set['map']['grid']:
        if 'delivery' in cell['cell_type']:
            delivery_coords = cell['cell_coordinates']
            break
    while agent_coords[0] != delivery_coords[0]:
        if agent_coords[0] > delivery_coords[0]:
            function_1()
            agent_coords[0] -= 1
        else:
            function_2()
            agent_coords[0] += 1
    while agent_coords[1] != delivery_coords[1]:
        if agent_coords[1] > delivery_coords[1]:
            function_3()
            agent_coords[1] -= 1
        else:
            function_4()
            agent_coords[1] += 1
    function_6()
