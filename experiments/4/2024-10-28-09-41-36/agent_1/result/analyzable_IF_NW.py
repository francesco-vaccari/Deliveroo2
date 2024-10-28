def function_7():
    global belief_set
    agent_pos = belief_set['agent']['coordinates']
    parcel_pos = belief_set['parcels'][1]['coordinates']
    if agent_pos[0] < parcel_pos[0]:
        function_2()
    elif agent_pos[0] > parcel_pos[0]:
        function_1()
    elif agent_pos[1] < parcel_pos[1]:
        function_4()
    elif agent_pos[1] > parcel_pos[1]:
        function_3()
    else:
        function_5()

def function_8():
    global belief_set
    parcel_coordinates = belief_set['parcels'][1]['coordinates']
    agent_coordinates = belief_set['agent']['coordinates']
    if agent_coordinates[0] > parcel_coordinates[0]:
        function_1()
    elif agent_coordinates[0] < parcel_coordinates[0]:
        function_2()
    elif agent_coordinates[1] > parcel_coordinates[1]:
        function_3()
    elif agent_coordinates[1] < parcel_coordinates[1]:
        function_4()
    else:
        function_5()

def function_11():
    global belief_set
    delivery_cells = [cell for cell in belief_set['map']['grid'] if 
        'delivery' in cell['cell_type']]
    closest_delivery_cell = min(delivery_cells, key=lambda cell: abs(cell[
        'cell_coordinates'][0] - belief_set['agent']['coordinates'][0]) +
        abs(cell['cell_coordinates'][1] - belief_set['agent']['coordinates'
        ][1]))
    while belief_set['agent']['coordinates'] != closest_delivery_cell[
        'cell_coordinates']:
        if belief_set['agent']['coordinates'][0] < closest_delivery_cell[
            'cell_coordinates'][0]:
            function_2()
        elif belief_set['agent']['coordinates'][0] > closest_delivery_cell[
            'cell_coordinates'][0]:
            function_1()
        elif belief_set['agent']['coordinates'][1] < closest_delivery_cell[
            'cell_coordinates'][1]:
            function_4()
        else:
            function_3()
    function_6()

def function_12():
    global belief_set
    delivery_cells = [cell for cell in belief_set['map']['grid'] if 
        'delivery' in cell['cell_type']]
    agent_position = belief_set['agent']['coordinates']
    nearest_delivery_cell = min(delivery_cells, key=lambda cell: abs(cell[
        'cell_coordinates'][0] - agent_position[0]) + abs(cell[
        'cell_coordinates'][1] - agent_position[1]))
    while agent_position != nearest_delivery_cell['cell_coordinates']:
        if agent_position[0] < nearest_delivery_cell['cell_coordinates'][0]:
            function_2()
        elif agent_position[0] > nearest_delivery_cell['cell_coordinates'][0]:
            function_1()
        elif agent_position[1] < nearest_delivery_cell['cell_coordinates'][1]:
            function_4()
        elif agent_position[1] > nearest_delivery_cell['cell_coordinates'][1]:
            function_3()
        if agent_position == belief_set['agent']['coordinates']:
            break
        agent_position = belief_set['agent']['coordinates']
    function_6()

def function_13():
    global belief_set
    agent = belief_set['agent']
    parcels = agent['parcels_carried_ids']
    if parcels and any(cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] in ['delivery_cell', 'double_points_delivery_cell'] and
        cell['cell_coordinates'] == agent['coordinates']):
        function_6()
    elif agent['coordinates'][0] < belief_set['map']['width'] - 1:
        function_2()
    elif agent['coordinates'][0] > 0:
        function_1()
    elif agent['coordinates'][1] < belief_set['map']['height'] - 1:
        function_4()
    elif agent['coordinates'][1] > 0:
        function_3()

def function_15():
    global belief_set
    delivery_cells = [cell['cell_coordinates'] for cell in belief_set['map'
        ]['grid'] if 'delivery' in cell['cell_type']]
    agent_coordinates = belief_set['agent']['coordinates']
    if agent_coordinates in delivery_cells:
        function_6()
    else:
        target_cell = delivery_cells[0]
        if agent_coordinates[0] < target_cell[0]:
            function_2()
        elif agent_coordinates[0] > target_cell[0]:
            function_1()
        elif agent_coordinates[1] < target_cell[1]:
            function_4()
        elif agent_coordinates[1] > target_cell[1]:
            function_3()

