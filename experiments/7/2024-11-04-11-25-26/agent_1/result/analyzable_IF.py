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
    agent = belief_set['agent'][1]
    map = belief_set['map']['grid']
    unvisited_cells = [cell for cell in map if cell['cell_type'] in [
        'parcels_spawn', 'batteries_spawn', 'delivery_cell'] and cell[
        'cell_coordinates'] != agent['coordinates']]
    if not unvisited_cells:
        return
    nearest_cell = min(unvisited_cells, key=lambda cell: abs(cell[
        'cell_coordinates'][0] - agent['coordinates'][0]) + abs(cell[
        'cell_coordinates'][1] - agent['coordinates'][1]))
    if nearest_cell['cell_coordinates'][0] < agent['coordinates'][0]:
        function_1()
    elif nearest_cell['cell_coordinates'][0] > agent['coordinates'][0]:
        function_2()
    elif nearest_cell['cell_coordinates'][1] < agent['coordinates'][1]:
        function_3()
    elif nearest_cell['cell_coordinates'][1] > agent['coordinates'][1]:
        function_4()

def function_8():
    global belief_set
    agent_id = 1
    agent_position = belief_set['agent'][agent_id]['coordinates']
    parcels = [parcel for parcel in belief_set['parcels'] if parcel[
        'carried_by_id'] == None and parcel['coordinates'] == agent_position]
    if parcels:
        function_5()
    else:
        function_7()

def function_9():
    global belief_set
    function_7()
    function_5()

def function_10():
    global belief_set
    function_7()
    for cell in belief_set['map']['grid']:
        if cell['cell_coordinates'] == belief_set['agent'][1]['coordinates'
            ] and 'spawn' in cell['cell_type']:
            function_5()
    return

def function_11():
    global belief_set
    agent = belief_set['agent'][1]
    key = belief_set['keys'][0]
    door = belief_set['doors'][0]
    while agent['coordinates'] != key['coordinates']:
        if agent['coordinates'][0] < key['coordinates'][0]:
            function_2()
        elif agent['coordinates'][0] > key['coordinates'][0]:
            function_1()
        elif agent['coordinates'][1] < key['coordinates'][1]:
            function_4()
        elif agent['coordinates'][1] > key['coordinates'][1]:
            function_3()
    function_5()
    while agent['coordinates'] != door['coordinates']:
        if agent['coordinates'][0] < door['coordinates'][0]:
            function_2()
        elif agent['coordinates'][0] > door['coordinates'][0]:
            function_1()
        elif agent['coordinates'][1] < door['coordinates'][1]:
            function_4()
        elif agent['coordinates'][1] > door['coordinates'][1]:
            function_3()
    function_5()

def function_12():
    global belief_set
    agent_coordinates = belief_set['agent'][1]['coordinates']
    battery_coordinates = belief_set['batteries'][0]['coordinates']
    delivery_coordinates = [i['cell_coordinates'] for i in belief_set['map'
        ]['grid'] if i['cell_type'] == 'delivery_cell'][0]
    while agent_coordinates != battery_coordinates:
        if agent_coordinates[0] < battery_coordinates[0]:
            function_2()
        elif agent_coordinates[0] > battery_coordinates[0]:
            function_1()
        elif agent_coordinates[1] < battery_coordinates[1]:
            function_4()
        elif agent_coordinates[1] > battery_coordinates[1]:
            function_3()
        agent_coordinates = belief_set['agent'][1]['coordinates']
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
        agent_coordinates = belief_set['agent'][1]['coordinates']
    function_6()

