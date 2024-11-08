def function_8():
    global belief_set
    agent_coordinates = belief_set['agent'][1]['coordinates']
    if belief_set['agent'][1]['parcels_carried_ids']:
        if 'delivery' in [cell['cell_type'] for cell in belief_set['map'][
            'grid'] if cell['cell_coordinates'] == agent_coordinates]:
            function_6()
        else:
            if agent_coordinates[0] > 0:
                function_1()
            elif agent_coordinates[0] < belief_set['map']['width'] - 1:
                function_2()
            if agent_coordinates[1] > 0:
                function_3()
            elif agent_coordinates[1] < belief_set['map']['height'] - 1:
                function_4()
    else:
        function_7()

def function_9():
    global belief_set
    agent = belief_set['agent'][1]
    parcels = belief_set['parcels']
    carried_parcels = [parcels[parcel_id] for parcel_id in agent[
        'parcels_carried_ids']]
    if not carried_parcels:
        return
    current_coordinates = agent['coordinates']
    target_coordinates = find_closest_walkable_cell(current_coordinates,
        belief_set['map']['grid'])
    while current_coordinates != target_coordinates:
        if current_coordinates[0] < target_coordinates[0]:
            function_2()
        elif current_coordinates[0] > target_coordinates[0]:
            function_1()
        if current_coordinates[1] < target_coordinates[1]:
            function_4()
        elif current_coordinates[1] > target_coordinates[1]:
            function_3()
        current_coordinates = agent['coordinates']
    function_6()

def function_10():
    global belief_set
    agent = belief_set['agent'][1]
    map = belief_set['map']['grid']
    walkable_cells = [cell for cell in map if cell['cell_type'] == 'walkable']
    current_coordinates = agent['coordinates']
    nearest_walkable_cell = min(walkable_cells, key=lambda cell: abs(cell[
        'cell_coordinates'][0] - current_coordinates[0]) + abs(cell[
        'cell_coordinates'][1] - current_coordinates[1]))
    target_coordinates = nearest_walkable_cell['cell_coordinates']
    while agent['coordinates'] != target_coordinates:
        if agent['coordinates'][0] < target_coordinates[0]:
            function_2()
            agent['coordinates'][0] += 1
        elif agent['coordinates'][0] > target_coordinates[0]:
            function_1()
            agent['coordinates'][0] -= 1
        if agent['coordinates'][1] < target_coordinates[1]:
            function_4()
            agent['coordinates'][1] += 1
        elif agent['coordinates'][1] > target_coordinates[1]:
            function_3()
            agent['coordinates'][1] -= 1
    function_6()

def function_11():
    global belief_set
    min_distance = float('inf')
    nearest_parcel = None
    for parcel in belief_set['parcels'].values():
        distance = abs(parcel['coordinates'][0] - belief_set['agent'][1][
            'coordinates'][0]) + abs(parcel['coordinates'][1] - belief_set[
            'agent'][1]['coordinates'][1])
        if distance < min_distance:
            min_distance = distance
            nearest_parcel = parcel
    while belief_set['agent'][1]['coordinates'] != nearest_parcel['coordinates'
        ]:
        if belief_set['agent'][1]['coordinates'][0] < nearest_parcel[
            'coordinates'][0]:
            function_2()
        elif belief_set['agent'][1]['coordinates'][0] > nearest_parcel[
            'coordinates'][0]:
            function_1()
        elif belief_set['agent'][1]['coordinates'][1] < nearest_parcel[
            'coordinates'][1]:
            function_4()
        elif belief_set['agent'][1]['coordinates'][1] > nearest_parcel[
            'coordinates'][1]:
            function_3()
    function_5()
    for cell in belief_set['map']['grid']:
        if cell['cell_type'] == 'delivery_cell':
            delivery_cell = cell
    while belief_set['agent'][1]['coordinates'] != delivery_cell[
        'cell_coordinates']:
        if belief_set['agent'][1]['coordinates'][0] < delivery_cell[
            'cell_coordinates'][0]:
            function_2()
        elif belief_set['agent'][1]['coordinates'][0] > delivery_cell[
            'cell_coordinates'][0]:
            function_1()
        elif belief_set['agent'][1]['coordinates'][1] < delivery_cell[
            'cell_coordinates'][1]:
            function_4()
        elif belief_set['agent'][1]['coordinates'][1] > delivery_cell[
            'cell_coordinates'][1]:
            function_3()
    function_6()

