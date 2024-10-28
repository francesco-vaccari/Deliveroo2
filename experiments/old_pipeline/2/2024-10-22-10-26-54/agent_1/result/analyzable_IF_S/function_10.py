def function_10():
    global belief_set
    keys = belief_set['keys']
    parcels = belief_set['parcels']
    agent = belief_set['agent']
    map_grid = belief_set['map']['grid']
    walkable_cells = [cell for cell in map_grid if cell['cell_type'] ==
        'walkable']
    key_cells = [cell for cell in walkable_cells if cell['cell_coordinates'
        ] in [keys[key]['coordinates'] for key in keys]]
    parcel_cells = [cell for cell in walkable_cells if cell[
        'cell_coordinates'] in [parcels[parcel]['coordinates'] for parcel in
        parcels]]
    if key_cells and not agent['has_key']:
        target_key_cell = min(key_cells, key=lambda cell: abs(cell[
            'cell_coordinates'][0] - agent['coordinates'][0]) + abs(cell[
            'cell_coordinates'][1] - agent['coordinates'][1]))
        while agent['coordinates'] != target_key_cell['cell_coordinates']:
            if agent['coordinates'][1] < target_key_cell['cell_coordinates'][1
                ]:
                function_4()
            elif agent['coordinates'][1] > target_key_cell['cell_coordinates'][
                1]:
                function_3()
            elif agent['coordinates'][0] < target_key_cell['cell_coordinates'][
                0]:
                function_2()
            elif agent['coordinates'][0] > target_key_cell['cell_coordinates'][
                0]:
                function_1()
        function_5()
    if parcel_cells and agent['parcels_carried_ids']:
        target_parcel_cell = min(parcel_cells, key=lambda cell: abs(cell[
            'cell_coordinates'][0] - agent['coordinates'][0]) + abs(cell[
            'cell_coordinates'][1] - agent['coordinates'][1]))
        while agent['coordinates'] != target_parcel_cell['cell_coordinates']:
            if agent['coordinates'][1] < target_parcel_cell['cell_coordinates'
                ][1]:
                function_4()
            elif agent['coordinates'][1] > target_parcel_cell[
                'cell_coordinates'][1]:
                function_3()
            elif agent['coordinates'][0] < target_parcel_cell[
                'cell_coordinates'][0]:
                function_2()
            elif agent['coordinates'][0] > target_parcel_cell[
                'cell_coordinates'][0]:
                function_1()
        function_5()
