def function_10():
    global belief_set
    agent = belief_set['agent'][1]
    map_grid = belief_set['map']['grid']
    non_walkable_cells = [cell for cell in map_grid if cell['cell_type'] ==
        'non_walkable']
    delivery_cell = [cell for cell in map_grid if cell['cell_type'] ==
        'delivery_cell'][0]
    parcels_spawn_cell = [cell for cell in map_grid if cell['cell_type'] ==
        'parcels_spawn'][0]
    path_to_delivery = a_star_pathfinding(agent['coordinates'],
        delivery_cell['cell_coordinates'], non_walkable_cells)
    if path_to_delivery is not None:
        for step in path_to_delivery:
            if step[0] < agent['coordinates'][0]:
                function_1()
            elif step[0] > agent['coordinates'][0]:
                function_2()
            elif step[1] < agent['coordinates'][1]:
                function_3()
            else:
                function_4()
        function_6()
    path_to_spawn = a_star_pathfinding(agent['coordinates'],
        parcels_spawn_cell['cell_coordinates'], non_walkable_cells)
    if path_to_spawn is not None:
        for step in path_to_spawn:
            if step[0] < agent['coordinates'][0]:
                function_1()
            elif step[0] > agent['coordinates'][0]:
                function_2()
            elif step[1] < agent['coordinates'][1]:
                function_3()
            else:
                function_4()
    function_5()
