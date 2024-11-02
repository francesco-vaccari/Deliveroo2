def function_7():
    global belief_set
    agent = belief_set['agent'][1]
    parcel_spawn = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'parcels_spawn'][0]
    delivery_cell = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'delivery_cell'][0]
    while agent['coordinates'] != parcel_spawn['cell_coordinates']:
        if agent['coordinates'][0] < parcel_spawn['cell_coordinates'][0]:
            function_2()
        elif agent['coordinates'][0] > parcel_spawn['cell_coordinates'][0]:
            function_1()
        elif agent['coordinates'][1] < parcel_spawn['cell_coordinates'][1]:
            function_4()
        elif agent['coordinates'][1] > parcel_spawn['cell_coordinates'][1]:
            function_3()
    function_5()
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

def function_9():
    global belief_set
    agent = belief_set['agent'][1]
    parcels_spawn = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'parcels_spawn'][0]
    delivery_cell = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'delivery_cell'][0]
    while agent['coordinates'] != parcels_spawn['cell_coordinates']:
        if agent['coordinates'][0] > parcels_spawn['cell_coordinates'][0]:
            function_1()
        elif agent['coordinates'][0] < parcels_spawn['cell_coordinates'][0]:
            function_2()
        elif agent['coordinates'][1] > parcels_spawn['cell_coordinates'][1]:
            function_3()
        elif agent['coordinates'][1] < parcels_spawn['cell_coordinates'][1]:
            function_4()
    function_5()
    while agent['coordinates'] != delivery_cell['cell_coordinates']:
        if agent['coordinates'][0] > delivery_cell['cell_coordinates'][0]:
            function_1()
        elif agent['coordinates'][0] < delivery_cell['cell_coordinates'][0]:
            function_2()
        elif agent['coordinates'][1] > delivery_cell['cell_coordinates'][1]:
            function_3()
        elif agent['coordinates'][1] < delivery_cell['cell_coordinates'][1]:
            function_4()
    function_6()

def function_10():
    global belief_set
    max_moves = 100
    moves = 0
    while moves < max_moves:
        if belief_set['agent'][1]['coordinates'] == [0, 0]:
            function_5()
            moves += 1
        elif belief_set['agent'][1]['coordinates'][1] > 0:
            function_3()
            moves += 1
        elif belief_set['agent'][1]['coordinates'][0] > 0:
            function_1()
            moves += 1
        elif belief_set['agent'][1]['coordinates'] == [1, 3]:
            function_6()
            moves += 1
        elif belief_set['agent'][1]['coordinates'][1] < 3:
            function_4()
            moves += 1
        elif belief_set['agent'][1]['coordinates'][0] < 1:
            function_2()
            moves += 1
    if moves == max_moves:
        return 'Max moves reached, goal not achieved'

def function_11():
    global belief_set
    agent = belief_set['agent'][1]
    parcels = belief_set['parcels']
    map_grid = belief_set['map']['grid']
    delivery_cell = [cell for cell in map_grid if cell['cell_type'] ==
        'delivery_cell'][0]
    while True:
        if not agent['parcels_carried_ids']:
            function_5()
            if agent['parcels_carried_ids']:
                continue
        if agent['coordinates'][0] > delivery_cell['cell_coordinates'][0]:
            function_1()
        elif agent['coordinates'][0] < delivery_cell['cell_coordinates'][0]:
            function_2()
        if agent['coordinates'][1] > delivery_cell['cell_coordinates'][1]:
            function_3()
        elif agent['coordinates'][1] < delivery_cell['cell_coordinates'][1]:
            function_4()
        if agent['coordinates'] == delivery_cell['cell_coordinates'] and agent[
            'parcels_carried_ids']:
            function_6()
            break

def function_13():
    global belief_set
    while True:
        if belief_set['agent'][1]['coordinates'] == belief_set['parcels'][16][
            'coordinates']:
            function_5()
        elif belief_set['agent'][1]['coordinates'] == [belief_set['map'][
            'grid'][7]['cell_coordinates'][0], belief_set['map']['grid'][7]
            ['cell_coordinates'][1]]:
            function_6()
        elif belief_set['agent'][1]['coordinates'][0] > belief_set['parcels'][
            16]['coordinates'][0] and belief_set['map']['grid'][(belief_set
            ['agent'][1]['coordinates'][0] - 1) * belief_set['map']['width'
            ] + belief_set['agent'][1]['coordinates'][1]]['cell_type'
            ] == 'walkable':
            function_1()
        elif belief_set['agent'][1]['coordinates'][0] < belief_set['parcels'][
            16]['coordinates'][0] and belief_set['map']['grid'][(belief_set
            ['agent'][1]['coordinates'][0] + 1) * belief_set['map']['width'
            ] + belief_set['agent'][1]['coordinates'][1]]['cell_type'
            ] == 'walkable':
            function_2()
        elif belief_set['agent'][1]['coordinates'][1] > belief_set['parcels'][
            16]['coordinates'][1] and belief_set['map']['grid'][belief_set[
            'agent'][1]['coordinates'][0] * belief_set['map']['width'] + (
            belief_set['agent'][1]['coordinates'][1] - 1)]['cell_type'
            ] == 'walkable':
            function_3()
        elif belief_set['agent'][1]['coordinates'][1] < belief_set['parcels'][
            16]['coordinates'][1] and belief_set['map']['grid'][belief_set[
            'agent'][1]['coordinates'][0] * belief_set['map']['width'] + (
            belief_set['agent'][1]['coordinates'][1] + 1)]['cell_type'
            ] == 'walkable':
            function_4()
        else:
            break

def function_14():
    global belief_set
    max_iterations = 100
    iteration = 0
    while iteration < max_iterations:
        function_8()
        if belief_set['agent'][1]['parcels_carried_ids']:
            function_6()
        iteration += 1

def function_15():
    global belief_set
    agent = belief_set['agent'][1]
    parcels = belief_set['parcels']
    map_grid = belief_set['map']['grid']
    delivery_cell = [cell for cell in map_grid if cell['cell_type'] ==
        'delivery_cell'][0]
    agent_cell = [cell for cell in map_grid if cell['cell_coordinates'] ==
        agent['coordinates']][0]
    if not agent['parcels_carried_ids']:
        parcel_spawn = [cell for cell in map_grid if cell['cell_type'] ==
            'parcels_spawn'][0]
        if agent_cell['cell_coordinates'][0] < parcel_spawn['cell_coordinates'
            ][0]:
            function_2()
        elif agent_cell['cell_coordinates'][0] > parcel_spawn[
            'cell_coordinates'][0]:
            function_1()
        elif agent_cell['cell_coordinates'][1] < parcel_spawn[
            'cell_coordinates'][1]:
            function_4()
        elif agent_cell['cell_coordinates'][1] > parcel_spawn[
            'cell_coordinates'][1]:
            function_3()
        function_5()
    else:
        if agent_cell['cell_coordinates'][0] < delivery_cell['cell_coordinates'
            ][0]:
            function_2()
        elif agent_cell['cell_coordinates'][0] > delivery_cell[
            'cell_coordinates'][0]:
            function_1()
        elif agent_cell['cell_coordinates'][1] < delivery_cell[
            'cell_coordinates'][1]:
            function_4()
        elif agent_cell['cell_coordinates'][1] > delivery_cell[
            'cell_coordinates'][1]:
            function_3()
        function_6()

