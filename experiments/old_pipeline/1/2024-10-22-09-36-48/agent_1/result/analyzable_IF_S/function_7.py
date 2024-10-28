def function_7():
    global belief_set
    agent = belief_set['agent'][1]
    parcels = belief_set['parcels']
    map_grid = belief_set['map']['grid']
    spawn_points = [cell for cell in map_grid if cell['cell_type'] ==
        'parcels_spawn']
    nearest_spawn_point = min(spawn_points, key=lambda cell: abs(cell[
        'cell_coordinates'][0] - agent['coordinates'][0]) + abs(cell[
        'cell_coordinates'][1] - agent['coordinates'][1]))
    while agent['coordinates'] != nearest_spawn_point['cell_coordinates']:
        if agent['coordinates'][0] < nearest_spawn_point['cell_coordinates'][0
            ]:
            function_2()
        elif agent['coordinates'][0] > nearest_spawn_point['cell_coordinates'][
            0]:
            function_1()
        if agent['coordinates'][1] < nearest_spawn_point['cell_coordinates'][1
            ]:
            function_4()
        elif agent['coordinates'][1] > nearest_spawn_point['cell_coordinates'][
            1]:
            function_3()
    for parcel in parcels.values():
        if parcel['coordinates'] == agent['coordinates'] and parcel[
            'carried_by_id'] is None:
            function_5()
