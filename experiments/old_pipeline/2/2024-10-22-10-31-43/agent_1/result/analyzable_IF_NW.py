def function_7():
    global belief_set
    target = belief_set['parcel'][1]['coordinates']
    agent_position = belief_set['agent'][1]['coordinates']
    while agent_position != target:
        if agent_position[0] < target[0] and belief_set['map']['grid'][
            agent_position[0] + 1][agent_position[1]]['cell_type'
            ] == 'walkable':
            function_2()
        elif agent_position[0] > target[0] and belief_set['map']['grid'][
            agent_position[0] - 1][agent_position[1]]['cell_type'
            ] == 'walkable':
            function_1()
        elif agent_position[1] < target[1] and belief_set['map']['grid'][
            agent_position[0]][agent_position[1] + 1]['cell_type'
            ] == 'walkable':
            function_4()
        elif agent_position[1] > target[1] and belief_set['map']['grid'][
            agent_position[0]][agent_position[1] - 1]['cell_type'
            ] == 'walkable':
            function_3()
    function_5()

def function_8():
    global belief_set
    agent_coordinates = belief_set['agent'][1]['coordinates']
    parcel_coordinates = belief_set['parcel'][1]['coordinates']
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

def function_10():
    global belief_set
    while belief_set['agent'][1]['coordinates'] != belief_set['map']['grid'][7
        ]['cell_coordinates']:
        if belief_set['agent'][1]['coordinates'][0] < belief_set['map']['grid'
            ][7]['cell_coordinates'][0]:
            function_2()
        elif belief_set['agent'][1]['coordinates'][0] > belief_set['map'][
            'grid'][7]['cell_coordinates'][0]:
            function_1()
        elif belief_set['agent'][1]['coordinates'][1] < belief_set['map'][
            'grid'][7]['cell_coordinates'][1]:
            function_4()
        elif belief_set['agent'][1]['coordinates'][1] > belief_set['map'][
            'grid'][7]['cell_coordinates'][1]:
            function_3()
    function_6()

def function_11():
    global belief_set
    agent = belief_set['agent'][1]
    parcel = belief_set['parcel'][1]
    while agent['coordinates'] != [1, 3]:
        if agent['coordinates'][0] < 1:
            function_2()
        elif agent['coordinates'][0] > 1:
            function_1()
        elif agent['coordinates'][1] < 3:
            function_4()
        elif agent['coordinates'][1] > 3:
            function_3()
    function_6()

def function_12():
    global belief_set
    agent_coordinates = belief_set['agent'][1]['coordinates']
    delivery_coordinates = [item['cell_coordinates'] for item in belief_set
        ['map']['grid'] if item['cell_type'] == 'delivery_cell'][0]
    if agent_coordinates[0] > delivery_coordinates[0]:
        function_1()
    elif agent_coordinates[0] < delivery_coordinates[0]:
        function_2()
    elif agent_coordinates[1] > delivery_coordinates[1]:
        function_3()
    elif agent_coordinates[1] < delivery_coordinates[1]:
        function_4()
    if agent_coordinates == delivery_coordinates:
        function_6()

def function_15():
    global belief_set
    function_13()
    if belief_set['agent'][1]['coordinates'] == belief_set['door'][1][
        'coordinates'] and belief_set['agent'][1]['has_key']:
        function_5()
    else:
        function_1()
        function_3()
    function_9()
    function_14()

def function_16():
    global belief_set
    agent_coords = belief_set['agent'][1]['coordinates']
    parcel_spawn_coords = [cell['cell_coordinates'] for cell in belief_set[
        'map']['grid'] if cell['cell_type'] == 'parcels_spawn'][0]
    delivery_coords = [cell['cell_coordinates'] for cell in belief_set[
        'map']['grid'] if cell['cell_type'] == 'delivery_cell'][0]
    while agent_coords != parcel_spawn_coords:
        if parcel_spawn_coords[0] < agent_coords[0]:
            function_1()
        elif parcel_spawn_coords[0] > agent_coords[0]:
            function_2()
        elif parcel_spawn_coords[1] < agent_coords[1]:
            function_3()
        elif parcel_spawn_coords[1] > agent_coords[1]:
            function_4()
        agent_coords = belief_set['agent'][1]['coordinates']
    function_5()
    while agent_coords != delivery_coords:
        if delivery_coords[0] < agent_coords[0]:
            function_1()
        elif delivery_coords[0] > agent_coords[0]:
            function_2()
        elif delivery_coords[1] < agent_coords[1]:
            function_3()
        elif delivery_coords[1] > agent_coords[1]:
            function_4()
        agent_coords = belief_set['agent'][1]['coordinates']
    function_6()

def function_17():
    global belief_set
    if not belief_set['agent'][1]['parcels_carried_ids']:
        function_9()
    if belief_set['agent'][1]['coordinates'] != [1, 3]:
        while belief_set['agent'][1]['coordinates'][1] != 3:
            function_4()
    function_14()
    while belief_set['agent'][1]['coordinates'][1] != 0:
        function_3()

