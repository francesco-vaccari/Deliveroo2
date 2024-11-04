def function_9():
    global belief_set
    current_coordinates = belief_set['agent']['coordinates']
    doors = belief_set['doors']
    nearest_door_coordinates = min(doors, key=lambda x: abs(x['coordinates'
        ][0] - current_coordinates[0]) + abs(x['coordinates'][1] -
        current_coordinates[1]))['coordinates']
    while current_coordinates != nearest_door_coordinates:
        if nearest_door_coordinates[0] < current_coordinates[0]:
            function_1()
        elif nearest_door_coordinates[0] > current_coordinates[0]:
            function_2()
        elif nearest_door_coordinates[1] < current_coordinates[1]:
            function_3()
        else:
            function_4()
        current_coordinates = belief_set['agent']['coordinates']
    function_7()
    parcels = belief_set['parcels']
    nearest_parcel_coordinates = min(parcels, key=lambda x: abs(x[
        'coordinates'][0] - current_coordinates[0]) + abs(x['coordinates'][
        1] - current_coordinates[1]))['coordinates']
    while current_coordinates != nearest_parcel_coordinates:
        if nearest_parcel_coordinates[0] < current_coordinates[0]:
            function_1()
        elif nearest_parcel_coordinates[0] > current_coordinates[0]:
            function_2()
        elif nearest_parcel_coordinates[1] < current_coordinates[1]:
            function_3()
        else:
            function_4()
        current_coordinates = belief_set['agent']['coordinates']
    function_5()
