def function_9():
    global belief_set
    agent = belief_set['agent'][1]
    parcels = belief_set['parcels']
    for parcel in parcels.values():
        if parcel['carried_by_id'] is None:
            parcel_x, parcel_y = parcel['coordinates']
            while agent['coordinates'][0] > parcel_x:
                function_1()
            while agent['coordinates'][0] < parcel_x:
                function_2()
            while agent['coordinates'][1] > parcel_y:
                function_3()
            while agent['coordinates'][1] < parcel_y:
                function_4()
            function_5()
