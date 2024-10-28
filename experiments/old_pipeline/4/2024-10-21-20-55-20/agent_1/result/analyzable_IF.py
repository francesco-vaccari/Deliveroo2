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
    agent_pos = belief_set['agent']['coordinates']
    key_pos = belief_set['keys'][1]['coordinates']
    while agent_pos != key_pos:
        if agent_pos[0] < key_pos[0]:
            function_2()
        elif agent_pos[0] > key_pos[0]:
            function_1()
        elif agent_pos[1] < key_pos[1]:
            function_4()
        elif agent_pos[1] > key_pos[1]:
            function_3()
        agent_pos = belief_set['agent']['coordinates']
    function_5()
    door_pos = min(belief_set['doors'].values(), key=lambda x: abs(x[
        'coordinates'][0] - agent_pos[0]) + abs(x['coordinates'][1] -
        agent_pos[1]))['coordinates']
    while agent_pos != door_pos:
        if agent_pos[0] < door_pos[0]:
            function_2()
        elif agent_pos[0] > door_pos[0]:
            function_1()
        elif agent_pos[1] < door_pos[1]:
            function_4()
        elif agent_pos[1] > door_pos[1]:
            function_3()
        agent_pos = belief_set['agent']['coordinates']
    function_6()

def function_8():
    global belief_set
    agent = belief_set['agent']
    keys = belief_set['keys']
    if not agent['has_key'] and keys[1]['carried_by_id'] is None and agent[
        'coordinates'] == keys[1]['coordinates']:
        function_5()
        return
    doors = belief_set['doors']
    door_1 = doors[1]['coordinates']
    door_2 = doors[2]['coordinates']
    if agent['has_key']:
        if abs(agent['coordinates'][0] - door_1[0]) + abs(agent[
            'coordinates'][1] - door_1[1]) < abs(agent['coordinates'][0] -
            door_2[0]) + abs(agent['coordinates'][1] - door_2[1]):
            if agent['coordinates'][0] > door_1[0]:
                function_1()
            elif agent['coordinates'][0] < door_1[0]:
                function_2()
            elif agent['coordinates'][1] > door_1[1]:
                function_3()
            else:
                function_4()
        elif agent['coordinates'][0] > door_2[0]:
            function_1()
        elif agent['coordinates'][0] < door_2[0]:
            function_2()
        elif agent['coordinates'][1] > door_2[1]:
            function_3()
        else:
            function_4()
        return

def function_9():
    global belief_set
    agent_position = belief_set['agent']['coordinates']
    nearest_door = min(belief_set['doors'].values(), key=lambda d: abs(d[
        'coordinates'][0] - agent_position[0]) + abs(d['coordinates'][1] -
        agent_position[1]))
    path = [cell for cell in belief_set['map']['grid'] if 'walkable' in
        cell['cell_type']]
    if nearest_door['coordinates'] in [cell['cell_coordinates'] for cell in
        path]:
        while agent_position != nearest_door['coordinates']:
            if agent_position[0] > nearest_door['coordinates'][0]:
                function_1()
                agent_position[0] -= 1
            elif agent_position[0] < nearest_door['coordinates'][0]:
                function_2()
                agent_position[0] += 1
            if agent_position[1] > nearest_door['coordinates'][1]:
                function_3()
                agent_position[1] -= 1
            elif agent_position[1] < nearest_door['coordinates'][1]:
                function_4()
                agent_position[1] += 1

def function_10():
    global belief_set
    if belief_set['agent']['coordinates'] == belief_set['parcels'][1][
        'coordinates']:
        function_5()
    elif belief_set['agent']['coordinates'][0] < belief_set['parcels'][1][
        'coordinates'][0]:
        function_2()
    elif belief_set['agent']['coordinates'][0] > belief_set['parcels'][1][
        'coordinates'][0]:
        function_1()
    elif belief_set['agent']['coordinates'][1] < belief_set['parcels'][1][
        'coordinates'][1]:
        function_4()
    elif belief_set['agent']['coordinates'][1] > belief_set['parcels'][1][
        'coordinates'][1]:
        function_3()
    else:
        function_2()

def function_11():
    global belief_set
    agent_coordinates = belief_set['agent']['coordinates']
    parcel_coordinates = belief_set['parcels'][1]['coordinates']
    delivery_cell_coordinates = [cell['cell_coordinates'] for cell in
        belief_set['map']['grid'] if cell['cell_type'] in ['delivery_cell',
        'double_delivery_cell']][0]
    while agent_coordinates != parcel_coordinates:
        if parcel_coordinates[0] < agent_coordinates[0]:
            function_1()
        elif parcel_coordinates[0] > agent_coordinates[0]:
            function_2()
        elif parcel_coordinates[1] < agent_coordinates[1]:
            function_3()
        elif parcel_coordinates[1] > agent_coordinates[1]:
            function_4()
        agent_coordinates = belief_set['agent']['coordinates']
    function_5()
    while agent_coordinates != delivery_cell_coordinates:
        if delivery_cell_coordinates[0] < agent_coordinates[0]:
            function_1()
        elif delivery_cell_coordinates[0] > agent_coordinates[0]:
            function_2()
        elif delivery_cell_coordinates[1] < agent_coordinates[1]:
            function_3()
        elif delivery_cell_coordinates[1] > agent_coordinates[1]:
            function_4()
        agent_coordinates = belief_set['agent']['coordinates']

def function_12():
    global belief_set
    agent_coords = belief_set['agent']['coordinates']
    delivery_coords = [cell['cell_coordinates'] for cell in belief_set[
        'map']['grid'] if 'delivery' in cell['cell_type']]
    if delivery_coords[0][0] > agent_coords[0]:
        function_2()
    elif delivery_coords[0][0] < agent_coords[0]:
        function_1()
    elif delivery_coords[0][1] > agent_coords[1]:
        function_4()
    elif delivery_coords[0][1] < agent_coords[1]:
        function_3()
    else:
        function_6()

