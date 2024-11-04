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
    agent_position = belief_set['agent']['coordinates']
    key_position = belief_set['keys'][0]['coordinates']
    while agent_position[0] != key_position[0]:
        if agent_position[0] > key_position[0]:
            function_1()
        else:
            function_2()
    while agent_position[1] != key_position[1]:
        if agent_position[1] > key_position[1]:
            function_3()
        else:
            function_4()
    function_5()
    door_position = belief_set['doors'][0]['coordinates']
    while agent_position[0] != door_position[0]:
        if agent_position[0] > door_position[0]:
            function_1()
        else:
            function_2()
    while agent_position[1] != door_position[1]:
        if agent_position[1] > door_position[1]:
            function_3()
        else:
            function_4()

def function_8():
    global belief_set
    target_key = belief_set['keys'][0]['coordinates']
    target_door = belief_set['doors'][0]['coordinates']
    agent_position = belief_set['agent']['coordinates']
    max_iterations = 1000
    while agent_position != target_key and max_iterations > 0:
        if agent_position[0] < target_key[0]:
            function_2()
        elif agent_position[0] > target_key[0]:
            function_1()
        elif agent_position[1] < target_key[1]:
            function_4()
        elif agent_position[1] > target_key[1]:
            function_3()
        agent_position = belief_set['agent']['coordinates']
        max_iterations -= 1
    function_5()
    while agent_position != target_door and max_iterations > 0:
        if agent_position[0] < target_door[0]:
            function_2()
        elif agent_position[0] > target_door[0]:
            function_1()
        elif agent_position[1] < target_door[1]:
            function_4()
        elif agent_position[1] > target_door[1]:
            function_3()
        agent_position = belief_set['agent']['coordinates']
        max_iterations -= 1

def function_9():
    global belief_set
    current_coordinates = belief_set['agent']['coordinates']
    doors = belief_set['doors']
    nearest_door_coordinates = min(doors, key=lambda x: abs(x['coordinates'
        ][0] - current_coordinates[0]) + abs(x['coordinates'][1] -
        current_coordinates[1]))['coordinates']
    while current_coordinates != nearest_door_coordinates:
        if nearest_door_coordinates[0] < current_coordinates[0]:
            function_1()
        elif nearest_door_coordinates[0] > current_coordinates[0]:
            function_2()
        elif nearest_door_coordinates[1] < current_coordinates[1]:
            function_3()
        else:
            function_4()
        current_coordinates = belief_set['agent']['coordinates']
    function_7()
    parcels = belief_set['parcels']
    nearest_parcel_coordinates = min(parcels, key=lambda x: abs(x[
        'coordinates'][0] - current_coordinates[0]) + abs(x['coordinates'][
        1] - current_coordinates[1]))['coordinates']
    while current_coordinates != nearest_parcel_coordinates:
        if nearest_parcel_coordinates[0] < current_coordinates[0]:
            function_1()
        elif nearest_parcel_coordinates[0] > current_coordinates[0]:
            function_2()
        elif nearest_parcel_coordinates[1] < current_coordinates[1]:
            function_3()
        else:
            function_4()
        current_coordinates = belief_set['agent']['coordinates']
    function_5()

def function_10():
    global belief_set
    agent = belief_set['agent']
    delivery_cell = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'delivery_cell'][0]['cell_coordinates']
    if agent['parcels_carried_ids'] and agent['energy'] > 0:
        if agent['coordinates'][0] < delivery_cell[0]:
            function_2()
        elif agent['coordinates'][0] > delivery_cell[0]:
            function_1()
        elif agent['coordinates'][1] < delivery_cell[1]:
            function_4()
        elif agent['coordinates'][1] > delivery_cell[1]:
            function_3()

def function_11():
    global belief_set
    for parcel in belief_set['parcels']:
        if parcel['carried_by_id'] is None:
            target_coordinates = parcel['coordinates']
            break
    x_diff = belief_set['agent']['coordinates'][0] - target_coordinates[0]
    y_diff = belief_set['agent']['coordinates'][1] - target_coordinates[1]
    if x_diff > 0:
        for _ in range(x_diff):
            function_1()
    elif x_diff < 0:
        for _ in range(-x_diff):
            function_2()
    if y_diff > 0:
        for _ in range(y_diff):
            function_3()
    elif y_diff < 0:
        for _ in range(-y_diff):
            function_4()
    function_5()

def function_12():
    global belief_set
    delivery_cell = [cell['cell_coordinates'] for cell in belief_set['map']
        ['grid'] if cell['cell_type'] == 'delivery_cell'][0]
    agent_coords = belief_set['agent']['coordinates']
    while agent_coords != delivery_cell:
        if agent_coords[0] < delivery_cell[0]:
            function_2()
        elif agent_coords[0] > delivery_cell[0]:
            function_1()
        elif agent_coords[1] < delivery_cell[1]:
            function_4()
        elif agent_coords[1] > delivery_cell[1]:
            function_3()
        agent_coords = belief_set['agent']['coordinates']
    function_6()

def function_13():
    global belief_set
    agent = belief_set['agent']
    batteries = belief_set['batteries']
    closest_battery = min(batteries, key=lambda battery: abs(battery[
        'coordinates'][0] - agent['coordinates'][0]) + abs(battery[
        'coordinates'][1] - agent['coordinates'][1]))
    while agent['coordinates'][0] < closest_battery['coordinates'][0]:
        function_2()
    while agent['coordinates'][0] > closest_battery['coordinates'][0]:
        function_1()
    while agent['coordinates'][1] < closest_battery['coordinates'][1]:
        function_4()
    while agent['coordinates'][1] > closest_battery['coordinates'][1]:
        function_3()
    function_5()

def function_14():
    global belief_set
    battery_coords = belief_set['batteries'][0]['coordinates']
    while belief_set['agent']['coordinates'] != battery_coords:
        if belief_set['agent']['coordinates'][0] < battery_coords[0]:
            function_2()
        elif belief_set['agent']['coordinates'][0] > battery_coords[0]:
            function_1()
        elif belief_set['agent']['coordinates'][1] < battery_coords[1]:
            function_4()
        elif belief_set['agent']['coordinates'][1] > battery_coords[1]:
            function_3()
    function_5()

def function_15():
    global belief_set
    while belief_set['agent']['coordinates'] != [0, 0]:
        if belief_set['agent']['coordinates'][0] > 0:
            function_1()
        else:
            function_3()
    function_5()
    while belief_set['agent']['coordinates'] != [1, 3]:
        if belief_set['agent']['coordinates'][0] < 1:
            function_2()
        else:
            function_4()
    function_6()

