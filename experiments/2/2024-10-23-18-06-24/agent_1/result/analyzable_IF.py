def function_1():
    with open('agent_dir/functions/agent_1/plan.txt', 'a') as f:
        f.write('action_1\n')
        f.close()
    wait()


def function_2():
    with open('agent_dir/functions/agent_1/plan.txt', 'a') as f:
        f.write('action_2\n')
        f.close()
    wait()


def function_3():
    with open('agent_dir/functions/agent_1/plan.txt', 'a') as f:
        f.write('action_3\n')
        f.close()
    wait()


def function_4():
    with open('agent_dir/functions/agent_1/plan.txt', 'a') as f:
        f.write('action_4\n')
        f.close()
    wait()


def function_5():
    with open('agent_dir/functions/agent_1/plan.txt', 'a') as f:
        f.write('action_5\n')
        f.close()
    wait()


def function_6():
    with open('agent_dir/functions/agent_1/plan.txt', 'a') as f:
        f.write('action_6\n')
        f.close()
    wait()


def function_7():
    global belief_set
    agent_coordinates = belief_set['agent']['coordinates']
    parcel_coordinates = belief_set['parcel'][1]['coordinates']
    if agent_coordinates[0] > parcel_coordinates[0]:
        function_1()
    elif agent_coordinates[0] < parcel_coordinates[0]:
        function_2()
    elif agent_coordinates[1] > parcel_coordinates[1]:
        function_3()
    elif agent_coordinates[1] < parcel_coordinates[1]:
        function_4()

def function_8():
    global belief_set
    while belief_set['agent']['coordinates'][0] > belief_set['parcel'][1][
        'coordinates'][0]:
        function_1()
    while belief_set['agent']['coordinates'][0] < belief_set['parcel'][1][
        'coordinates'][0]:
        function_2()
    while belief_set['agent']['coordinates'][1] > belief_set['parcel'][1][
        'coordinates'][1]:
        function_3()
    while belief_set['agent']['coordinates'][1] < belief_set['parcel'][1][
        'coordinates'][1]:
        function_4()
    function_5()
    while belief_set['agent']['coordinates'][0] > belief_set['map']['grid'][7][
        'cell_coordinates'][0]:
        function_1()
    while belief_set['agent']['coordinates'][0] < belief_set['map']['grid'][7][
        'cell_coordinates'][0]:
        function_2()
    while belief_set['agent']['coordinates'][1] > belief_set['map']['grid'][7][
        'cell_coordinates'][1]:
        function_3()
    while belief_set['agent']['coordinates'][1] < belief_set['map']['grid'][7][
        'cell_coordinates'][1]:
        function_4()
    function_6()

def function_9():
    global belief_set
    parcel_coordinates = belief_set['parcel'][1]['coordinates']
    agent_coordinates = belief_set['agent']['coordinates']
    delivery_coordinates = [i for i in belief_set['map']['grid'] if i[
        'cell_type'] == 'delivery_cell'][0]['cell_coordinates']
    while agent_coordinates != parcel_coordinates:
        if agent_coordinates[0] < parcel_coordinates[0]:
            function_2()
        elif agent_coordinates[0] > parcel_coordinates[0]:
            function_1()
        elif agent_coordinates[1] < parcel_coordinates[1]:
            function_4()
        elif agent_coordinates[1] > parcel_coordinates[1]:
            function_3()
        agent_coordinates = belief_set['agent']['coordinates']
    function_5()
    while agent_coordinates != delivery_coordinates:
        if agent_coordinates[0] < delivery_coordinates[0]:
            function_2()
        elif agent_coordinates[0] > delivery_coordinates[0]:
            function_1()
        elif agent_coordinates[1] < delivery_coordinates[1]:
            function_4()
        elif agent_coordinates[1] > delivery_coordinates[1]:
            function_3()
        agent_coordinates = belief_set['agent']['coordinates']
    function_6()

def function_10():
    global belief_set
    delivery_cell = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'delivery_cell'][0]['cell_coordinates']
    while belief_set['agent']['coordinates'] != delivery_cell:
        if belief_set['agent']['coordinates'][0] > delivery_cell[0]:
            function_1()
        elif belief_set['agent']['coordinates'][0] < delivery_cell[0]:
            function_2()
        elif belief_set['agent']['coordinates'][1] > delivery_cell[1]:
            function_3()
        elif belief_set['agent']['coordinates'][1] < delivery_cell[1]:
            function_4()
    function_6()

