def function_7():
    global belief_set
    parcel = list(belief_set['parcels'].values())[0]
    agent = belief_set['agents'][1]
    while parcel['coordinates'] != agent['coordinates']:
        if parcel['coordinates'][0] < agent['coordinates'][0]:
            function_1()
            agent['coordinates'][0] -= 1
        elif parcel['coordinates'][0] > agent['coordinates'][0]:
            function_2()
            agent['coordinates'][0] += 1
        elif parcel['coordinates'][1] < agent['coordinates'][1]:
            function_3()
            agent['coordinates'][1] -= 1
        elif parcel['coordinates'][1] > agent['coordinates'][1]:
            function_4()
            agent['coordinates'][1] += 1
    function_5()
    parcel['carried_by_id'] = 1
    agent['parcels_carried_ids'].append(parcel['id'])