def function_16():
    global belief_set
    agent_coordinates = belief_set['agent']['coordinates']
    if belief_set['agent']['parcels_carried_ids']:
        delivery_cells = [cell for cell in belief_set['map']['grid'] if 
            'delivery' in cell['cell_type']]
        delivery_cells.sort(key=lambda cell: abs(cell['cell_coordinates'][0
            ] - agent_coordinates[0]) + abs(cell['cell_coordinates'][1] -
            agent_coordinates[1]))
        target_coordinates = delivery_cells[0]['cell_coordinates']
        function_6(
            ) if agent_coordinates == target_coordinates else function_1(
            ) if agent_coordinates[0] > target_coordinates[0] else function_2(
            ) if agent_coordinates[0] < target_coordinates[0] else function_3(
            ) if agent_coordinates[1] > target_coordinates[1] else function_4()
    else:
        parcels = [parcel for parcel in belief_set['parcels'].values()]
        parcels.sort(key=lambda parcel: abs(parcel['coordinates'][0] -
            agent_coordinates[0]) + abs(parcel['coordinates'][1] -
            agent_coordinates[1]))
        target_coordinates = parcels[0]['coordinates']
        function_5(
            ) if agent_coordinates == target_coordinates else function_1(
            ) if agent_coordinates[0] > target_coordinates[0] else function_2(
            ) if agent_coordinates[0] < target_coordinates[0] else function_3(
            ) if agent_coordinates[1] > target_coordinates[1] else function_4()

def function_17():
    global belief_set
    agent_position = belief_set['agent']['coordinates']
    delivery_cells = [cell['cell_coordinates'] for cell in belief_set['map'
        ]['grid'] if 'delivery' in cell['cell_type']]
    closest_delivery_cell = min(delivery_cells, key=lambda cell: abs(cell[0
        ] - agent_position[0]) + abs(cell[1] - agent_position[1]))
    while agent_position != closest_delivery_cell:
        if agent_position[0] < closest_delivery_cell[0]:
            function_2()
        elif agent_position[0] > closest_delivery_cell[0]:
            function_1()
        elif agent_position[1] < closest_delivery_cell[1]:
            function_4()
        else:
            function_3()
    function_6()

def function_18():
    global belief_set
    delivery_cell = next(cell for cell in belief_set['map']['grid'] if cell
        ['cell_type'] in ['delivery_cell', 'double_points_delivery_cell'])
    agent = belief_set['agent']
    while agent['coordinates'] != delivery_cell['cell_coordinates']:
        if agent['coordinates'][0] < delivery_cell['cell_coordinates'][0]:
            function_2()
        elif agent['coordinates'][0] > delivery_cell['cell_coordinates'][0]:
            function_1()
        elif agent['coordinates'][1] < delivery_cell['cell_coordinates'][1]:
            function_4()
        elif agent['coordinates'][1] > delivery_cell['cell_coordinates'][1]:
            function_3()
    function_6()

def function_19():
    global belief_set
    delivered = False
    iterations = 0
    while not delivered and iterations < 50:
        agent_coords = belief_set['agent']['coordinates']
        delivery_coords = [cell['cell_coordinates'] for cell in belief_set[
            'map']['grid'] if cell['cell_type'] in ['delivery_cell',
            'double_points_delivery_cell']]
        for coords in delivery_coords:
            if agent_coords[0] < coords[0]:
                function_2()
            elif agent_coords[0] > coords[0]:
                function_1()
            elif agent_coords[1] < coords[1]:
                function_4()
            elif agent_coords[1] > coords[1]:
                function_3()
            else:
                function_6()
                delivered = True
                break
        iterations += 1

def function_20():
    global belief_set
    current_position = belief_set['agent']['coordinates']
    parcels_carried = belief_set['agent']['parcels_carried_ids']
    if parcels_carried:
        delivery_cell = next((cell['cell_coordinates'] for cell in
            belief_set['map']['grid'] if cell['cell_type'] in [
            'delivery_cell', 'double_points_delivery_cell']), None)
        if delivery_cell:
            previous_position = current_position
            while current_position != delivery_cell:
                if current_position[0] < delivery_cell[0]:
                    function_2()
                elif current_position[0] > delivery_cell[0]:
                    function_1()
                elif current_position[1] < delivery_cell[1]:
                    function_4()
                elif current_position[1] > delivery_cell[1]:
                    function_3()
                if current_position == previous_position:
                    break
                previous_position = current_position
            function_6()
    else:
        function_9()