def function_11():
    global belief_set
    delivery_cell = [cell['cell_coordinates'] for cell in belief_set['map']
        ['grid'] if cell['cell_type'] == 'delivery_cell'][0]
    agent_coordinates = belief_set['agent']['coordinates']
    max_attempts = 10
    attempts = 0
    while agent_coordinates != delivery_cell and attempts < max_attempts:
        if agent_coordinates[0] < delivery_cell[0]:
            if {'cell_coordinates': [agent_coordinates[0] + 1,
                agent_coordinates[1]], 'cell_type': 'non_walkable'
                } not in belief_set['map']['grid']:
                function_2()
        elif agent_coordinates[0] > delivery_cell[0]:
            if {'cell_coordinates': [agent_coordinates[0] - 1,
                agent_coordinates[1]], 'cell_type': 'non_walkable'
                } not in belief_set['map']['grid']:
                function_1()
        if agent_coordinates[1] < delivery_cell[1]:
            if {'cell_coordinates': [agent_coordinates[0], 
                agent_coordinates[1] + 1], 'cell_type': 'non_walkable'
                } not in belief_set['map']['grid']:
                function_4()
        elif agent_coordinates[1] > delivery_cell[1]:
            if {'cell_coordinates': [agent_coordinates[0], 
                agent_coordinates[1] - 1], 'cell_type': 'non_walkable'
                } not in belief_set['map']['grid']:
                function_3()
        attempts += 1
    function_6()
    return

def function_12():
    global belief_set
    agent_coords = belief_set['agent']['coordinates']
    parcel_coords = belief_set['parcel'][1]['coordinates']
    delivery_coords = [x for x in belief_set['map']['grid'] if x[
        'cell_type'] == 'delivery_cell'][0]['cell_coordinates']
    while agent_coords != parcel_coords:
        if agent_coords[0] < parcel_coords[0]:
            function_2()
        elif agent_coords[0] > parcel_coords[0]:
            function_1()
        elif agent_coords[1] < parcel_coords[1]:
            function_4()
        else:
            function_3()
    function_5()
    while agent_coords != delivery_coords:
        if agent_coords[0] < delivery_coords[0]:
            function_2()
        elif agent_coords[0] > delivery_coords[0]:
            function_1()
        elif agent_coords[1] < delivery_coords[1]:
            function_4()
        else:
            function_3()
    function_6()

def function_13():
    global belief_set
    agent = belief_set['agent']
    delivery_cell = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'delivery_cell'][0]
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

def function_14():
    global belief_set
    delivery_coordinates = [cell['cell_coordinates'] for cell in belief_set
        ['map']['grid'] if cell['cell_type'] == 'delivery_cell'][0]
    agent_coordinates = belief_set['agent']['coordinates']
    max_iterations = belief_set['map']['width'] * belief_set['map']['height']
    counter = 0
    while (agent_coordinates != delivery_coordinates and counter <
        max_iterations):
        if agent_coordinates[1] < delivery_coordinates[1]:
            function_4()
        elif agent_coordinates[0] < delivery_coordinates[0]:
            function_2()
        else:
            function_1()
        counter += 1
        agent_coordinates = belief_set['agent']['coordinates']

def function_15():
    global belief_set
    agent = belief_set['agent']
    map_cells = belief_set['map']['grid']
    agent_coords = agent['coordinates']
    delivery_cell_coords = next(cell['cell_coordinates'] for cell in
        map_cells if cell['cell_type'] == 'delivery_cell')
    delta_x = delivery_cell_coords[0] - agent_coords[0]
    delta_y = delivery_cell_coords[1] - agent_coords[1]
    if delta_x > 0 and next(cell for cell in map_cells if cell[
        'cell_coordinates'] == [agent_coords[0] + 1, agent_coords[1]])[
        'cell_type'] == 'walkable':
        function_2()
    elif delta_x < 0 and next(cell for cell in map_cells if cell[
        'cell_coordinates'] == [agent_coords[0] - 1, agent_coords[1]])[
        'cell_type'] == 'walkable':
        function_1()
    elif delta_y > 0 and next(cell for cell in map_cells if cell[
        'cell_coordinates'] == [agent_coords[0], agent_coords[1] + 1])[
        'cell_type'] == 'walkable':
        function_4()
    elif delta_y < 0 and next(cell for cell in map_cells if cell[
        'cell_coordinates'] == [agent_coords[0], agent_coords[1] - 1])[
        'cell_type'] == 'walkable':
        function_3()
    if belief_set['key'][1]['coordinates'] == agent_coords and not agent[
        'has_key']:
        function_5()

