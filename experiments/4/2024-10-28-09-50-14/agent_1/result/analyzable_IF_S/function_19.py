def function_19():
    global belief_set
    if belief_set['agents'][1]['parcels_carried_ids']:
        function_6()
        for cell in belief_set['map']['grid']:
            if cell['cell_type'] == 'delivery_cell' or cell['cell_type'
                ] == 'double_points_delivery_cell':
                while belief_set['agents'][1]['coordinates'] != cell[
                    'cell_coordinates']:
                    if belief_set['agents'][1]['coordinates'][0] > cell[
                        'cell_coordinates'][0]:
                        function_1()
                    elif belief_set['agents'][1]['coordinates'][0] < cell[
                        'cell_coordinates'][0]:
                        function_2()
                    elif belief_set['agents'][1]['coordinates'][1] > cell[
                        'cell_coordinates'][1]:
                        function_3()
                    else:
                        function_4()
    else:
        function_9()
