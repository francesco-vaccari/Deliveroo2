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
    agent_x, agent_y = belief_set['agent']['coordinates']
    shortest_distance = float('inf')
    target_object = None
    for parcel in belief_set['parcels'].values():
        if parcel['carried_by_id'] is None:
            parcel_x, parcel_y = parcel['coordinates']
            distance = abs(agent_x - parcel_x) + abs(agent_y - parcel_y)
            if distance < shortest_distance:
                shortest_distance = distance
                target_object = parcel
    for key in belief_set['keys'].values():
        if key['carried_by_id'] is None:
            key_x, key_y = key['coordinates']
            distance = abs(agent_x - key_x) + abs(agent_y - key_y)
            if distance < shortest_distance:
                shortest_distance = distance
                target_object = key
    if target_object is not None:
        target_x, target_y = target_object['coordinates']
        if agent_x > target_x:
            function_1()
        elif agent_x < target_x:
            function_2()
        elif agent_y > target_y:
            function_3()
        elif agent_y < target_y:
            function_4()
        else:
            function_5()

def function_8():
    global belief_set
    agent = belief_set['agent']
    parcels = belief_set['parcels']
    parcel_coordinates = min(parcels.values(), key=lambda x: abs(x[
        'coordinates'][0] - agent['coordinates'][0]) + abs(x['coordinates']
        [1] - agent['coordinates'][1]))['coordinates']
    while agent['coordinates'] != parcel_coordinates:
        if agent['coordinates'][0] < parcel_coordinates[0]:
            function_2()
        elif agent['coordinates'][0] > parcel_coordinates[0]:
            function_1()
        elif agent['coordinates'][1] < parcel_coordinates[1]:
            function_4()
        elif agent['coordinates'][1] > parcel_coordinates[1]:
            function_3()
    function_5()

def function_9():
    global belief_set
    agent_coordinates = belief_set['agent']['coordinates']
    nearest_parcel_coordinates = belief_set['parcels'][1]['coordinates']
    while agent_coordinates != nearest_parcel_coordinates:
        if agent_coordinates[0] < nearest_parcel_coordinates[0]:
            function_2()
            if belief_set['agent']['coordinates'] == agent_coordinates:
                break
        elif agent_coordinates[0] > nearest_parcel_coordinates[0]:
            function_1()
            if belief_set['agent']['coordinates'] == agent_coordinates:
                break
        elif agent_coordinates[1] < nearest_parcel_coordinates[1]:
            function_4()
            if belief_set['agent']['coordinates'] == agent_coordinates:
                break
        elif agent_coordinates[1] > nearest_parcel_coordinates[1]:
            function_3()
            if belief_set['agent']['coordinates'] == agent_coordinates:
                break
        agent_coordinates = belief_set['agent']['coordinates']
    function_5()

def function_10():
    global belief_set
    key_positions = [key['coordinates'] for key in belief_set['keys'].
        values() if key['carried_by_id'] is None]
    agent_position = belief_set['agent']['coordinates']
    nearest_key_position = min(key_positions, key=lambda pos: abs(pos[0] -
        agent_position[0]) + abs(pos[1] - agent_position[1]))
    while agent_position != nearest_key_position:
        if agent_position[0] < nearest_key_position[0]:
            function_2()
        elif agent_position[0] > nearest_key_position[0]:
            function_1()
        elif agent_position[1] < nearest_key_position[1]:
            function_4()
        elif agent_position[1] > nearest_key_position[1]:
            function_3()
        agent_position = belief_set['agent']['coordinates']
    function_5()

def function_11():
    global belief_set
    agent_position = belief_set['agent']['coordinates']
    delivery_cells = [cell['cell_coordinates'] for cell in belief_set['map'
        ]['grid'] if 'delivery' in cell['cell_type']]
    nearest_delivery_cell = min(delivery_cells, key=lambda x: abs(x[0] -
        agent_position[0]) + abs(x[1] - agent_position[1]))
    while agent_position != nearest_delivery_cell:
        if nearest_delivery_cell[0] < agent_position[0]:
            function_1()
            agent_position[0] -= 1
        elif nearest_delivery_cell[0] > agent_position[0]:
            function_2()
            agent_position[0] += 1
        elif nearest_delivery_cell[1] < agent_position[1]:
            function_3()
            agent_position[1] -= 1
        elif nearest_delivery_cell[1] > agent_position[1]:
            function_4()
            agent_position[1] += 1
    function_6()

def function_12():
    global belief_set
    if 'keys' in belief_set and belief_set['keys']:
        function_10()
    else:
        function_9()

def function_13():
    global belief_set
    if belief_set['agent']['has_key']:
        for door in belief_set['doors'].values():
            if belief_set['agent']['coordinates'] == door['coordinates']:
                function_5()
    else:
        function_10()
    for parcel in belief_set['parcels'].values():
        if belief_set['agent']['coordinates'] == parcel['coordinates']:
            function_5()
    if belief_set['agent']['parcels_carried_ids']:
        function_11()

def function_14():
    global belief_set
    if belief_set['agent']['parcels_carried_ids']:
        function_11()
    else:
        function_9()
    if belief_set['agent']['parcels_carried_ids']:
        function_11()
    else:
        function_9()

def function_15():
    global belief_set
    if belief_set['agent']['parcels_carried_ids'] == []:
        function_9()
    else:
        function_11()
    return

