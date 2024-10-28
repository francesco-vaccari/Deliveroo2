def function_14():
    global belief_set
    spawn_points = [cell['cell_coordinates'] for cell in belief_set['map'][
        'grid'] if cell['cell_type'] == 'parcels_spawn']
    if not spawn_points:
        return
    nearest_spawn_point = min(spawn_points, key=lambda x: abs(x[0] -
        belief_set['agent']['coordinates'][0]) + abs(x[1] - belief_set[
        'agent']['coordinates'][1]))
    while belief_set['agent']['coordinates'] != nearest_spawn_point:
        if belief_set['agent']['coordinates'][0] < nearest_spawn_point[0]:
            function_2()
        elif belief_set['agent']['coordinates'][0] > nearest_spawn_point[0]:
            function_1()
        elif belief_set['agent']['coordinates'][1] < nearest_spawn_point[1]:
            function_4()
        elif belief_set['agent']['coordinates'][1] > nearest_spawn_point[1]:
            function_3()
    function_5()
