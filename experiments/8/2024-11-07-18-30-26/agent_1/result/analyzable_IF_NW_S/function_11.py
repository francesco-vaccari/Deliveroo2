def function_11():
    global belief_set
    min_distance = float('inf')
    nearest_parcel = None
    for parcel in belief_set['parcels'].values():
        distance = abs(parcel['coordinates'][0] - belief_set['agent'][1][
            'coordinates'][0]) + abs(parcel['coordinates'][1] - belief_set[
            'agent'][1]['coordinates'][1])
        if distance < min_distance:
            min_distance = distance
            nearest_parcel = parcel
    while belief_set['agent'][1]['coordinates'] != nearest_parcel['coordinates'
        ]:
        if belief_set['agent'][1]['coordinates'][0] < nearest_parcel[
            'coordinates'][0]:
            function_2()
        elif belief_set['agent'][1]['coordinates'][0] > nearest_parcel[
            'coordinates'][0]:
            function_1()
        elif belief_set['agent'][1]['coordinates'][1] < nearest_parcel[
            'coordinates'][1]:
            function_4()
        elif belief_set['agent'][1]['coordinates'][1] > nearest_parcel[
            'coordinates'][1]:
            function_3()
    function_5()
    for cell in belief_set['map']['grid']:
        if cell['cell_type'] == 'delivery_cell':
            delivery_cell = cell
    while belief_set['agent'][1]['coordinates'] != delivery_cell[
        'cell_coordinates']:
        if belief_set['agent'][1]['coordinates'][0] < delivery_cell[
            'cell_coordinates'][0]:
            function_2()
        elif belief_set['agent'][1]['coordinates'][0] > delivery_cell[
            'cell_coordinates'][0]:
            function_1()
        elif belief_set['agent'][1]['coordinates'][1] < delivery_cell[
            'cell_coordinates'][1]:
            function_4()
        elif belief_set['agent'][1]['coordinates'][1] > delivery_cell[
            'cell_coordinates'][1]:
            function_3()
    function_6()
