def function_14():
    global belief_set
    battery_spawn_coordinates = next(cell['cell_coordinates'] for cell in
        belief_set['map']['grid'] if cell['cell_type'] == 'batteries_spawn')
    while belief_set['agent'][1]['coordinates'] != battery_spawn_coordinates:
        if belief_set['agent'][1]['coordinates'][0
            ] > battery_spawn_coordinates[0]:
            function_1()
        elif belief_set['agent'][1]['coordinates'][0
            ] < battery_spawn_coordinates[0]:
            function_2()
        elif belief_set['agent'][1]['coordinates'][1
            ] > battery_spawn_coordinates[1]:
            function_3()
        elif belief_set['agent'][1]['coordinates'][1
            ] < battery_spawn_coordinates[1]:
            function_4()
    function_5()
