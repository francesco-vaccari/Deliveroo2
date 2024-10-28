def function_12():
    global belief_set
    if len(belief_set['agent'][1]['parcels_carried_ids']) > 0:
        for cell in belief_set['map']['map']['grid']:
            if cell['cell_type'] == 'delivery_cell' and cell['cell_coordinates'
                ] == belief_set['agent'][1]['coordinates']:
                function_6()
                break
        else:
            for cell in belief_set['map']['map']['grid']:
                if cell['cell_type'] == 'delivery_cell':
                    if cell['cell_coordinates'][0] < belief_set['agent'][1][
                        'coordinates'][0]:
                        function_1()
                    elif cell['cell_coordinates'][0] > belief_set['agent'][1][
                        'coordinates'][0]:
                        function_2()
                    elif cell['cell_coordinates'][1] < belief_set['agent'][1][
                        'coordinates'][1]:
                        function_3()
                    elif cell['cell_coordinates'][1] > belief_set['agent'][1][
                        'coordinates'][1]:
                        function_4()
                    break
