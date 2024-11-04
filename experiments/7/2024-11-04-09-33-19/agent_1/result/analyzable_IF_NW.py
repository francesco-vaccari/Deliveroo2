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