def function_13():
    global belief_set
    agent = belief_set['agent'][1]
    batteries = belief_set['batteries']
    delivery_cell = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'delivery_cell'][0]
    max_movements = 10
    movement_count = 0
    while agent['coordinates'] != batteries[0]['coordinates'
        ] and movement_count < max_movements:
        if agent['coordinates'][0] > batteries[0]['coordinates'][0
            ] and belief_set['map']['grid'][agent['coordinates'][0] - 1][agent
            ['coordinates'][1]]['cell_type'] != 'non_walkable':
            function_1()
        elif agent['coordinates'][0] < batteries[0]['coordinates'][0
            ] and belief_set['map']['grid'][agent['coordinates'][0] + 1][agent
            ['coordinates'][1]]['cell_type'] != 'non_walkable':
            function_2()
        elif agent['coordinates'][1] > batteries[0]['coordinates'][1
            ] and belief_set['map']['grid'][agent['coordinates'][0]][agent[
            'coordinates'][1] - 1]['cell_type'] != 'non_walkable':
            function_3()
        elif agent['coordinates'][1] < batteries[0]['coordinates'][1
            ] and belief_set['map']['grid'][agent['coordinates'][0]][agent[
            'coordinates'][1] + 1]['cell_type'] != 'non_walkable':
            function_4()
        agent['coordinates'] = [agent['coordinates'][0] + i[0], agent[
            'coordinates'][1] + i[1]]
        movement_count += 1
    if agent['coordinates'] == batteries[0]['coordinates']:
        function_5()
    while agent['coordinates'] != delivery_cell['cell_coordinates'
        ] and movement_count < max_movements:
        if agent['coordinates'][0] > delivery_cell['cell_coordinates'][0
            ] and belief_set['map']['grid'][agent['coordinates'][0] - 1][agent
            ['coordinates'][1]]['cell_type'] != 'non_walkable':
            function_1()
        elif agent['coordinates'][0] < delivery_cell['cell_coordinates'][0
            ] and belief_set['map']['grid'][agent['coordinates'][0] + 1][agent
            ['coordinates'][1]]['cell_type'] != 'non_walkable':
            function_2()
        elif agent['coordinates'][1] > delivery_cell['cell_coordinates'][1
            ] and belief_set['map']['grid'][agent['coordinates'][0]][agent[
            'coordinates'][1] - 1]['cell_type'] != 'non_walkable':
            function_3()
        elif agent['coordinates'][1] < delivery_cell['cell_coordinates'][1
            ] and belief_set['map']['grid'][agent['coordinates'][0]][agent[
            'coordinates'][1] + 1]['cell_type'] != 'non_walkable':
            function_4()
        agent['coordinates'] = [agent['coordinates'][0] + i[0], agent[
            'coordinates'][1] + i[1]]
        movement_count += 1
    if agent['coordinates'] == delivery_cell['cell_coordinates']:
        function_6()

def function_14():
    global belief_set
    agent = belief_set['agent'][1]
    parcels = belief_set['parcels']
    for parcel in parcels:
        if parcel['carried_by_id'] is None:
            parcel_coords = parcel['coordinates']
            while agent['coordinates'] != parcel_coords:
                if agent['coordinates'][0] < parcel_coords[0]:
                    function_2()
                elif agent['coordinates'][0] > parcel_coords[0]:
                    function_1()
                elif agent['coordinates'][1] < parcel_coords[1]:
                    function_4()
                elif agent['coordinates'][1] > parcel_coords[1]:
                    function_3()
            function_5()
            break

def function_15():
    global belief_set
    agent = belief_set['agent'][1]
    parcels = belief_set['parcels']
    map_grid = belief_set['map']['grid']
    max_iterations = belief_set['map']['width'] * belief_set['map']['height']
    iterations = 0
    while iterations < max_iterations:
        for parcel in parcels:
            if parcel['carried_by_id'] is None:
                parcel_coordinates = parcel['coordinates']
                for cell in map_grid:
                    if cell['cell_coordinates'] == parcel_coordinates and cell[
                        'cell_type'] == 'walkable':
                        if agent['coordinates'][0] < parcel_coordinates[0]:
                            function_2()
                        elif agent['coordinates'][0] > parcel_coordinates[0]:
                            function_1()
                        elif agent['coordinates'][1] < parcel_coordinates[1]:
                            function_4()
                        elif agent['coordinates'][1] > parcel_coordinates[1]:
                            function_3()
                        elif agent['coordinates'] == parcel_coordinates:
                            function_5()
                            return
        iterations += 1

def function_16():
    global belief_set
    agent = belief_set['agent'][1]
    parcels = belief_set['parcels']
    batteries = belief_set['batteries']
    nearest_parcel = min(parcels, key=lambda x: abs(x['coordinates'][0] -
        agent['coordinates'][0]) + abs(x['coordinates'][1] - agent[
        'coordinates'][1]))
    while agent['coordinates'] != nearest_parcel['coordinates']:
        if agent['coordinates'][0] < nearest_parcel['coordinates'][0]:
            function_2()
        elif agent['coordinates'][0] > nearest_parcel['coordinates'][0]:
            function_1()
        elif agent['coordinates'][1] < nearest_parcel['coordinates'][1]:
            function_4()
        else:
            function_3()
    function_5()
    if agent['energy'] < 20:
        nearest_battery = min(batteries, key=lambda x: abs(x['coordinates']
            [0] - agent['coordinates'][0]) + abs(x['coordinates'][1] -
            agent['coordinates'][1]))
        while agent['coordinates'] != nearest_battery['coordinates']:
            if agent['coordinates'][0] < nearest_battery['coordinates'][0]:
                function_2()
            elif agent['coordinates'][0] > nearest_battery['coordinates'][0]:
                function_1()
            elif agent['coordinates'][1] < nearest_battery['coordinates'][1]:
                function_4()
            else:
                function_3()
        function_5()

