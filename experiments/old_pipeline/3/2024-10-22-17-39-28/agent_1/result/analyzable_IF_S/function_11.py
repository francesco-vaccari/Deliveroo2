def function_11():
    global belief_set
    agent = belief_set['agent'][1]
    parcels = belief_set['parcels']
    for parcel in parcels.values():
        if parcel['carried_by_id'] == agent['id']:
            function_6()
            function_5()
            break
    if not agent['parcels_carried_ids']:
        function_5()
    if belief_set['map']['grid'][agent['coordinates'][0]][agent[
        'coordinates'][1]]['cell_type'] == 'delivery_cell':
        function_6()
    else:
        if agent['coordinates'][0] > 0:
            function_1()
        elif agent['coordinates'][0] < belief_set['map']['height'] - 1:
            function_2()
        if agent['coordinates'][1] > 0:
            function_3()
        elif agent['coordinates'][1] < belief_set['map']['width'] - 1:
            function_4()
