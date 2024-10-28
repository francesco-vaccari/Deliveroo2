def function_7():
    global belief_set
    agent = belief_set['agent']
    parcels = belief_set['parcels']
    for parcel in parcels.values():
        if parcel['coordinates'][0] < agent['coordinates'][0]:
            function_1()
        elif parcel['coordinates'][0] > agent['coordinates'][0]:
            function_2()
        elif parcel['coordinates'][1] < agent['coordinates'][1]:
            function_3()
        elif parcel['coordinates'][1] > agent['coordinates'][1]:
            function_4()
    function_5()

def function_8():
    global belief_set
    agent = belief_set['agent']
    parcels = belief_set['parcels']
    for parcel_id, parcel in parcels.items():
        if not parcel['carried_by_id']:
            parcel_coords = parcel['coordinates']
            while agent['coordinates'] != parcel_coords:
                if agent['coordinates'][0] < parcel_coords[0]:
                    function_2()
                elif agent['coordinates'][0] > parcel_coords[0]:
                    function_1()
                elif agent['coordinates'][1] < parcel_coords[1]:
                    function_4()
                elif agent['coordinates'][1] > parcel_coords[1]:
                    function_3()
            function_5()
            break
    delivery_cell_coords = [cell['cell_coordinates'] for cell in belief_set
        ['map']['grid'] if cell['cell_type'] in ['delivery_cell',
        'double_points_delivery_cell']][0]
    while agent['coordinates'] != delivery_cell_coords:
        if agent['coordinates'][0] < delivery_cell_coords[0]:
            function_2()
        elif agent['coordinates'][0] > delivery_cell_coords[0]:
            function_1()
        elif agent['coordinates'][1] < delivery_cell_coords[1]:
            function_4()
        elif agent['coordinates'][1] > delivery_cell_coords[1]:
            function_3()
    function_6()

def function_9():
    global belief_set
    agent = belief_set['agent']
    parcels = belief_set['parcels']
    map = belief_set['map']['grid']
    parcel_coordinates = [parcel['coordinates'] for parcel in parcels.
        values() if parcel['carried_by_id'] is None]
    delivery_coordinates = [cell['cell_coordinates'] for cell in map if 
        cell['cell_type'] in ['delivery_cell', 'double_points_delivery_cell']]
    if not agent['parcels_carried_ids']:
        target_coordinates = parcel_coordinates[0]
    else:
        target_coordinates = delivery_coordinates[0]
    while agent['coordinates'] != target_coordinates:
        if agent['coordinates'][0] > target_coordinates[0]:
            function_1()
        elif agent['coordinates'][0] < target_coordinates[0]:
            function_2()
        elif agent['coordinates'][1] > target_coordinates[1]:
            function_3()
        elif agent['coordinates'][1] < target_coordinates[1]:
            function_4()
    if not agent['parcels_carried_ids']:
        function_5()
    else:
        function_6()

def function_10():
    global belief_set
    agent = belief_set['agent']
    key = belief_set['keys'][1]
    while agent['coordinates'] != key['coordinates']:
        if agent['coordinates'][0] < key['coordinates'][0]:
            function_2()
        elif agent['coordinates'][0] > key['coordinates'][0]:
            function_1()
        elif agent['coordinates'][1] < key['coordinates'][1]:
            function_4()
        elif agent['coordinates'][1] > key['coordinates'][1]:
            function_3()
    function_5()

def function_13():
    global belief_set
    parcels = belief_set['parcels']
    agent = belief_set['agent']
    for parcel in parcels:
        if parcels[parcel]['coordinates'] == agent['coordinates']:
            function_5()
            function_12()
            break
        else:
            if parcels[parcel]['coordinates'][0] > agent['coordinates'][0]:
                function_2()
            elif parcels[parcel]['coordinates'][0] < agent['coordinates'][0]:
                function_1()
            if parcels[parcel]['coordinates'][1] > agent['coordinates'][1]:
                function_4()
            elif parcels[parcel]['coordinates'][1] < agent['coordinates'][1]:
                function_3()

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

def function_15():
    global belief_set
    max_steps = 100
    steps = 0
    while belief_set['agent']['coordinates'] != belief_set['keys'][1][
        'coordinates'] and steps < max_steps:
        if belief_set['agent']['coordinates'][0] > belief_set['keys'][1][
            'coordinates'][0]:
            function_1()
        elif belief_set['agent']['coordinates'][0] < belief_set['keys'][1][
            'coordinates'][0]:
            function_2()
        elif belief_set['agent']['coordinates'][1] > belief_set['keys'][1][
            'coordinates'][1]:
            function_3()
        elif belief_set['agent']['coordinates'][1] < belief_set['keys'][1][
            'coordinates'][1]:
            function_4()
        steps += 1
    function_5()
    steps = 0
    while belief_set['agent']['coordinates'] != belief_set['map']['grid'][0][
        'cell_coordinates'] and steps < max_steps:
        if belief_set['agent']['coordinates'][0] > belief_set['map']['grid'][0
            ]['cell_coordinates'][0]:
            function_1()
        elif belief_set['agent']['coordinates'][0] < belief_set['map']['grid'][
            0]['cell_coordinates'][0]:
            function_2()
        elif belief_set['agent']['coordinates'][1] > belief_set['map']['grid'][
            0]['cell_coordinates'][1]:
            function_3()
        elif belief_set['agent']['coordinates'][1] < belief_set['map']['grid'][
            0]['cell_coordinates'][1]:
            function_4()
        steps += 1
    function_5()
    function_12()

