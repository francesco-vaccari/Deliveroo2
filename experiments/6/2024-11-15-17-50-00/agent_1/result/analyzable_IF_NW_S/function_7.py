def function_7():
    global belief_set
    agent = belief_set['agent'][1]
    parcels = belief_set['parcels']
    batteries = belief_set['batteries']
    if agent['energy'] < 30:
        for battery in batteries.values():
            while agent['coordinates'] != battery['coordinates']:
                if agent['coordinates'][0] < battery['coordinates'][0]:
                    function_2()
                elif agent['coordinates'][0] > battery['coordinates'][0]:
                    function_1()
                elif agent['coordinates'][1] < battery['coordinates'][1]:
                    function_4()
                else:
                    function_3()
        function_5()
    for parcel in parcels.values():
        if parcel['carried_by_id'] is None:
            while agent['coordinates'] != parcel['coordinates']:
                if agent['coordinates'][0] < parcel['coordinates'][0]:
                    function_2()
                elif agent['coordinates'][0] > parcel['coordinates'][0]:
                    function_1()
                elif agent['coordinates'][1] < parcel['coordinates'][1]:
                    function_4()
                else:
                    function_3()
            function_5()
            while agent['coordinates'] != [2, 3]:
                if agent['coordinates'][0] < 2:
                    function_2()
                elif agent['coordinates'][0] > 2:
                    function_1()
                elif agent['coordinates'][1] < 3:
                    function_4()
                else:
                    function_3()
            function_6()
