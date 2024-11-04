def function_7():
    global belief_set
    agent_position = belief_set['agent'][1]['coordinates']
    parcel_position = belief_set['parcels'][1]['coordinates']
    delivery_position = [belief_set['map']['grid'][i]['cell_coordinates'] for
        i in range(len(belief_set['map']['grid'])) if belief_set['map'][
        'grid'][i]['cell_type'] == 'delivery_cell'][0]
    while agent_position[0] != parcel_position[0]:
        if agent_position[0] > parcel_position[0]:
            function_1()
            agent_position[0] -= 1
        else:
            function_2()
            agent_position[0] += 1
    while agent_position[1] != parcel_position[1]:
        if agent_position[1] > parcel_position[1]:
            function_3()
            agent_position[1] -= 1
        else:
            function_4()
            agent_position[1] += 1
    function_5()
    while agent_position[0] != delivery_position[0]:
        if agent_position[0] > delivery_position[0]:
            function_1()
            agent_position[0] -= 1
        else:
            function_2()
            agent_position[0] += 1
    while agent_position[1] != delivery_position[1]:
        if agent_position[1] > delivery_position[1]:
            function_3()
            agent_position[1] -= 1
        else:
            function_4()
            agent_position[1] += 1
    function_6()
