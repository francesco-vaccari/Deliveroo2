def function_14():
    global belief_set
    agent = belief_set['agent'][1]
    parcels = belief_set['parcels']
    for parcel in parcels:
        if parcel['carried_by_id'] is None:
            parcel_coords = parcel['coordinates']
            while agent['coordinates'] != parcel_coords:
                if agent['coordinates'][0] < parcel_coords[0]:
                    function_2()
                elif agent['coordinates'][0] > parcel_coords[0]:
                    function_1()
                elif agent['coordinates'][1] < parcel_coords[1]:
                    function_4()
                elif agent['coordinates'][1] > parcel_coords[1]:
                    function_3()
            function_5()
            break
