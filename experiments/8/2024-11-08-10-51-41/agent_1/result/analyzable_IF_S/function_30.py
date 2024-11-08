def function_30():
    global belief_set
    agent = belief_set['agent'][1]
    parcels = belief_set['parcels']
    batteries = belief_set['batteries']
    if agent['energy'] < 30:
        function_16()
    elif len(agent['parcels_carried_ids']) == 0:
        nearest_parcel = min(parcels, key=lambda x: abs(agent['coordinates'
            ][0] - parcels[x]['coordinates'][0]) + abs(agent['coordinates']
            [1] - parcels[x]['coordinates'][1]))
        parcel_coordinates = parcels[nearest_parcel]['coordinates']
        if agent['coordinates'][0] < parcel_coordinates[0]:
            function_2()
        elif agent['coordinates'][0] > parcel_coordinates[0]:
            function_1()
        elif agent['coordinates'][1] < parcel_coordinates[1]:
            function_4()
        elif agent['coordinates'][1] > parcel_coordinates[1]:
            function_3()
        function_5()
    else:
        function_14()
        function_6()
