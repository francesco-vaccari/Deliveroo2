def function_13():
    global belief_set
    agent = belief_set['agent'][1]
    map_grid = belief_set['map']['grid']
    delivery_cell_coordinates = next(cell['cell_coordinates'] for cell in
        map_grid if cell['cell_type'] == 'delivery_cell')
    while agent['coordinates'] != delivery_cell_coordinates:
        if agent['coordinates'][0] < delivery_cell_coordinates[0]:
            function_2()
        elif agent['coordinates'][0] > delivery_cell_coordinates[0]:
            function_1()
        if agent['coordinates'][1] < delivery_cell_coordinates[1]:
            function_4()
        elif agent['coordinates'][1] > delivery_cell_coordinates[1]:
            function_3()
    function_6()
