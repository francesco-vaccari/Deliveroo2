def function_11():
    global belief_set
    delivery_cells = [cell for cell in belief_set['map']['grid'] if 
        'delivery' in cell['cell_type']]
    closest_delivery_cell = min(delivery_cells, key=lambda cell: abs(cell[
        'cell_coordinates'][0] - belief_set['agent']['coordinates'][0]) +
        abs(cell['cell_coordinates'][1] - belief_set['agent']['coordinates'
        ][1]))
    while belief_set['agent']['coordinates'] != closest_delivery_cell[
        'cell_coordinates']:
        if belief_set['agent']['coordinates'][0] < closest_delivery_cell[
            'cell_coordinates'][0]:
            function_2()
        elif belief_set['agent']['coordinates'][0] > closest_delivery_cell[
            'cell_coordinates'][0]:
            function_1()
        elif belief_set['agent']['coordinates'][1] < closest_delivery_cell[
            'cell_coordinates'][1]:
            function_4()
        else:
            function_3()
    function_6()
