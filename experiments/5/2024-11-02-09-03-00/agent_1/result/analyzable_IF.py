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
    parcels_spawn = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'parcels_spawn'][0]
    delivery_cell = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'delivery_cell'][0]
    while agent['coordinates'] != parcels_spawn['cell_coordinates']:
        if agent['coordinates'][0] < parcels_spawn['cell_coordinates'][0]:
            function_2()
        elif agent['coordinates'][0] > parcels_spawn['cell_coordinates'][0]:
            function_1()
        if agent['coordinates'][1] < parcels_spawn['cell_coordinates'][1]:
            function_4()
        elif agent['coordinates'][1] > parcels_spawn['cell_coordinates'][1]:
            function_3()
    function_5()
    while agent['coordinates'] != delivery_cell['cell_coordinates']:
        if agent['coordinates'][0] < delivery_cell['cell_coordinates'][0]:
            function_2()
        elif agent['coordinates'][0] > delivery_cell['cell_coordinates'][0]:
            function_1()
        if agent['coordinates'][1] < delivery_cell['cell_coordinates'][1]:
            function_4()
        elif agent['coordinates'][1] > delivery_cell['cell_coordinates'][1]:
            function_3()
    function_6()

def function_8():
    global belief_set
    parcel_carrying = False
    while not parcel_carrying:
        if belief_set['agent'][1]['coordinates'] == belief_set['map']['grid'][0
            ]['cell_coordinates']:
            function_5()
            parcel_carrying = True
        elif belief_set['agent'][1]['coordinates'][0] > belief_set['map'][
            'grid'][0]['cell_coordinates'][0]:
            function_1()
        elif belief_set['agent'][1]['coordinates'][0] < belief_set['map'][
            'grid'][0]['cell_coordinates'][0]:
            function_2()
        elif belief_set['agent'][1]['coordinates'][1] > belief_set['map'][
            'grid'][0]['cell_coordinates'][1]:
            function_3()
        else:
            function_4()
    while belief_set['agent'][1]['coordinates'] != belief_set['map']['grid'][7
        ]['cell_coordinates']:
        if belief_set['agent'][1]['coordinates'][0] > belief_set['map']['grid'
            ][7]['cell_coordinates'][0]:
            function_1()
        elif belief_set['agent'][1]['coordinates'][0] < belief_set['map'][
            'grid'][7]['cell_coordinates'][0]:
            function_2()
        elif belief_set['agent'][1]['coordinates'][1] > belief_set['map'][
            'grid'][7]['cell_coordinates'][1]:
            function_3()
        else:
            function_4()
    function_6()
    return

def function_9():
    global belief_set
    parcel_coordinates = [parcel['coordinates'] for parcel in belief_set[
        'parcels'].values() if parcel['carried_by_id'] is None]
    delivery_coordinates = [cell['cell_coordinates'] for cell in belief_set
        ['map']['grid'] if cell['cell_type'] == 'delivery_cell'][0]
    agent_coordinates = belief_set['agent'][1]['coordinates']
    while agent_coordinates != parcel_coordinates[0]:
        if agent_coordinates[0] < parcel_coordinates[0][0]:
            function_2()
        elif agent_coordinates[0] > parcel_coordinates[0][0]:
            function_1()
        if agent_coordinates[1] < parcel_coordinates[0][1]:
            function_4()
        elif agent_coordinates[1] > parcel_coordinates[0][1]:
            function_3()
        agent_coordinates = belief_set['agent'][1]['coordinates']
    function_5()
    while agent_coordinates != delivery_coordinates:
        if agent_coordinates[0] < delivery_coordinates[0]:
            function_2()
        elif agent_coordinates[0] > delivery_coordinates[0]:
            function_1()
        if agent_coordinates[1] < delivery_coordinates[1]:
            function_4()
        elif agent_coordinates[1] > delivery_coordinates[1]:
            function_3()
        agent_coordinates = belief_set['agent'][1]['coordinates']
    function_6()

def function_10():
    global belief_set
    agent = belief_set['agent'][1]
    parcels = belief_set['parcels']
    map_grid = belief_set['map']['grid']
    spawn_cells = [cell for cell in map_grid if cell['cell_type'] ==
        'parcels_spawn']
    delivery_cells = [cell for cell in map_grid if cell['cell_type'] ==
        'delivery_cell']
    if len(agent['parcels_carried_ids']) == 0:
        for cell in spawn_cells:
            while agent['coordinates'] != cell['cell_coordinates']:
                if agent['coordinates'][0] > cell['cell_coordinates'][0]:
                    function_1()
                elif agent['coordinates'][0] < cell['cell_coordinates'][0]:
                    function_2()
                elif agent['coordinates'][1] > cell['cell_coordinates'][1]:
                    function_3()
                elif agent['coordinates'][1] < cell['cell_coordinates'][1]:
                    function_4()
            function_5()
    else:
        for cell in delivery_cells:
            while agent['coordinates'] != cell['cell_coordinates']:
                if agent['coordinates'][0] > cell['cell_coordinates'][0]:
                    function_1()
                elif agent['coordinates'][0] < cell['cell_coordinates'][0]:
                    function_2()
                elif agent['coordinates'][1] > cell['cell_coordinates'][1]:
                    function_3()
                elif agent['coordinates'][1] < cell['cell_coordinates'][1]:
                    function_4()
            function_6()

