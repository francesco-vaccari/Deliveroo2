def function_7():
    global belief_set
    agent_coords = belief_set['agent'][1]['coordinates']
    parcel_coords = belief_set['parcels'][1]['coordinates']
    while agent_coords[0] < parcel_coords[0]:
        function_2()
        agent_coords[0] += 1
    while agent_coords[1] < parcel_coords[1]:
        function_4()
        agent_coords[1] += 1
    function_5()
    while agent_coords[0] > 0:
        function_1()
        agent_coords[0] -= 1
    while agent_coords[1] > 0:
        function_3()
        agent_coords[1] -= 1
    function_6()

def function_8():
    global belief_set
    agent = belief_set['agent'][1]
    parcels = belief_set['parcels']
    map = belief_set['map']['grid']
    delivery_point = [cell for cell in map if cell['cell_type'] ==
        'parcels_spawn'][0]['cell_coordinates']
    for parcel_id, parcel in parcels.items():
        if parcel['carried_by_id'] is None:
            if agent['coordinates'] == parcel['coordinates']:
                function_5()
            elif agent['coordinates'][0] < parcel['coordinates'][0]:
                function_2()
            elif agent['coordinates'][0] > parcel['coordinates'][0]:
                function_1()
            elif agent['coordinates'][1] < parcel['coordinates'][1]:
                function_4()
            else:
                function_3()
        elif parcel['carried_by_id'] == agent['id']:
            if agent['coordinates'] == delivery_point:
                function_6()
            elif agent['coordinates'][0] < delivery_point[0]:
                function_2()
            elif agent['coordinates'][0] > delivery_point[0]:
                function_1()
            elif agent['coordinates'][1] < delivery_point[1]:
                function_4()
            else:
                function_3()

def function_9():
    global belief_set
    parcel_spawn_location = None
    for cell in belief_set['map']['grid']:
        if cell['cell_type'] == 'parcels_spawn':
            parcel_spawn_location = cell['cell_coordinates']
            break
    if parcel_spawn_location is not None:
        agent_location = belief_set['agent'][1]['coordinates']
        if agent_location[0] < parcel_spawn_location[0]:
            function_2()
        elif agent_location[0] > parcel_spawn_location[0]:
            function_1()
        elif agent_location[1] < parcel_spawn_location[1]:
            function_4()
        elif agent_location[1] > parcel_spawn_location[1]:
            function_3()
        if belief_set['agent'][1]['energy'] < 20:
            belief_set['agent'][1]['energy'] += 20

def function_10():
    global belief_set
    agent = belief_set['agent'][1]
    delivery_cells = [cell['cell_coordinates'] for cell in belief_set['map'
        ]['grid'] if cell['cell_type'] == 'delivery_cell']
    for cell in delivery_cells:
        if agent['coordinates'][0] > cell[0]:
            function_1()
        elif agent['coordinates'][0] < cell[0]:
            function_2()
        elif agent['coordinates'][1] > cell[1]:
            function_3()
        elif agent['coordinates'][1] < cell[1]:
            function_4()

def function_12():
    global belief_set
    delivery_cells = [cell['cell_coordinates'] for cell in belief_set['map'
        ]['grid'] if cell['cell_type'] == 'delivery_cell']
    agent_position = belief_set['agent'][1]['coordinates']
    agent_energy = belief_set['agent'][1]['energy']
    if agent_energy >= 5:
        for cell in delivery_cells:
            if cell[0] < agent_position[0] and belief_set['map']['grid'][
                agent_position[0] - 1][agent_position[1]]['cell_type'
                ] == 'walkable':
                function_1()
                break
            elif cell[0] > agent_position[0] and belief_set['map']['grid'][
                agent_position[0] + 1][agent_position[1]]['cell_type'
                ] == 'walkable':
                function_2()
                break
            elif cell[1] < agent_position[1] and belief_set['map']['grid'][
                agent_position[0]][agent_position[1] - 1]['cell_type'
                ] == 'walkable':
                function_3()
                break
            elif cell[1] > agent_position[1] and belief_set['map']['grid'][
                agent_position[0]][agent_position[1] + 1]['cell_type'
                ] == 'walkable':
                function_4()
                break

