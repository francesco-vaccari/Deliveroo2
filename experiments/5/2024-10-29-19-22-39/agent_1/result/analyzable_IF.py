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
    spawn_location = [cell['cell_coordinates'] for cell in belief_set['map'
        ]['grid'] if cell['cell_type'] == 'parcels_spawn'][0]
    while belief_set['agent'][1]['coordinates'] != spawn_location:
        if belief_set['agent'][1]['coordinates'][0] > spawn_location[0]:
            function_1()
        elif belief_set['agent'][1]['coordinates'][0] < spawn_location[0]:
            function_2()
        if belief_set['agent'][1]['coordinates'][1] > spawn_location[1]:
            function_3()
        elif belief_set['agent'][1]['coordinates'][1] < spawn_location[1]:
            function_4()
    function_5()

def function_8():
    global belief_set
    delivery_cell = next(cell for cell in belief_set['map']['grid'] if cell
        ['cell_type'] == 'delivery_cell')
    agent = belief_set['agent'][1]
    while agent['coordinates'] != delivery_cell['cell_coordinates']:
        if agent['coordinates'][0] < delivery_cell['cell_coordinates'][0] and [
            agent['coordinates'][0] + 1, agent['coordinates'][1]] not in [cell
            ['cell_coordinates'] for cell in belief_set['map']['grid'] if 
            cell['cell_type'] == 'non_walkable']:
            function_2()
        elif agent['coordinates'][0] > delivery_cell['cell_coordinates'][0
            ] and [agent['coordinates'][0] - 1, agent['coordinates'][1]
            ] not in [cell['cell_coordinates'] for cell in belief_set['map'
            ]['grid'] if cell['cell_type'] == 'non_walkable']:
            function_1()
        elif agent['coordinates'][1] < delivery_cell['cell_coordinates'][1
            ] and [agent['coordinates'][0], agent['coordinates'][1] + 1
            ] not in [cell['cell_coordinates'] for cell in belief_set['map'
            ]['grid'] if cell['cell_type'] == 'non_walkable']:
            function_4()
        elif agent['coordinates'][1] > delivery_cell['cell_coordinates'][1
            ] and [agent['coordinates'][0], agent['coordinates'][1] - 1
            ] not in [cell['cell_coordinates'] for cell in belief_set['map'
            ]['grid'] if cell['cell_type'] == 'non_walkable']:
            function_3()
    function_6()

def function_9():
    global belief_set
    max_attempts = 10
    attempts = 0
    while attempts < max_attempts and belief_set['agent'][1][
        'parcels_carried_ids']:
        coordinates = belief_set['agent'][1]['coordinates']
        if [coordinates[0] + 1, coordinates[1]] in [item['cell_coordinates'
            ] for item in belief_set['map']['grid'] if item['cell_type'] ==
            'walkable']:
            function_2()
        elif [coordinates[0], coordinates[1] + 1] in [item[
            'cell_coordinates'] for item in belief_set['map']['grid'] if 
            item['cell_type'] == 'walkable']:
            function_4()
        elif [coordinates[0] - 1, coordinates[1]] in [item[
            'cell_coordinates'] for item in belief_set['map']['grid'] if 
            item['cell_type'] == 'walkable']:
            function_1()
        elif [coordinates[0], coordinates[1] - 1] in [item[
            'cell_coordinates'] for item in belief_set['map']['grid'] if 
            item['cell_type'] == 'walkable']:
            function_3()
        attempts += 1
    if belief_set['agent'][1]['coordinates'] in [item['cell_coordinates'] for
        item in belief_set['map']['grid'] if item['cell_type'] ==
        'delivery_cell'] and belief_set['agent'][1]['parcels_carried_ids']:
        function_6()