def function_12():
    global belief_set
    agent = belief_set['agent'][1]
    battery = belief_set['batteries'][1]
    while agent['coordinates'] != battery['coordinates']:
        if agent['coordinates'][0] < battery['coordinates'][0]:
            function_2()
        elif agent['coordinates'][0] > battery['coordinates'][0]:
            function_1()
        if agent['coordinates'][1] < battery['coordinates'][1]:
            function_4()
        elif agent['coordinates'][1] > battery['coordinates'][1]:
            function_3()
    function_5()

def function_13():
    global belief_set
    agent = belief_set['agent'][1]
    battery = belief_set['batteries'][1]
    x_distance = battery['coordinates'][0] - agent['coordinates'][0]
    y_distance = battery['coordinates'][1] - agent['coordinates'][1]
    iterations = 0
    max_iterations = 10
    while agent['coordinates'] != battery['coordinates'
        ] and iterations < max_iterations:
        if x_distance > 0:
            function_2()
            x_distance -= 1
        elif x_distance < 0:
            function_1()
            x_distance += 1
        if y_distance > 0:
            function_4()
            y_distance -= 1
        elif y_distance < 0:
            function_3()
            y_distance += 1
        iterations += 1
    function_5()

def function_14():
    global belief_set
    agent = belief_set['agent'][1]
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

def function_15():
    global belief_set
    agent = belief_set['agent'][1]
    keys = belief_set['keys']
    for key_id, key in keys.items():
        if key['carried_by_id'] is None:
            while agent['coordinates'] != key['coordinates']:
                if agent['coordinates'][0] > key['coordinates'][0] and agent[
                    'coordinates'][0] > 0:
                    function_1()
                elif agent['coordinates'][0] < key['coordinates'][0] and agent[
                    'coordinates'][0] < belief_set['map']['width'] - 1:
                    function_2()
                elif agent['coordinates'][1] > key['coordinates'][1] and agent[
                    'coordinates'][1] > 0:
                    function_3()
                elif agent['coordinates'][1] < key['coordinates'][1] and agent[
                    'coordinates'][1] < belief_set['map']['height'] - 1:
                    function_4()
                else:
                    break
            function_5()
            break

def function_16():
    global belief_set
    agent = belief_set['agent'][1]
    key = belief_set['keys'][1]
    while agent['coordinates'] != key['coordinates']:
        if agent['coordinates'][0] < key['coordinates'][0] and agent[
            'coordinates'][0] < belief_set['map']['width'] - 1:
            function_2()
            agent['coordinates'][0] += 1
        elif agent['coordinates'][0] > key['coordinates'][0] and agent[
            'coordinates'][0] > 0:
            function_1()
            agent['coordinates'][0] -= 1
        if agent['coordinates'][1] < key['coordinates'][1] and agent[
            'coordinates'][1] < belief_set['map']['height'] - 1:
            function_4()
            agent['coordinates'][1] += 1
        elif agent['coordinates'][1] > key['coordinates'][1] and agent[
            'coordinates'][1] > 0:
            function_3()
            agent['coordinates'][1] -= 1
    function_5()

def function_17():
    global belief_set
    agent = belief_set['agent'][1]
    door = belief_set['doors'][1]
    if agent['coordinates'][0] < door['coordinates'][0]:
        function_2()
    elif agent['coordinates'][0] > door['coordinates'][0]:
        function_1()
    elif agent['coordinates'][1] < door['coordinates'][1]:
        function_4()
    elif agent['coordinates'][1] > door['coordinates'][1]:
        function_3()
    elif agent['has_key']:
        function_5()

