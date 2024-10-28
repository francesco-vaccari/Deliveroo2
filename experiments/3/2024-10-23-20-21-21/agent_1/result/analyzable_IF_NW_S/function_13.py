def function_13():
    global belief_set
    parcels = belief_set['parcels']
    agent = belief_set['agent']
    for parcel in parcels:
        if parcels[parcel]['coordinates'] == agent['coordinates']:
            function_5()
            function_12()
            break
        else:
            if parcels[parcel]['coordinates'][0] > agent['coordinates'][0]:
                function_2()
            elif parcels[parcel]['coordinates'][0] < agent['coordinates'][0]:
                function_1()
            if parcels[parcel]['coordinates'][1] > agent['coordinates'][1]:
                function_4()
            elif parcels[parcel]['coordinates'][1] < agent['coordinates'][1]:
                function_3()
