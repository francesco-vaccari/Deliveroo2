def function_10():
    global belief_set
    agent = belief_set['agent'][1]
    map_grid = belief_set['map']['grid']
    delivery_cell = next(cell for cell in map_grid if cell['cell_type'] ==
        'delivery_cell')
    battery_spawn = next(cell for cell in map_grid if cell['cell_type'] ==
        'batteries_spawn')
    if agent['energy'] < 30:
        if agent['coordinates'][0] < battery_spawn['cell_coordinates'][0]:
            function_2()
        elif agent['coordinates'][0] > battery_spawn['cell_coordinates'][0]:
            function_1()
        elif agent['coordinates'][1] < battery_spawn['cell_coordinates'][1]:
            function_4()
        else:
            function_3()
    else:
        if agent['coordinates'][0] < delivery_cell['cell_coordinates'][0]:
            function_2()
        elif agent['coordinates'][0] > delivery_cell['cell_coordinates'][0]:
            function_1()
        elif agent['coordinates'][1] < delivery_cell['cell_coordinates'][1]:
            function_4()
        else:
            function_3()
        if agent['coordinates'] == delivery_cell['cell_coordinates']:
            function_6()
