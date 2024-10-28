def function_15():
    global belief_set
    agent = belief_set['agent']
    parcels = belief_set['parcels']
    if len(agent['parcels_carried_ids']) > 0:
        for parcel_id in agent['parcels_carried_ids']:
            if parcels[parcel_id]['coordinates'] == agent['coordinates']:
                function_6()
                return
        if agent['coordinates'][0] < 3:
            function_2()
        elif agent['coordinates'][0] > 3:
            function_1()
        elif agent['coordinates'][1] < 0:
            function_4()
        elif agent['coordinates'][1] > 0:
            function_3()
    else:
        function_10()
