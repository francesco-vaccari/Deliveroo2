def function_7():
    global belief_set
    agent_x, agent_y = belief_set['agent']['coordinates']
    shortest_distance = float('inf')
    target_object = None
    for parcel in belief_set['parcels'].values():
        if parcel['carried_by_id'] is None:
            parcel_x, parcel_y = parcel['coordinates']
            distance = abs(agent_x - parcel_x) + abs(agent_y - parcel_y)
            if distance < shortest_distance:
                shortest_distance = distance
                target_object = parcel
    for key in belief_set['keys'].values():
        if key['carried_by_id'] is None:
            key_x, key_y = key['coordinates']
            distance = abs(agent_x - key_x) + abs(agent_y - key_y)
            if distance < shortest_distance:
                shortest_distance = distance
                target_object = key
    if target_object is not None:
        target_x, target_y = target_object['coordinates']
        if agent_x > target_x:
            function_1()
        elif agent_x < target_x:
            function_2()
        elif agent_y > target_y:
            function_3()
        elif agent_y < target_y:
            function_4()
        else:
            function_5()
