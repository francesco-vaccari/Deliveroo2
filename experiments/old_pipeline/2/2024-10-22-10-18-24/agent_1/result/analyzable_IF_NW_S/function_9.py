def function_9():
    global belief_set
    for parcel in belief_set['parcel'].values():
        if parcel['coordinates'] == belief_set['agent']['coordinates'
            ] and parcel['carried_by_id'] is None:
            function_5()
            break
    for cell in belief_set['map']['grid']:
        if cell['cell_type'] == 'delivery_cell':
            delivery_cell_coordinates = cell['cell_coordinates']
            while belief_set['agent']['coordinates'
                ] != delivery_cell_coordinates:
                if belief_set['agent']['coordinates'][0
                    ] < delivery_cell_coordinates[0]:
                    function_2()
                elif belief_set['agent']['coordinates'][0
                    ] > delivery_cell_coordinates[0]:
                    function_1()
                elif belief_set['agent']['coordinates'][1
                    ] < delivery_cell_coordinates[1]:
                    function_4()
                elif belief_set['agent']['coordinates'][1
                    ] > delivery_cell_coordinates[1]:
                    function_3()
    function_6()
