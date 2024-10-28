def function_11():
    global belief_set
    parcel_location = [p['coordinates'] for p in belief_set['parcel'].
        values() if p['carried_by_id'] is None][0]
    agent_location = belief_set['agent'][1]['coordinates']
    while agent_location != parcel_location:
        if agent_location[0] < parcel_location[0]:
            function_2()
        elif agent_location[0] > parcel_location[0]:
            function_1()
        elif agent_location[1] < parcel_location[1]:
            function_4()
        elif agent_location[1] > parcel_location[1]:
            function_3()
        agent_location = belief_set['agent'][1]['coordinates']
    function_5()
    delivery_location = [c['cell_coordinates'] for c in belief_set['map'][
        'map']['grid'] if c['cell_type'] == 'delivery_cell'][0]
    while agent_location != delivery_location:
        if agent_location[0] < delivery_location[0]:
            function_2()
        elif agent_location[0] > delivery_location[0]:
            function_1()
        elif agent_location[1] < delivery_location[1]:
            function_4()
        elif agent_location[1] > delivery_location[1]:
            function_3()
        agent_location = belief_set['agent'][1]['coordinates']
    function_6()
