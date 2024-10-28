def function_26():
    global belief_set
    if not belief_set['agent']['parcels_carried_ids']:
        function_23()
    else:
        coordinates = belief_set['agent']['coordinates']
        delivery_cells = [cell['cell_coordinates'] for cell in belief_set[
            'map']['grid'] if cell['cell_type'] in ['delivery_cell',
            'double_points_delivery_cell']]
        delivery_cells.sort(key=lambda x: abs(coordinates[0] - x[0]) + abs(
            coordinates[1] - x[1]))
        target_cell = delivery_cells[0]
        while coordinates != target_cell:
            if coordinates[0] < target_cell[0]:
                function_2()
            elif coordinates[0] > target_cell[0]:
                function_1()
            elif coordinates[1] < target_cell[1]:
                function_4()
            elif coordinates[1] > target_cell[1]:
                function_3()
            coordinates = belief_set['agent']['coordinates']
        function_6()