def function_18():
    global belief_set
    agent = belief_set['agent'][1]
    door = belief_set['doors'][1]
    while agent['coordinates'] != door['coordinates']:
        if agent['coordinates'][0] < door['coordinates'][0]:
            function_2()
        elif agent['coordinates'][0] > door['coordinates'][0]:
            function_1()
        elif agent['coordinates'][1] < door['coordinates'][1]:
            function_4()
        else:
            function_3()
    door['is_locked'] = False
    return

def function_19():
    global belief_set
    agent = belief_set['agent'][1]
    door = belief_set['doors'][1]
    agent_coordinates = agent['coordinates']
    door_coordinates = door['coordinates']
    while agent_coordinates != door_coordinates:
        if agent_coordinates[0] < door_coordinates[0]:
            function_2()
            agent_coordinates[0] += 1
        elif agent_coordinates[0] > door_coordinates[0]:
            function_1()
            agent_coordinates[0] -= 1
        if agent_coordinates[1] < door_coordinates[1]:
            function_4()
            agent_coordinates[1] += 1
        elif agent_coordinates[1] > door_coordinates[1]:
            function_3()
            agent_coordinates[1] -= 1

def function_20():
    global belief_set
    agent = belief_set['agent'][1]
    delivery_cell = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'delivery_cell'][0]['cell_coordinates']
    if agent['coordinates'] == delivery_cell and len(agent[
        'parcels_carried_ids']) > 0:
        function_6()
    elif agent['coordinates'][0] < delivery_cell[0]:
        function_2()
    elif agent['coordinates'][0] > delivery_cell[0]:
        function_1()
    elif agent['coordinates'][1] < delivery_cell[1]:
        function_4()
    elif agent['coordinates'][1] > delivery_cell[1]:
        function_3()
    elif agent['energy'] < 30:
        battery_cell = [cell for cell in belief_set['map']['grid'] if cell[
            'cell_type'] == 'batteries_spawn'][0]['cell_coordinates']
        if agent['coordinates'] == battery_cell:
            function_5()
        elif agent['coordinates'][0] < battery_cell[0]:
            function_2()
        elif agent['coordinates'][0] > battery_cell[0]:
            function_1()
        elif agent['coordinates'][1] < battery_cell[1]:
            function_4()
        elif agent['coordinates'][1] > battery_cell[1]:
            function_3()
    else:
        function_7()

def function_21():
    global belief_set
    delivery_cell = next(cell for cell in belief_set['map']['grid'] if cell
        ['cell_type'] == 'delivery_cell')
    agent = belief_set['agent'][1]
    dx, dy = delivery_cell['cell_coordinates'][0] - agent['coordinates'][0
        ], delivery_cell['cell_coordinates'][1] - agent['coordinates'][1]
    if dx < 0:
        function_1()
    elif dx > 0:
        function_2()
    elif dy < 0:
        function_3()
    elif dy > 0:
        function_4()
    function_6()

def function_22():
    global belief_set
    agent = belief_set['agent'][1]
    if agent['energy'] < 30:
        for cell in belief_set['map']['grid']:
            if cell['cell_type'] == 'batteries_spawn':
                agent['coordinates'] = cell['cell_coordinates']
                break
    else:
        parcel_picked = False
        for parcel in belief_set['parcels'].values():
            if parcel['coordinates'] == agent['coordinates']:
                function_5()
                parcel_picked = True
                break
        if not parcel_picked:
            function_7()
        for cell in belief_set['map']['grid']:
            if cell['cell_type'] == 'delivery_cell':
                while agent['coordinates'] != cell['cell_coordinates']:
                    if agent['coordinates'][0] < cell['cell_coordinates'][0]:
                        function_2()
                    elif agent['coordinates'][0] > cell['cell_coordinates'][0]:
                        function_1()
                    elif agent['coordinates'][1] < cell['cell_coordinates'][1]:
                        function_4()
                    elif agent['coordinates'][1] > cell['cell_coordinates'][1]:
                        function_3()
                function_6()
                break

