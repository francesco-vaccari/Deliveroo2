def function_7():
    global belief_set
    agent = belief_set['agent'][1]
    parcel = belief_set['parcel'][1]
    map_grid = belief_set['map']['grid']
    spawn_points = [cell['cell_coordinates'] for cell in map_grid if cell[
        'cell_type'] == 'parcels_spawn']
    delivery_points = [cell['cell_coordinates'] for cell in map_grid if 
        cell['cell_type'] == 'delivery_cell']
    if parcel['carried_by_id'] is None and parcel['coordinates'] == agent[
        'coordinates']:
        function_5()
    elif parcel['carried_by_id'] == agent['id'] and agent['coordinates'
        ] in delivery_points:
        function_6()
    else:
        target = spawn_points[0] if parcel['carried_by_id'
            ] is None else delivery_points[0]
        if agent['coordinates'][0] > target[0]:
            function_1()
        elif agent['coordinates'][0] < target[0]:
            function_2()
        elif agent['coordinates'][1] > target[1]:
            function_3()
        elif agent['coordinates'][1] < target[1]:
            function_4()

