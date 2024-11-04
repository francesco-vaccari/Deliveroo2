def function_20():
    global belief_set
    agent = belief_set['agent'][1]
    battery_spawn = next(cell for cell in belief_set['map']['grid'] if cell
        ['cell_type'] == 'batteries_spawn')
    while agent['coordinates'] != battery_spawn['cell_coordinates']:
        if agent['coordinates'][0] < battery_spawn['cell_coordinates'][0]:
            function_2()
        elif agent['coordinates'][0] > battery_spawn['cell_coordinates'][0]:
            function_1()
        elif agent['coordinates'][1] < battery_spawn['cell_coordinates'][1]:
            function_4()
        elif agent['coordinates'][1] > battery_spawn['cell_coordinates'][1]:
            function_3()
    function_5()
