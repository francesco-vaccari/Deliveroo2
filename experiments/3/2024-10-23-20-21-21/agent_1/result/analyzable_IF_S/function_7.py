def function_7():
    global belief_set
    agent = belief_set['agent']
    parcels = belief_set['parcels']
    for parcel in parcels.values():
        if parcel['coordinates'][0] < agent['coordinates'][0]:
            function_1()
        elif parcel['coordinates'][0] > agent['coordinates'][0]:
            function_2()
        elif parcel['coordinates'][1] < agent['coordinates'][1]:
            function_3()
        elif parcel['coordinates'][1] > agent['coordinates'][1]:
            function_4()
    function_5()
