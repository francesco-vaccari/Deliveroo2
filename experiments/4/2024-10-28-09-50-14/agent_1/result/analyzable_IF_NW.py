def function_7():
    global belief_set
    current_position = belief_set['agents'][1]['coordinates']
    parcel_position = belief_set['parcels'][1]['coordinates']
    if current_position[0] > parcel_position[0]:
        function_1()
    elif current_position[0] < parcel_position[0]:
        function_2()
    elif current_position[1] > parcel_position[1]:
        function_3()
    elif current_position[1] < parcel_position[1]:
        function_4()
    else:
        function_5()

def function_8():
    global belief_set
    agent_pos = belief_set['agents'][1]['coordinates']
    parcel_pos = belief_set['parcels'][1]['coordinates']
    if agent_pos[0] > parcel_pos[0]:
        function_1()
    elif agent_pos[0] < parcel_pos[0]:
        function_2()
    elif agent_pos[1] > parcel_pos[1]:
        function_3()
    elif agent_pos[1] < parcel_pos[1]:
        function_4()
    elif agent_pos == parcel_pos:
        function_5()

def function_10():
    global belief_set
    agent_location = belief_set['agents'][1]['coordinates']
    delivery_cells = [cell['cell_coordinates'] for cell in belief_set['map'
        ]['grid'] if 'delivery' in cell['cell_type']]
    delivery_cells.sort(key=lambda x: abs(x[0] - agent_location[0]) + abs(x
        [1] - agent_location[1]))
    target_cell = delivery_cells[0]
    if agent_location[0] < target_cell[0]:
        function_2()
    elif agent_location[0] > target_cell[0]:
        function_1()
    elif agent_location[1] < target_cell[1]:
        function_4()
    elif agent_location[1] > target_cell[1]:
        function_3()
    else:
        function_6()

def function_11():
    global belief_set
    if not belief_set['agents'][1]['parcels_carried_ids']:
        function_9()
    else:
        parcel_coordinates = belief_set['parcels'][belief_set['agents'][1][
            'parcels_carried_ids'][0]]['coordinates']
        delivery_coordinates = [cell['cell_coordinates'] for cell in
            belief_set['map']['grid'] if 'delivery_cell' in cell['cell_type']][
            0]
        if parcel_coordinates[0] < delivery_coordinates[0]:
            function_2()
        elif parcel_coordinates[0] > delivery_coordinates[0]:
            function_1()
        elif parcel_coordinates[1] < delivery_coordinates[1]:
            function_4()
        elif parcel_coordinates[1] > delivery_coordinates[1]:
            function_3()
        else:
            function_6()

def function_12():
    global belief_set
    agent = belief_set['agents'][1]
    delivery_cells = [cell for cell in belief_set['map']['grid'] if 
        'delivery' in cell['cell_type']]
    min_distance = float('inf')
    target_cell = None
    for cell in delivery_cells:
        distance = abs(agent['coordinates'][0] - cell['cell_coordinates'][0]
            ) + abs(agent['coordinates'][1] - cell['cell_coordinates'][1])
        if distance < min_distance:
            min_distance = distance
            target_cell = cell
    if target_cell:
        if agent['coordinates'][0] > target_cell['cell_coordinates'][0]:
            function_1()
        elif agent['coordinates'][0] < target_cell['cell_coordinates'][0]:
            function_2()
        elif agent['coordinates'][1] > target_cell['cell_coordinates'][1]:
            function_3()
        elif agent['coordinates'][1] < target_cell['cell_coordinates'][1]:
            function_4()
        else:
            function_6()

def function_13():
    global belief_set
    delivery_cells = [cell for cell in belief_set['map']['grid'] if 
        'delivery' in cell['cell_type']]
    agent_coordinates = belief_set['agents'][1]['coordinates']
    nearest_delivery_cell = None
    min_distance = float('inf')
    for cell in delivery_cells:
        distance = abs(cell['cell_coordinates'][0] - agent_coordinates[0]
            ) + abs(cell['cell_coordinates'][1] - agent_coordinates[1])
        if distance < min_distance:
            min_distance = distance
            nearest_delivery_cell = cell
    delta_x = nearest_delivery_cell['cell_coordinates'][0] - agent_coordinates[
        0]
    delta_y = nearest_delivery_cell['cell_coordinates'][1] - agent_coordinates[
        1]
    if delta_x < 0:
        for _ in range(abs(delta_x)):
            function_1()
    elif delta_x > 0:
        for _ in range(delta_x):
            function_2()
    if delta_y < 0:
        for _ in range(abs(delta_y)):
            function_3()
    elif delta_y > 0:
        for _ in range(delta_y):
            function_4()
    function_6()

