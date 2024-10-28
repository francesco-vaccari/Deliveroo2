def function_7():
    global belief_set
    agent = belief_set['agent'][1]
    parcel = belief_set['parcel'][1]
    while agent['coordinates'] != parcel['coordinates']:
        if agent['coordinates'][0] > parcel['coordinates'][0]:
            function_1()
        elif agent['coordinates'][0] < parcel['coordinates'][0]:
            function_2()
        if agent['coordinates'][1] > parcel['coordinates'][1]:
            function_3()
        elif agent['coordinates'][1] < parcel['coordinates'][1]:
            function_4()
    function_5()
