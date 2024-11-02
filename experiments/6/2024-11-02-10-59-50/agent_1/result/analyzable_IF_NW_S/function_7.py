def function_7():
    global belief_set
    agent_loc = belief_set['agent'][1]['coordinates']
    parcel_loc = belief_set['parcels'][1]['coordinates']
    delivery_loc = [cell['cell_coordinates'] for cell in belief_set['map'][
        'grid'] if cell['cell_type'] == 'delivery_cell'][0]
    while agent_loc != parcel_loc:
        if agent_loc[0] < parcel_loc[0]:
            function_2()
        elif agent_loc[0] > parcel_loc[0]:
            function_1()
        elif agent_loc[1] < parcel_loc[1]:
            function_4()
        else:
            function_3()
        agent_loc = belief_set['agent'][1]['coordinates']
    function_5()
    while agent_loc != delivery_loc:
        if agent_loc[0] < delivery_loc[0]:
            function_2()
        elif agent_loc[0] > delivery_loc[0]:
            function_1()
        elif agent_loc[1] < delivery_loc[1]:
            function_4()
        else:
            function_3()
        agent_loc = belief_set['agent'][1]['coordinates']
    function_6()
