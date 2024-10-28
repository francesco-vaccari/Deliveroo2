def function_21():
    global belief_set
    parcel_coords = belief_set['agent']['coordinates']
    delivery_cells = [cell['cell_coordinates'] for cell in belief_set['map'
        ]['grid'] if 'delivery' in cell['cell_type']]
    nearest_delivery_cell = min(delivery_cells, key=lambda x: abs(x[0] -
        parcel_coords[0]) + abs(x[1] - parcel_coords[1]))
    while belief_set['agent']['coordinates'] != nearest_delivery_cell:
        if nearest_delivery_cell[0] < belief_set['agent']['coordinates'][0]:
            function_1()
        elif nearest_delivery_cell[0] > belief_set['agent']['coordinates'][0]:
            function_2()
        elif nearest_delivery_cell[1] < belief_set['agent']['coordinates'][1]:
            function_3()
        else:
            function_4()
    function_6()
