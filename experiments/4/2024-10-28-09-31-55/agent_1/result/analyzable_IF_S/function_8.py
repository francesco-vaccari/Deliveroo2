def function_8():
    global belief_set
    agent = belief_set['agent']
    parcel = next(iter(belief_set['parcels'].values()))
    if agent['coordinates'][0] < parcel['coordinates'][0]:
        function_2()
    elif agent['coordinates'][0] > parcel['coordinates'][0]:
        function_1()
    elif agent['coordinates'][1] < parcel['coordinates'][1]:
        function_4()
    elif agent['coordinates'][1] > parcel['coordinates'][1]:
        function_3()
