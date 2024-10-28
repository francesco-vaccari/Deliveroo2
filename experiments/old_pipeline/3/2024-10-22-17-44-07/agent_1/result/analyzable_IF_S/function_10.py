def function_10():
    global belief_set
    while belief_set['agent']['coordinates'] != belief_set['parcels'][1][
        'coordinates']:
        if belief_set['agent']['coordinates'][0] > belief_set['parcels'][1][
            'coordinates'][0]:
            function_1()
        elif belief_set['agent']['coordinates'][0] < belief_set['parcels'][1][
            'coordinates'][0]:
            function_2()
        elif belief_set['agent']['coordinates'][1] > belief_set['parcels'][1][
            'coordinates'][1]:
            function_3()
        elif belief_set['agent']['coordinates'][1] < belief_set['parcels'][1][
            'coordinates'][1]:
            function_4()
    function_5()
    for cell in belief_set['map']['grid']:
        if cell['cell_type'] in ['double_delivery_cell', 'delivery_cell']:
            while belief_set['agent']['coordinates'] != cell['cell_coordinates'
                ]:
                if belief_set['agent']['coordinates'][0] > cell[
                    'cell_coordinates'][0]:
                    function_1()
                elif belief_set['agent']['coordinates'][0] < cell[
                    'cell_coordinates'][0]:
                    function_2()
                elif belief_set['agent']['coordinates'][1] > cell[
                    'cell_coordinates'][1]:
                    function_3()
                elif belief_set['agent']['coordinates'][1] < cell[
                    'cell_coordinates'][1]:
                    function_4()
    function_6()
