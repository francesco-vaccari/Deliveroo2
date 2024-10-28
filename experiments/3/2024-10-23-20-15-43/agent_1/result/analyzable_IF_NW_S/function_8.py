def function_8():
    global belief_set
    agent = belief_set['agent']
    parcels = belief_set['parcels']
    parcel_coordinates = min(parcels.values(), key=lambda x: abs(x[
        'coordinates'][0] - agent['coordinates'][0]) + abs(x['coordinates']
        [1] - agent['coordinates'][1]))['coordinates']
    while agent['coordinates'] != parcel_coordinates:
        if agent['coordinates'][0] < parcel_coordinates[0]:
            function_2()
        elif agent['coordinates'][0] > parcel_coordinates[0]:
            function_1()
        elif agent['coordinates'][1] < parcel_coordinates[1]:
            function_4()
        elif agent['coordinates'][1] > parcel_coordinates[1]:
            function_3()
    function_5()
