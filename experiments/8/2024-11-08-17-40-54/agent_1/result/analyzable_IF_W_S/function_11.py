def function_11():
    global belief_set
    max_actions = 10
    actions_taken = 0
    while actions_taken < max_actions:
        if 'parcels_carried_ids' in belief_set['agent'] and len(belief_set[
            'agent']['parcels_carried_ids']) > 0:
            for cell in belief_set['map']['grid']:
                if cell['cell_type'] == 'delivery_cell' and cell[
                    'cell_coordinates'] == belief_set['agent']['coordinates']:
                    function_6()
                    return
        for cell in belief_set['map']['grid']:
            if cell['cell_type'] == 'delivery_cell' and cell['cell_coordinates'
                ][0] > belief_set['agent']['coordinates'][0] and belief_set[
                'agent']['energy'] > 10:
                function_2()
                actions_taken += 1
            elif cell['cell_type'] == 'delivery_cell' and cell[
                'cell_coordinates'][0] < belief_set['agent']['coordinates'][0
                ] and belief_set['agent']['energy'] > 10:
                function_1()
                actions_taken += 1
            elif cell['cell_type'] == 'delivery_cell' and cell[
                'cell_coordinates'][1] > belief_set['agent']['coordinates'][1
                ] and belief_set['agent']['energy'] > 10:
                function_4()
                actions_taken += 1
            elif cell['cell_type'] == 'delivery_cell' and cell[
                'cell_coordinates'][1] < belief_set['agent']['coordinates'][1
                ] and belief_set['agent']['energy'] > 10:
                function_3()
                actions_taken += 1
        actions_taken += 1
    return