def function_17():
    global belief_set
    for cell in belief_set['map']['grid']:
        if cell['cell_type'] == 'parcels_spawn':
            parcel_spawn_coordinates = cell['cell_coordinates']
    agent_coordinates = belief_set['agent'][1]['coordinates']
    while agent_coordinates != parcel_spawn_coordinates:
        if agent_coordinates[0] < parcel_spawn_coordinates[0]:
            function_2()
        elif agent_coordinates[0] > parcel_spawn_coordinates[0]:
            function_1()
        elif agent_coordinates[1] < parcel_spawn_coordinates[1]:
            function_4()
        elif agent_coordinates[1] > parcel_spawn_coordinates[1]:
            function_3()
        agent_coordinates = belief_set['agent'][1]['coordinates']
    function_5()

def function_18():
    global belief_set
    delivery_cell = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'delivery_cell']
    agent = belief_set['agent'][1]
    while agent['coordinates'] != delivery_cell[0]['cell_coordinates']:
        if agent['coordinates'][0] < delivery_cell[0]['cell_coordinates'][0]:
            function_2()
        elif agent['coordinates'][0] > delivery_cell[0]['cell_coordinates'][0]:
            function_1()
        elif agent['coordinates'][1] < delivery_cell[0]['cell_coordinates'][1]:
            function_4()
        elif agent['coordinates'][1] > delivery_cell[0]['cell_coordinates'][1]:
            function_3()
    function_6()

def function_19():
    global belief_set
    MAX_ITERATIONS = 1000
    iteration = 0
    delivery_cell = [c['cell_coordinates'] for c in belief_set['map'][
        'grid'] if c['cell_type'] == 'delivery_cell'][0]
    while belief_set['agent'][1]['coordinates'
        ] != delivery_cell and iteration < MAX_ITERATIONS:
        x_diff = belief_set['agent'][1]['coordinates'][0] - delivery_cell[0]
        y_diff = belief_set['agent'][1]['coordinates'][1] - delivery_cell[1]
        if x_diff > 0:
            function_1()
        elif x_diff < 0:
            function_2()
        if y_diff > 0:
            function_3()
        elif y_diff < 0:
            function_4()
        iteration += 1
    function_6()

def function_20():
    global belief_set
    agent = belief_set['agent'][1]
    battery_spawn = next(cell for cell in belief_set['map']['grid'] if cell
        ['cell_type'] == 'batteries_spawn')
    while agent['coordinates'] != battery_spawn['cell_coordinates']:
        if agent['coordinates'][0] < battery_spawn['cell_coordinates'][0]:
            function_2()
        elif agent['coordinates'][0] > battery_spawn['cell_coordinates'][0]:
            function_1()
        elif agent['coordinates'][1] < battery_spawn['cell_coordinates'][1]:
            function_4()
        elif agent['coordinates'][1] > battery_spawn['cell_coordinates'][1]:
            function_3()
    function_5()

def function_21():
    global belief_set
    battery_spawn = [cell['cell_coordinates'] for cell in belief_set['map']
        ['grid'] if cell['cell_type'] == 'batteries_spawn'][0]
    agent_pos = belief_set['agent'][1]['coordinates']
    while True:
        if agent_pos[0] > battery_spawn[0]:
            function_1()
        elif agent_pos[0] < battery_spawn[0]:
            function_2()
        elif agent_pos[1] > battery_spawn[1]:
            function_3()
        elif agent_pos[1] < battery_spawn[1]:
            function_4()
        agent_pos = belief_set['agent'][1]['coordinates']
        if agent_pos == battery_spawn:
            function_5()
            break

def function_22():
    global belief_set
    while True:
        if belief_set['agent'][1]['energy'] < 50:
            function_21()
        elif len(belief_set['agent'][1]['parcels_carried_ids']) == 0:
            function_17()
        else:
            function_19()

def function_23():
    global belief_set
    counter = 0
    while True:
        counter += 1
        if counter > 100:
            break
        if belief_set['agent'][1]['energy'] < 50:
            function_21()
            continue
        if len(belief_set['agent'][1]['parcels_carried_ids']) > 0:
            function_19()
        else:
            function_17()

def function_24():
    global belief_set
    while True:
        if belief_set['agent'][1]['energy'] < 50:
            function_21()
        elif len(belief_set['agent'][1]['parcels_carried_ids']) == 0:
            function_17()
        else:
            function_19()
        if belief_set['agent'][1]['score'] == belief_set['agent'][1]['score']:
            break