def function_11():
    global belief_set
    max_iterations = 100
    iteration_count = 0
    agent_id = 1
    while iteration_count < max_iterations:
        agent_coords = belief_set['agent'][agent_id]['coordinates']
        parcel_spawn_coords = [cell['cell_coordinates'] for cell in
            belief_set['map']['grid'] if cell['cell_type'] == 'parcels_spawn'][
            0]
        delivery_cell_coords = [cell['cell_coordinates'] for cell in
            belief_set['map']['grid'] if cell['cell_type'] == 'delivery_cell'][
            0]
        if agent_coords == parcel_spawn_coords and len(belief_set['agent'][
            agent_id]['parcels_carried_ids']) < 1:
            function_5()
        elif agent_coords == delivery_cell_coords and len(belief_set[
            'agent'][agent_id]['parcels_carried_ids']) >= 1:
            function_6()
        elif agent_coords[0] > parcel_spawn_coords[0] and belief_set['map'][
            'grid'][agent_coords[0] - 1][agent_coords[1]]['cell_type'
            ] != 'non_walkable':
            function_1()
        elif agent_coords[0] < parcel_spawn_coords[0] and belief_set['map'][
            'grid'][agent_coords[0] + 1][agent_coords[1]]['cell_type'
            ] != 'non_walkable':
            function_2()
        elif agent_coords[1] > parcel_spawn_coords[1] and belief_set['map'][
            'grid'][agent_coords[0]][agent_coords[1] - 1]['cell_type'
            ] != 'non_walkable':
            function_3()
        elif agent_coords[1] < parcel_spawn_coords[1] and belief_set['map'][
            'grid'][agent_coords[0]][agent_coords[1] + 1]['cell_type'
            ] != 'non_walkable':
            function_4()
        iteration_count += 1

def function_12():
    global belief_set
    agent = belief_set['agent'][1]
    spawn_point = [item for item in belief_set['map']['grid'] if item[
        'cell_type'] == 'parcels_spawn'][0]['cell_coordinates']
    delivery_point = [item for item in belief_set['map']['grid'] if item[
        'cell_type'] == 'delivery_cell'][0]['cell_coordinates']
    previous_coordinates = agent['coordinates'][:]
    while True:
        if agent['coordinates'] == spawn_point:
            function_5()
        elif agent['coordinates'] == delivery_point:
            function_6()
        elif agent['coordinates'][0] > spawn_point[0]:
            function_1()
        elif agent['coordinates'][0] < spawn_point[0]:
            function_2()
        elif agent['coordinates'][1] > spawn_point[1]:
            function_3()
        elif agent['coordinates'][1] < spawn_point[1]:
            function_4()
        if previous_coordinates == agent['coordinates']:
            break
        else:
            previous_coordinates = agent['coordinates'][:]

def function_13():
    global belief_set
    agent = belief_set['agent'][1]
    while agent['coordinates'] != [0, 0]:
        if agent['coordinates'][0] > 0:
            function_1()
        elif agent['coordinates'][1] > 0:
            function_3()
    function_5()
    while agent['coordinates'] != [1, 3]:
        if agent['coordinates'][0] < 1:
            function_2()
        elif agent['coordinates'][1] < 3:
            function_4()
    function_6()

def function_14():
    global belief_set
    max_iterations = 100
    iteration_count = 0
    while iteration_count < max_iterations and belief_set['agent'][1][
        'coordinates'] != belief_set['parcels'][12]['coordinates']:
        if belief_set['agent'][1]['coordinates'][0] < belief_set['parcels'][12
            ]['coordinates'][0]:
            function_2()
        elif belief_set['agent'][1]['coordinates'][0] > belief_set['parcels'][
            12]['coordinates'][0]:
            function_1()
        elif belief_set['agent'][1]['coordinates'][1] < belief_set['parcels'][
            12]['coordinates'][1]:
            function_4()
        else:
            function_3()
        iteration_count += 1
    function_5()
    while iteration_count < max_iterations and belief_set['agent'][1][
        'coordinates'] != [1, 3]:
        if belief_set['agent'][1]['coordinates'][0] < 1:
            function_2()
        elif belief_set['agent'][1]['coordinates'][0] > 1:
            function_1()
        elif belief_set['agent'][1]['coordinates'][1] < 3:
            function_4()
        else:
            function_3()
        iteration_count += 1
    function_6()