def function_14():
    global belief_set
    while belief_set['agents'][1]['has_key'] == False:
        function_9()
        function_5()
    while belief_set['agents'][1]['has_key'] == True:
        function_1()
        function_5()

def function_15():
    global belief_set
    max_attempts = 100
    attempts = 0
    while not belief_set['agents'][1]['has_key'] and attempts < max_attempts:
        function_9()
        function_5()
        attempts += 1
    if belief_set['agents'][1]['has_key']:
        while belief_set['doors'] and attempts < max_attempts:
            function_9()
            attempts += 1
    else:
        while belief_set['parcels'] and attempts < max_attempts:
            function_9()
            attempts += 1

def function_16():
    global belief_set
    agent = belief_set['agents'][1]
    key_locations = [key['coordinates'] for key in belief_set['keys'].
        values() if key['carried_by_id'] is None]
    if not agent['has_key'] and key_locations:
        nearest_key_location = min(key_locations, key=lambda c: abs(c[0] -
            agent['coordinates'][0]) + abs(c[1] - agent['coordinates'][1]))
        while agent['coordinates'] != nearest_key_location:
            if agent['coordinates'][0] < nearest_key_location[0]:
                function_2()
            elif agent['coordinates'][0] > nearest_key_location[0]:
                function_1()
            if agent['coordinates'][1] < nearest_key_location[1]:
                function_4()
            elif agent['coordinates'][1] > nearest_key_location[1]:
                function_3()
        function_5()

def function_17():
    global belief_set
    agent = belief_set['agents'][1]
    if not agent['has_key']:
        nearest_key_location = min(belief_set['keys'], key=lambda k: abs(
            agent['coordinates'][0] - belief_set['keys'][k]['coordinates'][
            0]) + abs(agent['coordinates'][1] - belief_set['keys'][k][
            'coordinates'][1]))
        nearest_key_location = belief_set['keys'][nearest_key_location][
            'coordinates']
        previous_location = agent['coordinates'].copy()
        while agent['coordinates'] != nearest_key_location:
            if agent['coordinates'][0] < nearest_key_location[0]:
                function_2()
            elif agent['coordinates'][0] > nearest_key_location[0]:
                function_1()
            if agent['coordinates'][1] < nearest_key_location[1]:
                function_4()
            elif agent['coordinates'][1] > nearest_key_location[1]:
                function_3()
            if agent['coordinates'] == previous_location:
                break
            previous_location = agent['coordinates'].copy()
        if agent['coordinates'] == nearest_key_location:
            function_5()

def function_19():
    global belief_set
    if belief_set['agents'][1]['parcels_carried_ids']:
        function_6()
        for cell in belief_set['map']['grid']:
            if cell['cell_type'] == 'delivery_cell' or cell['cell_type'
                ] == 'double_points_delivery_cell':
                while belief_set['agents'][1]['coordinates'] != cell[
                    'cell_coordinates']:
                    if belief_set['agents'][1]['coordinates'][0] > cell[
                        'cell_coordinates'][0]:
                        function_1()
                    elif belief_set['agents'][1]['coordinates'][0] < cell[
                        'cell_coordinates'][0]:
                        function_2()
                    elif belief_set['agents'][1]['coordinates'][1] > cell[
                        'cell_coordinates'][1]:
                        function_3()
                    else:
                        function_4()
    else:
        function_9()

def function_20():
    global belief_set
    max_iterations = 1000
    iteration = 0
    while iteration < max_iterations:
        iteration += 1
        previous_location = belief_set['agents'][1]['coordinates']
        if len(belief_set['agents'][1]['parcels_carried_ids']) == 0:
            function_9()
        else:
            function_18()
        if belief_set['agents'][1]['coordinates'] == previous_location:
            break