def function_10():
    global belief_set
    agent = belief_set['agent'][1]
    map_grid = belief_set['map']['grid']
    non_walkable_cells = [cell for cell in map_grid if cell['cell_type'] ==
        'non_walkable']
    delivery_cell = [cell for cell in map_grid if cell['cell_type'] ==
        'delivery_cell'][0]
    parcels_spawn_cell = [cell for cell in map_grid if cell['cell_type'] ==
        'parcels_spawn'][0]
    path_to_delivery = a_star_pathfinding(agent['coordinates'],
        delivery_cell['cell_coordinates'], non_walkable_cells)
    if path_to_delivery is not None:
        for step in path_to_delivery:
            if step[0] < agent['coordinates'][0]:
                function_1()
            elif step[0] > agent['coordinates'][0]:
                function_2()
            elif step[1] < agent['coordinates'][1]:
                function_3()
            else:
                function_4()
        function_6()
    path_to_spawn = a_star_pathfinding(agent['coordinates'],
        parcels_spawn_cell['cell_coordinates'], non_walkable_cells)
    if path_to_spawn is not None:
        for step in path_to_spawn:
            if step[0] < agent['coordinates'][0]:
                function_1()
            elif step[0] > agent['coordinates'][0]:
                function_2()
            elif step[1] < agent['coordinates'][1]:
                function_3()
            else:
                function_4()
    function_5()

def function_11():
    global belief_set
    agent = belief_set['agent'][1]
    delivery_cell = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'delivery_cell'][0]
    if agent['coordinates'][0] < delivery_cell['cell_coordinates'][0]:
        function_2()
    elif agent['coordinates'][0] > delivery_cell['cell_coordinates'][0]:
        function_1()
    elif agent['coordinates'][1] < delivery_cell['cell_coordinates'][1]:
        function_4()
    elif agent['coordinates'][1] > delivery_cell['cell_coordinates'][1]:
        function_3()
    else:
        function_6()

def function_12():
    global belief_set
    spawn_location = [cell['cell_coordinates'] for cell in belief_set['map'
        ]['grid'] if cell['cell_type'] == 'parcels_spawn'][0]
    delivery_location = [cell['cell_coordinates'] for cell in belief_set[
        'map']['grid'] if cell['cell_type'] == 'delivery_cell'][0]
    agent_location = belief_set['agent'][1]['coordinates']
    while agent_location != spawn_location:
        if agent_location[0] > spawn_location[0]:
            function_1()
        elif agent_location[0] < spawn_location[0]:
            function_2()
        if agent_location[1] > spawn_location[1]:
            function_3()
        elif agent_location[1] < spawn_location[1]:
            function_4()
        agent_location = belief_set['agent'][1]['coordinates']
    function_5()
    while agent_location != delivery_location:
        if agent_location[0] > delivery_location[0]:
            function_1()
        elif agent_location[0] < delivery_location[0]:
            function_2()
        if agent_location[1] > delivery_location[1]:
            function_3()
        elif agent_location[1] < delivery_location[1]:
            function_4()
        agent_location = belief_set['agent'][1]['coordinates']
    function_6()

def function_13():
    global belief_set
    function_7()
    function_5()
    function_12()

def function_14():
    global belief_set
    if belief_set['agent'][1]['coordinates'] != [0, 0]:
        function_1()
    function_5()
    while belief_set['agent'][1]['coordinates'] != [1, 3]:
        function_4()
    function_6()

def function_15():
    global belief_set
    parcel_spawn = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'parcels_spawn'][0]['cell_coordinates']
    delivery_cell = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'delivery_cell'][0]['cell_coordinates']
    agent_coordinates = belief_set['agent'][1]['coordinates']
    while agent_coordinates != parcel_spawn:
        if agent_coordinates[0] < parcel_spawn[0]:
            function_2()
            agent_coordinates[0] += 1
        elif agent_coordinates[0] > parcel_spawn[0]:
            function_1()
            agent_coordinates[0] -= 1
        elif agent_coordinates[1] < parcel_spawn[1]:
            function_4()
            agent_coordinates[1] += 1
        elif agent_coordinates[1] > parcel_spawn[1]:
            function_3()
            agent_coordinates[1] -= 1
    function_5()
    while agent_coordinates != delivery_cell:
        if agent_coordinates[0] < delivery_cell[0]:
            function_2()
            agent_coordinates[0] += 1
        elif agent_coordinates[0] > delivery_cell[0]:
            function_1()
            agent_coordinates[0] -= 1
        elif agent_coordinates[1] < delivery_cell[1]:
            function_4()
            agent_coordinates[1] += 1
        elif agent_coordinates[1] > delivery_cell[1]:
            function_3()
            agent_coordinates[1] -= 1
    function_6()

