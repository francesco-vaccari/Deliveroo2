def function_12():
    global belief_set
    min_distance = float('inf')
    nearest_parcel = None
    for parcel_id, parcel_info in belief_set['parcels'].items():
        if parcel_info['carried_by_id'] is None:
            distance = abs(belief_set['agent'][1]['coordinates'][0] -
                parcel_info['coordinates'][0]) + abs(belief_set['agent'][1]
                ['coordinates'][1] - parcel_info['coordinates'][1])
            if distance < min_distance:
                min_distance = distance
                nearest_parcel = parcel_info
    while belief_set['agent'][1]['coordinates'] != nearest_parcel['coordinates'
        ]:
        if belief_set['agent'][1]['coordinates'][0] > nearest_parcel[
            'coordinates'][0]:
            function_1()
        elif belief_set['agent'][1]['coordinates'][0] < nearest_parcel[
            'coordinates'][0]:
            function_2()
        elif belief_set['agent'][1]['coordinates'][1] > nearest_parcel[
            'coordinates'][1]:
            function_3()
        else:
            function_4()
    function_5()
    for cell in belief_set['map']['grid']:
        if cell['cell_type'] == 'delivery_cell':
            delivery_cell = cell
            break
    while belief_set['agent'][1]['coordinates'] != delivery_cell[
        'cell_coordinates']:
        if belief_set['agent'][1]['coordinates'][0] > delivery_cell[
            'cell_coordinates'][0]:
            function_1()
        elif belief_set['agent'][1]['coordinates'][0] < delivery_cell[
            'cell_coordinates'][0]:
            function_2()
        elif belief_set['agent'][1]['coordinates'][1] > delivery_cell[
            'cell_coordinates'][1]:
            function_3()
        else:
            function_4()
    function_6()