def function_15():
    global belief_set
    agent_coordinates = belief_set['agent'][1]['coordinates']
    battery_spawn_coordinates = [cell['cell_coordinates'] for cell in
        belief_set['map']['grid'] if cell['cell_type'] == 'batteries_spawn'][0]
    x_diff = battery_spawn_coordinates[0] - agent_coordinates[0]
    y_diff = battery_spawn_coordinates[1] - agent_coordinates[1]
    if x_diff > 0:
        function_2()
    elif x_diff < 0:
        function_1()
    elif y_diff > 0:
        function_4()
    elif y_diff < 0:
        function_3()
    if agent_coordinates == battery_spawn_coordinates:
        function_5()

def function_16():
    global belief_set
    agent = belief_set['agent'][1]
    battery_location = belief_set['batteries'][1]['coordinates']
    while agent['coordinates'] != battery_location:
        if agent['coordinates'][0] < battery_location[0]:
            function_2()
            agent['coordinates'][0] += 1
        elif agent['coordinates'][0] > battery_location[0]:
            function_1()
            agent['coordinates'][0] -= 1
        if agent['coordinates'][1] < battery_location[1]:
            function_4()
            agent['coordinates'][1] += 1
        elif agent['coordinates'][1] > battery_location[1]:
            function_3()
            agent['coordinates'][1] -= 1
    function_5()

def function_17():
    global belief_set
    agent_coords = belief_set['agent'][1]['coordinates']
    key_coords = belief_set['keys'][1]['coordinates']
    has_key = belief_set['agent'][1]['has_key']
    if not has_key:
        if agent_coords[0] > key_coords[0]:
            function_1()
        elif agent_coords[0] < key_coords[0]:
            function_2()
        elif agent_coords[1] > key_coords[1]:
            function_3()
        elif agent_coords[1] < key_coords[1]:
            function_4()
        if agent_coords == key_coords:
            function_5()
    else:
        pass

def function_18():
    global belief_set
    agent = belief_set['agent'][1]
    key = belief_set['keys'][1]
    if agent['coordinates'] == key['coordinates']:
        function_5()
    elif agent['coordinates'][0] > key['coordinates'][0]:
        function_1()
    elif agent['coordinates'][0] < key['coordinates'][0]:
        function_2()
    elif agent['coordinates'][1] > key['coordinates'][1]:
        function_3()
    else:
        function_4()

def function_19():
    global belief_set
    key_coordinates = belief_set['keys'][1]['coordinates']
    agent_coordinates = belief_set['agent'][1]['coordinates']
    while agent_coordinates[0] > key_coordinates[0]:
        function_1()
        agent_coordinates = belief_set['agent'][1]['coordinates']
    while agent_coordinates[0] < key_coordinates[0]:
        function_2()
        agent_coordinates = belief_set['agent'][1]['coordinates']
    while agent_coordinates[1] > key_coordinates[1]:
        function_3()
        agent_coordinates = belief_set['agent'][1]['coordinates']
    while agent_coordinates[1] < key_coordinates[1]:
        function_4()
        agent_coordinates = belief_set['agent'][1]['coordinates']
    function_5()
    function_4()

def function_20():
    global belief_set
    agent = belief_set['agent'][1]
    door = belief_set['doors'][1]
    if agent['has_key']:
        if agent['coordinates'][0] < door['coordinates'][0]:
            function_2()
        elif agent['coordinates'][0] > door['coordinates'][0]:
            function_1()
        if agent['coordinates'][1] < door['coordinates'][1]:
            function_4()
        elif agent['coordinates'][1] > door['coordinates'][1]:
            function_3()

def function_21():
    global belief_set
    agent = belief_set['agent'][1]
    if agent['has_key']:
        door_coordinates = belief_set['doors'][1]['coordinates']
        if agent['coordinates'][0] < door_coordinates[0]:
            function_2()
        elif agent['coordinates'][0] > door_coordinates[0]:
            function_1()
        elif agent['coordinates'][1] < door_coordinates[1]:
            function_4()
        else:
            function_3()
    else:
        key_coordinates = belief_set['keys'][1]['coordinates']
        if agent['coordinates'][0] < key_coordinates[0]:
            function_2()
        elif agent['coordinates'][0] > key_coordinates[0]:
            function_1()
        elif agent['coordinates'][1] < key_coordinates[1]:
            function_4()
        else:
            function_3()
        function_5()

def function_22():
    global belief_set
    agent = belief_set['agent'][1]
    if agent['has_key'] and agent['energy'] > 10:
        door = belief_set['doors'][1]
        if agent['coordinates'][0] > door['coordinates'][0]:
            function_1()
        elif agent['coordinates'][0] < door['coordinates'][0]:
            function_2()
        elif agent['coordinates'][1] > door['coordinates'][1]:
            function_3()
        elif agent['coordinates'][1] < door['coordinates'][1]:
            function_4()
    elif agent['energy'] <= 10:
        function_16()

