def function_29():
    global belief_set
    parcels = belief_set['parcels']
    agent = belief_set['agent'][1]
    min_distance = float('inf')
    nearest_parcel_coordinates = None
    for parcel_id, parcel_info in parcels.items():
        if parcel_info['carried_by_id'] is None:
            parcel_coordinates = parcel_info['coordinates']
            distance = abs(agent['coordinates'][0] - parcel_coordinates[0]
                ) + abs(agent['coordinates'][1] - parcel_coordinates[1])
            if distance < min_distance:
                min_distance = distance
                nearest_parcel_coordinates = parcel_coordinates
    if nearest_parcel_coordinates is not None:
        if agent['coordinates'][0] > nearest_parcel_coordinates[0]:
            function_1()
        elif agent['coordinates'][0] < nearest_parcel_coordinates[0]:
            function_2()
        elif agent['coordinates'][1] > nearest_parcel_coordinates[1]:
            function_3()
        elif agent['coordinates'][1] < nearest_parcel_coordinates[1]:
            function_4()
        elif agent['coordinates'] == nearest_parcel_coordinates:
            function_5()
    else:
        function_16()
