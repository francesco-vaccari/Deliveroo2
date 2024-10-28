def function_10():
    global belief_set
    agent = belief_set['agent'][1]
    parcels = belief_set['parcel']
    map_grid = belief_set['map']['map']['grid']
    delivery_cell = next(cell for cell in map_grid if cell['cell_type'] ==
        'delivery_cell')['cell_coordinates']
    while agent['coordinates'] != delivery_cell:
        if agent['coordinates'][0] < delivery_cell[0]:
            function_2()
        elif agent['coordinates'][0] > delivery_cell[0]:
            function_1()
        if agent['coordinates'][1] < delivery_cell[1]:
            function_4()
        elif agent['coordinates'][1] > delivery_cell[1]:
            function_3()
    function_6()