def function_23():
    global belief_set
    agent = belief_set['agent'][1]
    if agent['energy'] < 30:
        function_16()
    else:
        function_14()
    if 'parcels' in belief_set and agent['coordinates'] in [parcel[
        'coordinates'] for parcel in belief_set['parcels'].values()]:
        function_5()
    if 'keys' in belief_set and agent['coordinates'] == belief_set['keys'][2][
        'coordinates']:
        function_5()

def function_24():
    global belief_set
    agent_coords = belief_set['agent'][1]['coordinates']
    parcel_coords = [parcel['coordinates'] for parcel in belief_set[
        'parcels'].values() if parcel['carried_by_id'] is None]
    if agent_coords in parcel_coords:
        function_5()
    else:
        min_distance = float('inf')
        for coords in parcel_coords:
            distance = abs(agent_coords[0] - coords[0]) + abs(agent_coords[
                1] - coords[1])
            if distance < min_distance:
                min_distance = distance
                nearest_parcel = coords
        if agent_coords[0] > nearest_parcel[0]:
            function_1()
        elif agent_coords[0] < nearest_parcel[0]:
            function_2()
        elif agent_coords[1] > nearest_parcel[1]:
            function_3()
        elif agent_coords[1] < nearest_parcel[1]:
            function_4()

def function_25():
    global belief_set
    agent = belief_set['agent'][1]
    parcels = belief_set['parcels']
    min_distance = float('inf')
    nearest_parcel = None
    for parcel_id, parcel in parcels.items():
        if parcel['carried_by_id'] is not None:
            continue
        distance = abs(agent['coordinates'][0] - parcel['coordinates'][0]
            ) + abs(agent['coordinates'][1] - parcel['coordinates'][1])
        if distance < min_distance:
            min_distance = distance
            nearest_parcel = parcel
    if nearest_parcel is not None:
        if agent['coordinates'] == nearest_parcel['coordinates']:
            function_5()
        elif agent['coordinates'][0] > nearest_parcel['coordinates'][0]:
            function_1()
        elif agent['coordinates'][0] < nearest_parcel['coordinates'][0]:
            function_2()
        elif agent['coordinates'][1] > nearest_parcel['coordinates'][1]:
            function_3()
        elif agent['coordinates'][1] < nearest_parcel['coordinates'][1]:
            function_4()

def function_26():
    global belief_set
    agent = belief_set['agent'][1]
    if agent['energy'] < 30:
        function_16()
    else:
        parcels = belief_set['parcels']
        keys = belief_set['keys']
        if parcels or keys:
            function_5()
        else:
            function_11()

def function_27():
    global belief_set
    parcel_location = next((parcel['coordinates'] for parcel in belief_set[
        'parcels'].values() if parcel['carried_by_id'] is None), None)
    if belief_set['agent'][1]['coordinates'] == parcel_location:
        function_5()
    elif belief_set['agent'][1]['coordinates'][0] < parcel_location[0]:
        function_2()
    elif belief_set['agent'][1]['coordinates'][0] > parcel_location[0]:
        function_1()
    elif belief_set['agent'][1]['coordinates'][1] < parcel_location[1]:
        function_4()
    elif belief_set['agent'][1]['coordinates'][1] > parcel_location[1]:
        function_3()
    delivery_cell_location = next((cell['cell_coordinates'] for cell in
        belief_set['map']['grid'] if cell['cell_type'] == 'delivery_cell'),
        None)
    if belief_set['agent'][1]['coordinates'] == delivery_cell_location:
        function_6()
    elif belief_set['agent'][1]['coordinates'][0] < delivery_cell_location[0]:
        function_2()
    elif belief_set['agent'][1]['coordinates'][0] > delivery_cell_location[0]:
        function_1()
    elif belief_set['agent'][1]['coordinates'][1] < delivery_cell_location[1]:
        function_4()
    elif belief_set['agent'][1]['coordinates'][1] > delivery_cell_location[1]:
        function_3()

