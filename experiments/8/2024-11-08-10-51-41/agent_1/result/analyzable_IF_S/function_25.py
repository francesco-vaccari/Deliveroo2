def function_25():
    global belief_set
    agent = belief_set['agent'][1]
    parcels = belief_set['parcels']
    min_distance = float('inf')
    nearest_parcel = None
    for parcel_id, parcel in parcels.items():
        if parcel['carried_by_id'] is not None:
            continue
        distance = abs(agent['coordinates'][0] - parcel['coordinates'][0]
            ) + abs(agent['coordinates'][1] - parcel['coordinates'][1])
        if distance < min_distance:
            min_distance = distance
            nearest_parcel = parcel
    if nearest_parcel is not None:
        if agent['coordinates'] == nearest_parcel['coordinates']:
            function_5()
        elif agent['coordinates'][0] > nearest_parcel['coordinates'][0]:
            function_1()
        elif agent['coordinates'][0] < nearest_parcel['coordinates'][0]:
            function_2()
        elif agent['coordinates'][1] > nearest_parcel['coordinates'][1]:
            function_3()
        elif agent['coordinates'][1] < nearest_parcel['coordinates'][1]:
            function_4()