def function_16():
    global belief_set
    agent_coords = belief_set['agent']['coordinates']
    key_coords = belief_set['key'][1]['coordinates']
    while agent_coords[0] > key_coords[0]:
        function_1()
        agent_coords = belief_set['agent']['coordinates']
    while agent_coords[0] < key_coords[0]:
        function_2()
        agent_coords = belief_set['agent']['coordinates']
    while agent_coords[1] > key_coords[1]:
        function_3()
        agent_coords = belief_set['agent']['coordinates']
    while agent_coords[1] < key_coords[1]:
        function_4()
        agent_coords = belief_set['agent']['coordinates']
    function_5()
    min_distance = float('inf')
    nearest_door_coords = None
    for door_id, door_info in belief_set['door'].items():
        distance = abs(door_info['coordinates'][0] - agent_coords[0]) + abs(
            door_info['coordinates'][1] - agent_coords[1])
        if distance < min_distance:
            min_distance = distance
            nearest_door_coords = door_info['coordinates']
    while agent_coords[0] > nearest_door_coords[0]:
        function_1()
        agent_coords = belief_set['agent']['coordinates']
    while agent_coords[0] < nearest_door_coords[0]:
        function_2()
        agent_coords = belief_set['agent']['coordinates']
    while agent_coords[1] > nearest_door_coords[1]:
        function_3()
        agent_coords = belief_set['agent']['coordinates']
    while agent_coords[1] < nearest_door_coords[1]:
        function_4()
        agent_coords = belief_set['agent']['coordinates']

def function_17():
    global belief_set
    delivery_cell_coordinates = next(cell['cell_coordinates'] for cell in
        belief_set['map']['grid'] if cell['cell_type'] == 'delivery_cell')
    agent_coordinates = belief_set['agent']['coordinates']
    while agent_coordinates != delivery_cell_coordinates:
        if agent_coordinates[0] > delivery_cell_coordinates[0]:
            function_1()
        elif agent_coordinates[0] < delivery_cell_coordinates[0]:
            function_2()
        elif agent_coordinates[1] > delivery_cell_coordinates[1]:
            function_3()
        elif agent_coordinates[1] < delivery_cell_coordinates[1]:
            function_4()
        agent_coordinates = belief_set['agent']['coordinates']
    function_6()

def function_18():
    global belief_set
    key_coords = belief_set['key'][1]['coordinates']
    agent_coords = belief_set['agent']['coordinates']
    while agent_coords != key_coords:
        if agent_coords[0] < key_coords[0]:
            function_2()
        elif agent_coords[0] > key_coords[0]:
            function_1()
        elif agent_coords[1] < key_coords[1]:
            function_4()
        else:
            function_3()
    function_5()
    door_coords = belief_set['door'][1]['coordinates']
    while agent_coords != door_coords:
        if agent_coords[0] < door_coords[0]:
            function_2()
        elif agent_coords[0] > door_coords[0]:
            function_1()
        elif agent_coords[1] < door_coords[1]:
            function_4()
        else:
            function_3()
    function_6()

def function_19():
    global belief_set
    delivery_cell = [cell['cell_coordinates'] for cell in belief_set['map']
        ['grid'] if cell['cell_type'] == 'delivery_cell'][0]
    agent_coords = belief_set['agent']['coordinates']
    while agent_coords != delivery_cell:
        if agent_coords[0] > delivery_cell[0]:
            function_1()
        elif agent_coords[0] < delivery_cell[0]:
            function_2()
        elif agent_coords[1] > delivery_cell[1]:
            function_3()
        elif agent_coords[1] < delivery_cell[1]:
            function_4()
        agent_coords = belief_set['agent']['coordinates']
    if belief_set['agent']['parcels_carried_ids']:
        function_17()

def function_20():
    global belief_set
    spawn_cell_coordinates = [cell['cell_coordinates'] for cell in
        belief_set['map']['grid'] if cell['cell_type'] == 'parcels_spawn'][0]
    delivery_cell_coordinates = [cell['cell_coordinates'] for cell in
        belief_set['map']['grid'] if cell['cell_type'] == 'delivery_cell'][0]
    while belief_set['agent']['coordinates'] != spawn_cell_coordinates:
        if belief_set['agent']['coordinates'][0] < spawn_cell_coordinates[0]:
            function_2()
        elif belief_set['agent']['coordinates'][0] > spawn_cell_coordinates[0]:
            function_1()
        elif belief_set['agent']['coordinates'][1] < spawn_cell_coordinates[1]:
            function_4()
        else:
            function_3()
    function_5()
    while belief_set['agent']['coordinates'] != delivery_cell_coordinates:
        if belief_set['agent']['coordinates'][0] < delivery_cell_coordinates[0
            ]:
            function_2()
        elif belief_set['agent']['coordinates'][0] > delivery_cell_coordinates[
            0]:
            function_1()
        elif belief_set['agent']['coordinates'][1] < delivery_cell_coordinates[
            1]:
            function_4()
        else:
            function_3()
    function_17()