def function_23():
    global belief_set
    delivery_cell = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'delivery_cell'][0]['cell_coordinates']
    agent_position = belief_set['agent'][1]['coordinates']
    while agent_position != delivery_cell:
        if agent_position[0] > delivery_cell[0]:
            function_1()
            agent_position[0] -= 1
        elif agent_position[0] < delivery_cell[0]:
            function_2()
            agent_position[0] += 1
        elif agent_position[1] > delivery_cell[1]:
            function_3()
            agent_position[1] -= 1
        elif agent_position[1] < delivery_cell[1]:
            function_4()
            agent_position[1] += 1
    function_6()

def function_24():
    global belief_set
    agent = belief_set['agent'][1]
    parcels = belief_set['parcels']
    nearest_parcel = min(parcels.values(), key=lambda p: abs(p[
        'coordinates'][0] - agent['coordinates'][0]) + abs(p['coordinates']
        [1] - agent['coordinates'][1]))
    while agent['coordinates'] != nearest_parcel['coordinates']:
        if agent['coordinates'][0] < nearest_parcel['coordinates'][0]:
            function_2()
        elif agent['coordinates'][0] > nearest_parcel['coordinates'][0]:
            function_1()
        elif agent['coordinates'][1] < nearest_parcel['coordinates'][1]:
            function_4()
        else:
            function_3()
    function_5()
    delivery_cell = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'delivery_cell'][0]
    while agent['coordinates'] != delivery_cell['cell_coordinates']:
        if agent['coordinates'][0] < delivery_cell['cell_coordinates'][0]:
            function_2()
        elif agent['coordinates'][0] > delivery_cell['cell_coordinates'][0]:
            function_1()
        elif agent['coordinates'][1] < delivery_cell['cell_coordinates'][1]:
            function_4()
        else:
            function_3()
    function_6()

def function_25():
    global belief_set
    agent = belief_set['agent'][1]
    batteries_spawn = [cell['cell_coordinates'] for cell in belief_set[
        'map']['grid'] if cell['cell_type'] == 'batteries_spawn'][0]
    parcels_spawn = [cell['cell_coordinates'] for cell in belief_set['map']
        ['grid'] if cell['cell_type'] == 'parcels_spawn'][0]
    delivery_cell = [cell['cell_coordinates'] for cell in belief_set['map']
        ['grid'] if cell['cell_type'] == 'delivery_cell'][0]
    max_moves = belief_set['map']['width'] * belief_set['map']['height']
    for _ in range(max_moves):
        if agent['coordinates'][0] > batteries_spawn[0]:
            function_1()
        elif agent['coordinates'][0] < batteries_spawn[0]:
            function_2()
        elif agent['coordinates'][1] > batteries_spawn[1]:
            function_3()
        elif agent['coordinates'][1] < batteries_spawn[1]:
            function_4()
        else:
            break
    function_5()
    for _ in range(max_moves):
        if agent['coordinates'][0] > parcels_spawn[0]:
            function_1()
        elif agent['coordinates'][0] < parcels_spawn[0]:
            function_2()
        elif agent['coordinates'][1] > parcels_spawn[1]:
            function_3()
        elif agent['coordinates'][1] < parcels_spawn[1]:
            function_4()
        else:
            break
    function_5()
    for _ in range(max_moves):
        if agent['coordinates'][0] > delivery_cell[0]:
            function_1()
        elif agent['coordinates'][0] < delivery_cell[0]:
            function_2()
        elif agent['coordinates'][1] > delivery_cell[1]:
            function_3()
        elif agent['coordinates'][1] < delivery_cell[1]:
            function_4()
        else:
            break
    function_6()

