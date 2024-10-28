def function_21():
    global belief_set
    if len(belief_set['agents'][1]['parcels_carried_ids']) == 0:
        function_9()
    else:
        parcel_coord = belief_set['parcels'][belief_set['agents'][1][
            'parcels_carried_ids'][0]]['coordinates']
        delivery_cells = [cell for cell in belief_set['map']['grid'] if 
            cell['cell_type'] in ['delivery_cell',
            'double_points_delivery_cell']]
        delivery_cells.sort(key=lambda cell: abs(cell['cell_coordinates'][0
            ] - parcel_coord[0]) + abs(cell['cell_coordinates'][1] -
            parcel_coord[1]))
        target_delivery_cell = delivery_cells[0]
        while belief_set['agents'][1]['coordinates'] != target_delivery_cell[
            'cell_coordinates']:
            if belief_set['agents'][1]['coordinates'][0
                ] > target_delivery_cell['cell_coordinates'][0]:
                function_1()
            elif belief_set['agents'][1]['coordinates'][0
                ] < target_delivery_cell['cell_coordinates'][0]:
                function_2()
            elif belief_set['agents'][1]['coordinates'][1
                ] > target_delivery_cell['cell_coordinates'][1]:
                function_3()
            elif belief_set['agents'][1]['coordinates'][1
                ] < target_delivery_cell['cell_coordinates'][1]:
                function_4()
            if belief_set['agents'][1]['coordinates'] in [door[
                'coordinates'] for door in belief_set['doors'].values()
                ] and belief_set['agents'][1]['has_key']:
                function_18()
        function_6()
