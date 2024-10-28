def function_10():
    global belief_set
    closest_parcel = min(belief_set['parcels'].items(), key=lambda x: abs(x
        [1]['coordinates'][0] - belief_set['agent']['coordinates'][0]) +
        abs(x[1]['coordinates'][1] - belief_set['agent']['coordinates'][1]))
    while belief_set['agent']['coordinates'] != closest_parcel[1]['coordinates'
        ]:
        if belief_set['agent']['coordinates'][0] < closest_parcel[1][
            'coordinates'][0]:
            function_2()
        elif belief_set['agent']['coordinates'][0] > closest_parcel[1][
            'coordinates'][0]:
            function_1()
        if belief_set['agent']['coordinates'][1] < closest_parcel[1][
            'coordinates'][1]:
            function_4()
        elif belief_set['agent']['coordinates'][1] > closest_parcel[1][
            'coordinates'][1]:
            function_3()
    function_5()
    closest_delivery_cell = min(filter(lambda x: x['cell_type'] in [
        'delivery_cell', 'double_delivery_cell'], belief_set['map']['grid']
        ), key=lambda x: abs(x['cell_coordinates'][0] - belief_set['agent']
        ['coordinates'][0]) + abs(x['cell_coordinates'][1] - belief_set[
        'agent']['coordinates'][1]))
    while belief_set['agent']['coordinates'] != closest_delivery_cell[
        'cell_coordinates']:
        if belief_set['agent']['coordinates'][0] < closest_delivery_cell[
            'cell_coordinates'][0]:
            function_2()
        elif belief_set['agent']['coordinates'][0] > closest_delivery_cell[
            'cell_coordinates'][0]:
            function_1()
        if belief_set['agent']['coordinates'][1] < closest_delivery_cell[
            'cell_coordinates'][1]:
            function_4()
        elif belief_set['agent']['coordinates'][1] > closest_delivery_cell[
            'cell_coordinates'][1]:
            function_3()
    function_6()
