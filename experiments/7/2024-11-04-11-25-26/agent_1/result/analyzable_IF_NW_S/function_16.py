def function_16():
    global belief_set
    agent = belief_set['agent'][1]
    parcels = belief_set['parcels']
    batteries = belief_set['batteries']
    nearest_parcel = min(parcels, key=lambda x: abs(x['coordinates'][0] -
        agent['coordinates'][0]) + abs(x['coordinates'][1] - agent[
        'coordinates'][1]))
    while agent['coordinates'] != nearest_parcel['coordinates']:
        if agent['coordinates'][0] < nearest_parcel['coordinates'][0]:
            function_2()
        elif agent['coordinates'][0] > nearest_parcel['coordinates'][0]:
            function_1()
        elif agent['coordinates'][1] < nearest_parcel['coordinates'][1]:
            function_4()
        else:
            function_3()
    function_5()
    if agent['energy'] < 20:
        nearest_battery = min(batteries, key=lambda x: abs(x['coordinates']
            [0] - agent['coordinates'][0]) + abs(x['coordinates'][1] -
            agent['coordinates'][1]))
        while agent['coordinates'] != nearest_battery['coordinates']:
            if agent['coordinates'][0] < nearest_battery['coordinates'][0]:
                function_2()
            elif agent['coordinates'][0] > nearest_battery['coordinates'][0]:
                function_1()
            elif agent['coordinates'][1] < nearest_battery['coordinates'][1]:
                function_4()
            else:
                function_3()
        function_5()
