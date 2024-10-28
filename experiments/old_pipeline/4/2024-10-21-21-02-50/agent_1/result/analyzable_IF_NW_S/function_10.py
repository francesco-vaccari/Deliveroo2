def function_10():
    global belief_set
    agent = belief_set['agents'][1]
    delivery_cells = [cell for cell in belief_set['map']['grid'] if 
        'delivery' in cell['cell_type']]
    closest_delivery_cell = min(delivery_cells, key=lambda cell: abs(cell[
        'cell_coordinates'][0] - agent['coordinates'][0]) + abs(cell[
        'cell_coordinates'][1] - agent['coordinates'][1]))
    while agent['coordinates'] != closest_delivery_cell['cell_coordinates']:
        if agent['coordinates'][0] < closest_delivery_cell['cell_coordinates'][
            0]:
            function_2()
        elif agent['coordinates'][0] > closest_delivery_cell['cell_coordinates'
            ][0]:
            function_1()
        if agent['coordinates'][1] < closest_delivery_cell['cell_coordinates'][
            1]:
            function_4()
        elif agent['coordinates'][1] > closest_delivery_cell['cell_coordinates'
            ][1]:
            function_3()
    function_6()