def function_21():
    global belief_set
    keys = belief_set['keys']
    agent_position = belief_set['agent']['coordinates']
    for key_id, key_details in keys.items():
        if key_details['carried_by_id'] is None:
            key_position = key_details['coordinates']
            while agent_position != key_position:
                if agent_position[0] < key_position[0]:
                    function_2()
                elif agent_position[0] > key_position[0]:
                    function_1()
                if agent_position[1] < key_position[1]:
                    function_4()
                elif agent_position[1] > key_position[1]:
                    function_3()
            function_5()
            break

def function_22():
    global belief_set
    agent_position = belief_set['agent']['coordinates']
    parcel_position = sorted(belief_set['parcels'].values(), key=lambda x: 
        abs(x['coordinates'][0] - agent_position[0]) + abs(x['coordinates']
        [1] - agent_position[1]))[0]['coordinates']
    while agent_position != parcel_position and len(belief_set['agent'][
        'parcels_carried_ids']) == 0:
        if agent_position[0] < parcel_position[0]:
            function_2()
        elif agent_position[0] > parcel_position[0]:
            function_1()
        elif agent_position[1] < parcel_position[1]:
            function_4()
        elif agent_position[1] > parcel_position[1]:
            function_3()
        agent_position = belief_set['agent']['coordinates']
        if agent_position == parcel_position:
            function_5()
            break

def function_24():
    global belief_set
    agent = belief_set['agent']
    delivery_cell = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'double_points_delivery_cell'][0]['cell_coordinates']
    if agent['coordinates'][0] < delivery_cell[0]:
        function_2()
    elif agent['coordinates'][0] > delivery_cell[0]:
        function_1()
    elif agent['coordinates'][1] < delivery_cell[1]:
        function_4()
    elif agent['coordinates'][1] > delivery_cell[1]:
        function_3()
    else:
        function_6()

def function_25():
    global belief_set
    agent = belief_set['agent']
    parcels = belief_set['parcels']
    map = belief_set['map']['grid']
    keys = belief_set['keys']
    doors = belief_set['doors']
    for cell in map:
        if cell['cell_type'] == 'double_points_delivery_cell':
            target = cell['cell_coordinates']
    if 'carried_by_id' in parcels[1] and parcels[1]['carried_by_id'] == agent[
        'id']:
        if agent['coordinates'][0] < target[0]:
            function_2()
        elif agent['coordinates'][0] > target[0]:
            function_1()
        elif agent['coordinates'][1] < target[1]:
            function_4()
        else:
            function_3()
    else:
        if not agent['has_key']:
            for key in keys.values():
                if key['carried_by_id'] is None:
                    if agent['coordinates'][0] < key['coordinates'][0]:
                        function_2()
                    elif agent['coordinates'][0] > key['coordinates'][0]:
                        function_1()
                    elif agent['coordinates'][1] < key['coordinates'][1]:
                        function_4()
                    else:
                        function_3()
        else:
            for door in doors.values():
                if agent['coordinates'][0] < door['coordinates'][0]:
                    function_2()
                elif agent['coordinates'][0] > door['coordinates'][0]:
                    function_1()
                elif agent['coordinates'][1] < door['coordinates'][1]:
                    function_4()
                else:
                    function_3()
        function_5()
    function_6()

def function_26():
    global belief_set
    if not belief_set['agent']['parcels_carried_ids']:
        function_23()
    else:
        coordinates = belief_set['agent']['coordinates']
        delivery_cells = [cell['cell_coordinates'] for cell in belief_set[
            'map']['grid'] if cell['cell_type'] in ['delivery_cell',
            'double_points_delivery_cell']]
        delivery_cells.sort(key=lambda x: abs(coordinates[0] - x[0]) + abs(
            coordinates[1] - x[1]))
        target_cell = delivery_cells[0]
        while coordinates != target_cell:
            if coordinates[0] < target_cell[0]:
                function_2()
            elif coordinates[0] > target_cell[0]:
                function_1()
            elif coordinates[1] < target_cell[1]:
                function_4()
            elif coordinates[1] > target_cell[1]:
                function_3()
            coordinates = belief_set['agent']['coordinates']
        function_6()

