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
    parcel = list(belief_set['parcels'].values())[0]
    agent = belief_set['agents'][1]
    while parcel['coordinates'] != agent['coordinates']:
        if parcel['coordinates'][0] < agent['coordinates'][0]:
            function_1()
            agent['coordinates'][0] -= 1
        elif parcel['coordinates'][0] > agent['coordinates'][0]:
            function_2()
            agent['coordinates'][0] += 1
        elif parcel['coordinates'][1] < agent['coordinates'][1]:
            function_3()
            agent['coordinates'][1] -= 1
        elif parcel['coordinates'][1] > agent['coordinates'][1]:
            function_4()
            agent['coordinates'][1] += 1
    function_5()
    parcel['carried_by_id'] = 1
    agent['parcels_carried_ids'].append(parcel['id'])

def function_8():
    global belief_set
    agent = belief_set['agents'][1]
    parcel = belief_set['parcels'][agent['parcels_carried_ids'][0]]
    delivery_cells = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] in ['delivery_cell', 'double_points_delivery_cell']]
    nearest_delivery_cell = min(delivery_cells, key=lambda cell: abs(cell[
        'cell_coordinates'][0] - agent['coordinates'][0]) + abs(cell[
        'cell_coordinates'][1] - agent['coordinates'][1]))
    while agent['coordinates'] != nearest_delivery_cell['cell_coordinates']:
        if agent['coordinates'][0] < nearest_delivery_cell['cell_coordinates'][
            0]:
            function_2()
        elif agent['coordinates'][0] > nearest_delivery_cell['cell_coordinates'
            ][0]:
            function_1()
        elif agent['coordinates'][1] < nearest_delivery_cell['cell_coordinates'
            ][1]:
            function_4()
        elif agent['coordinates'][1] > nearest_delivery_cell['cell_coordinates'
            ][1]:
            function_3()
    function_6()

def function_9():
    global belief_set
    max_iterations = 100
    i = 0
    agent = belief_set['agents'][1]
    delivery_cell = [3, 0]
    while i < max_iterations and agent['coordinates'] != delivery_cell:
        if agent['coordinates'][0] < delivery_cell[0]:
            function_2()
            agent['coordinates'][0] += 1
        elif agent['coordinates'][0] > delivery_cell[0]:
            function_1()
            agent['coordinates'][0] -= 1
        elif agent['coordinates'][1] < delivery_cell[1]:
            function_4()
            agent['coordinates'][1] += 1
        elif agent['coordinates'][1] > delivery_cell[1]:
            function_3()
            agent['coordinates'][1] -= 1
        i += 1
    if agent['coordinates'] == delivery_cell:
        function_6()
    return

def function_10():
    global belief_set
    key_coordinates = None
    for key_id, key_info in belief_set['keys'].items():
        if key_info['carried_by_id'] is None:
            key_coordinates = key_info['coordinates']
            break
    if key_coordinates is None:
        return
    agent_coordinates = belief_set['agents'][1]['coordinates']
    while agent_coordinates[0] != key_coordinates[0]:
        if agent_coordinates[0] > key_coordinates[0]:
            function_1()
        else:
            function_2()
    while agent_coordinates[1] != key_coordinates[1]:
        if agent_coordinates[1] > key_coordinates[1]:
            function_3()
        else:
            function_4()
    function_5()
    door_coordinates = None
    for door_id, door_info in belief_set['doors'].items():
        door_coordinates = door_info['coordinates']
        break
    while agent_coordinates[0] != door_coordinates[0]:
        if agent_coordinates[0] > door_coordinates[0]:
            function_1()
        else:
            function_2()
    while agent_coordinates[1] != door_coordinates[1]:
        if agent_coordinates[1] > door_coordinates[1]:
            function_3()
        else:
            function_4()

def function_11():
    global belief_set
    agent_id = 1
    agent = belief_set['agents'][agent_id]
    key = [k for k in belief_set['keys'].values() if k['carried_by_id'] is None
        ][0]
    key_coords = key['coordinates']
    iteration_count = 0
    while agent['coordinates'] != key_coords and iteration_count < 100:
        if agent['coordinates'][0] > key_coords[0]:
            function_1()
        elif agent['coordinates'][0] < key_coords[0]:
            function_2()
        elif agent['coordinates'][1] > key_coords[1]:
            function_3()
        elif agent['coordinates'][1] < key_coords[1]:
            function_4()
        agent['coordinates'] = [agent['coordinates'][0] - 1 if agent[
            'coordinates'][0] > key_coords[0] else agent['coordinates'][0] +
            1 if agent['coordinates'][0] < key_coords[0] else agent[
            'coordinates'][0], agent['coordinates'][1] - 1 if agent[
            'coordinates'][1] > key_coords[1] else agent['coordinates'][1] +
            1 if agent['coordinates'][1] < key_coords[1] else agent[
            'coordinates'][1]]
        iteration_count += 1
    function_5()
    if 'has_key' in agent and agent['has_key']:
        door_coords = [d['coordinates'] for d in belief_set['doors'].values()][
            0]
        iteration_count = 0
        while agent['coordinates'] != door_coords and iteration_count < 100:
            if agent['coordinates'][0] > door_coords[0]:
                function_1()
            elif agent['coordinates'][0] < door_coords[0]:
                function_2()
            elif agent['coordinates'][1] > door_coords[1]:
                function_3()
            elif agent['coordinates'][1] < door_coords[1]:
                function_4()
            agent['coordinates'] = [agent['coordinates'][0] - 1 if agent[
                'coordinates'][0] > door_coords[0] else agent['coordinates'
                ][0] + 1 if agent['coordinates'][0] < door_coords[0] else
                agent['coordinates'][0], agent['coordinates'][1] - 1 if 
                agent['coordinates'][1] > door_coords[1] else agent[
                'coordinates'][1] + 1 if agent['coordinates'][1] <
                door_coords[1] else agent['coordinates'][1]]
            iteration_count += 1

def function_12():
    global belief_set
    doors = belief_set['doors']
    agent = belief_set['agents'][1]
    min_distance = float('inf')
    nearest_door = None
    for door in doors.values():
        distance = abs(door['coordinates'][0] - agent['coordinates'][0]) + abs(
            door['coordinates'][1] - agent['coordinates'][1])
        if distance < min_distance:
            min_distance = distance
            nearest_door = door
    if nearest_door is not None:
        if nearest_door['coordinates'][0] < agent['coordinates'][0]:
            function_1()
        elif nearest_door['coordinates'][0] > agent['coordinates'][0]:
            function_2()
        if nearest_door['coordinates'][1] < agent['coordinates'][1]:
            function_3()
        elif nearest_door['coordinates'][1] > agent['coordinates'][1]:
            function_4()