def function_28():
    global belief_set
    agent = belief_set['agent'][1]
    parcel_coords = [parcel['coordinates'] for parcel in belief_set[
        'parcels'].values() if parcel['carried_by_id'] is None]
    delivery_coords = [cell['cell_coordinates'] for cell in belief_set[
        'map']['grid'] if cell['cell_type'] == 'delivery_cell'][0]
    while agent['coordinates'] != parcel_coords[0]:
        if agent['coordinates'][0] < parcel_coords[0][0]:
            function_2()
        elif agent['coordinates'][0] > parcel_coords[0][0]:
            function_1()
        elif agent['coordinates'][1] < parcel_coords[0][1]:
            function_4()
        elif agent['coordinates'][1] > parcel_coords[0][1]:
            function_3()
    function_5()
    while agent['coordinates'] != delivery_coords:
        if agent['coordinates'][0] < delivery_coords[0]:
            function_2()
        elif agent['coordinates'][0] > delivery_coords[0]:
            function_1()
        elif agent['coordinates'][1] < delivery_coords[1]:
            function_4()
        elif agent['coordinates'][1] > delivery_coords[1]:
            function_3()
    function_6()
    if agent['energy'] < 30:
        function_16()

def function_29():
    global belief_set
    parcels = belief_set['parcels']
    agent = belief_set['agent'][1]
    min_distance = float('inf')
    nearest_parcel_coordinates = None
    for parcel_id, parcel_info in parcels.items():
        if parcel_info['carried_by_id'] is None:
            parcel_coordinates = parcel_info['coordinates']
            distance = abs(agent['coordinates'][0] - parcel_coordinates[0]
                ) + abs(agent['coordinates'][1] - parcel_coordinates[1])
            if distance < min_distance:
                min_distance = distance
                nearest_parcel_coordinates = parcel_coordinates
    if nearest_parcel_coordinates is not None:
        if agent['coordinates'][0] > nearest_parcel_coordinates[0]:
            function_1()
        elif agent['coordinates'][0] < nearest_parcel_coordinates[0]:
            function_2()
        elif agent['coordinates'][1] > nearest_parcel_coordinates[1]:
            function_3()
        elif agent['coordinates'][1] < nearest_parcel_coordinates[1]:
            function_4()
        elif agent['coordinates'] == nearest_parcel_coordinates:
            function_5()
    else:
        function_16()

def function_30():
    global belief_set
    agent = belief_set['agent'][1]
    parcels = belief_set['parcels']
    batteries = belief_set['batteries']
    if agent['energy'] < 30:
        function_16()
    elif len(agent['parcels_carried_ids']) == 0:
        nearest_parcel = min(parcels, key=lambda x: abs(agent['coordinates'
            ][0] - parcels[x]['coordinates'][0]) + abs(agent['coordinates']
            [1] - parcels[x]['coordinates'][1]))
        parcel_coordinates = parcels[nearest_parcel]['coordinates']
        if agent['coordinates'][0] < parcel_coordinates[0]:
            function_2()
        elif agent['coordinates'][0] > parcel_coordinates[0]:
            function_1()
        elif agent['coordinates'][1] < parcel_coordinates[1]:
            function_4()
        elif agent['coordinates'][1] > parcel_coordinates[1]:
            function_3()
        function_5()
    else:
        function_14()
        function_6()

def function_31():
    global belief_set
    if belief_set['agent'][1]['energy'] < 50:
        function_16()
    elif belief_set['agent'][1]['coordinates'] in [i['cell_coordinates'] for
        i in belief_set['map']['grid'] if i['cell_type'] == 'delivery_cell']:
        function_6()
    else:
        function_13()

def function_32():
    global belief_set
    agent = belief_set['agent'][1]
    delivery_cell = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'delivery_cell'][0]
    if agent['coordinates'] == delivery_cell['cell_coordinates']:
        function_6()
    elif agent['energy'] < 20:
        battery = [cell for cell in belief_set['map']['grid'] if cell[
            'cell_type'] == 'batteries_spawn'][0]
        if agent['coordinates'][0] < battery['cell_coordinates'][0]:
            function_2()
        elif agent['coordinates'][0] > battery['cell_coordinates'][0]:
            function_1()
        elif agent['coordinates'][1] < battery['cell_coordinates'][1]:
            function_4()
        else:
            function_3()
    elif agent['coordinates'][0] < delivery_cell['cell_coordinates'][0]:
        function_2()
    elif agent['coordinates'][0] > delivery_cell['cell_coordinates'][0]:
        function_1()
    elif agent['coordinates'][1] < delivery_cell['cell_coordinates'][1]:
        function_4()
    else:
        function_3()

