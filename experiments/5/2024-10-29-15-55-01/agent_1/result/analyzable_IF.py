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
    agent_position = belief_set['agent'][1]['coordinates']
    parcel_position = belief_set['parcels'][1]['coordinates']
    delivery_position = [cell['cell_coordinates'] for cell in belief_set[
        'map']['grid'] if cell['cell_type'] == 'delivery_cell'][0]
    while agent_position != parcel_position:
        if agent_position[0] > parcel_position[0]:
            function_1()
            agent_position[0] -= 1
        elif agent_position[0] < parcel_position[0]:
            function_2()
            agent_position[0] += 1
        elif agent_position[1] > parcel_position[1]:
            function_3()
            agent_position[1] -= 1
        elif agent_position[1] < parcel_position[1]:
            function_4()
            agent_position[1] += 1
    function_5()
    while agent_position != delivery_position:
        if agent_position[0] > delivery_position[0]:
            function_1()
            agent_position[0] -= 1
        elif agent_position[0] < delivery_position[0]:
            function_2()
            agent_position[0] += 1
        elif agent_position[1] > delivery_position[1]:
            function_3()
            agent_position[1] -= 1
        elif agent_position[1] < delivery_position[1]:
            function_4()
            agent_position[1] += 1
    function_6()

def function_8():
    global belief_set
    agent = belief_set['agent'][1]
    parcels = belief_set['parcels']
    map_grid = belief_set['map']['grid']
    delivery_cell = [cell for cell in map_grid if cell['cell_type'] ==
        'delivery_cell'][0]['cell_coordinates']
    parcel_ids = [parcel['id'] for parcel in parcels.values() if parcel[
        'carried_by_id'] is None]
    if parcel_ids:
        parcel_location = parcels[parcel_ids[0]]['coordinates']
        while agent['coordinates'] != parcel_location:
            if agent['coordinates'][0] < parcel_location[0]:
                function_2()
            elif agent['coordinates'][0] > parcel_location[0]:
                function_1()
            elif agent['coordinates'][1] < parcel_location[1]:
                function_4()
            elif agent['coordinates'][1] > parcel_location[1]:
                function_3()
        function_5()
    while agent['coordinates'] != delivery_cell:
        if agent['coordinates'][0] < delivery_cell[0]:
            function_2()
        elif agent['coordinates'][0] > delivery_cell[0]:
            function_1()
        elif agent['coordinates'][1] < delivery_cell[1]:
            function_4()
        elif agent['coordinates'][1] > delivery_cell[1]:
            function_3()
    function_6()

def function_9():
    global belief_set
    width = belief_set['map']['width']
    height = belief_set['map']['height']
    grid = belief_set['map']['grid']
    agent = belief_set['agent'][1]
    parcels = belief_set['parcels']
    non_walkable_cells = [cell for cell in grid if cell['cell_type'] ==
        'non_walkable']
    for i in range(width * height):
        for parcel in parcels.values():
            if parcel['carried_by_id'] is None and parcel['coordinates'
                ] not in [cell['cell_coordinates'] for cell in
                non_walkable_cells]:
                while agent['coordinates'][0] > parcel['coordinates'][0]:
                    function_1()
                while agent['coordinates'][0] < parcel['coordinates'][0]:
                    function_2()
                while agent['coordinates'][1] > parcel['coordinates'][1]:
                    function_3()
                while agent['coordinates'][1] < parcel['coordinates'][1]:
                    function_4()
                function_5()
                break
        else:
            continue
        break
    delivery_cell_coordinates = [cell['cell_coordinates'] for cell in grid if
        cell['cell_type'] == 'delivery_cell'][0]
    for i in range(width * height):
        while agent['coordinates'][0] > delivery_cell_coordinates[0]:
            function_1()
        while agent['coordinates'][0] < delivery_cell_coordinates[0]:
            function_2()
        while agent['coordinates'][1] > delivery_cell_coordinates[1]:
            function_3()
        while agent['coordinates'][1] < delivery_cell_coordinates[1]:
            function_4()
        function_6()
        break

def function_10():
    global belief_set
    agent = belief_set['agent'][1]
    parcels = belief_set['parcels']
    map_info = belief_set['map']
    width = map_info['width']
    height = map_info['height']
    delivery_cell = [cell for cell in map_info['grid'] if cell['cell_type'] ==
        'delivery_cell'][0]['cell_coordinates']
    for parcel_id, parcel_info in parcels.items():
        if parcel_info['carried_by_id'] is None:
            parcel_coordinates = parcel_info['coordinates']
            while agent['coordinates'] != parcel_coordinates:
                if agent['coordinates'][0] > parcel_coordinates[0] and agent[
                    'coordinates'][0] > 0:
                    function_1()
                elif agent['coordinates'][0] < parcel_coordinates[0] and agent[
                    'coordinates'][0] < width - 1:
                    function_2()
                if agent['coordinates'][1] > parcel_coordinates[1] and agent[
                    'coordinates'][1] > 0:
                    function_3()
                elif agent['coordinates'][1] < parcel_coordinates[1] and agent[
                    'coordinates'][1] < height - 1:
                    function_4()
            function_5()
            break
    while agent['coordinates'] != delivery_cell:
        if agent['coordinates'][0] > delivery_cell[0] and agent['coordinates'][
            0] > 0:
            function_1()
        elif agent['coordinates'][0] < delivery_cell[0] and agent['coordinates'
            ][0] < width - 1:
            function_2()
        if agent['coordinates'][1] > delivery_cell[1] and agent['coordinates'][
            1] > 0:
            function_3()
        elif agent['coordinates'][1] < delivery_cell[1] and agent['coordinates'
            ][1] < height - 1:
            function_4()
    function_6()

def function_11():
    global belief_set
    spawn_coordinates = [cell['cell_coordinates'] for cell in belief_set[
        'map']['grid'] if cell['cell_type'] == 'parcels_spawn'][0]
    delivery_coordinates = [cell['cell_coordinates'] for cell in belief_set
        ['map']['grid'] if cell['cell_type'] == 'delivery_cell'][0]
    agent_coordinates = belief_set['agent'][1]['coordinates']
    while agent_coordinates != spawn_coordinates:
        if agent_coordinates[0] > spawn_coordinates[0]:
            function_1()
        elif agent_coordinates[0] < spawn_coordinates[0]:
            function_2()
        if agent_coordinates[1] > spawn_coordinates[1]:
            function_3()
        elif agent_coordinates[1] < spawn_coordinates[1]:
            function_4()
        agent_coordinates = belief_set['agent'][1]['coordinates']
    function_5()
    while agent_coordinates != delivery_coordinates:
        if agent_coordinates[0] > delivery_coordinates[0]:
            function_1()
        elif agent_coordinates[0] < delivery_coordinates[0]:
            function_2()
        if agent_coordinates[1] > delivery_coordinates[1]:
            function_3()
        elif agent_coordinates[1] < delivery_coordinates[1]:
            function_4()
        agent_coordinates = belief_set['agent'][1]['coordinates']
    function_6()

def function_12():
    global belief_set
    agent = belief_set['agent'][1]
    map_grid = belief_set['map']['grid']
    agent_x, agent_y = agent['coordinates']
    walkable_cells = [cell for cell in map_grid if cell['cell_type'] ==
        'walkable']
    nearest_walkable_cell = min(walkable_cells, key=lambda cell: abs(cell[
        'cell_coordinates'][0] - agent_x) + abs(cell['cell_coordinates'][1] -
        agent_y))
    if nearest_walkable_cell['cell_coordinates'][0] < agent_x:
        function_1()
    elif nearest_walkable_cell['cell_coordinates'][0] > agent_x:
        function_2()
    elif nearest_walkable_cell['cell_coordinates'][1] < agent_y:
        function_3()
    elif nearest_walkable_cell['cell_coordinates'][1] > agent_y:
        function_4()

def function_13():
    global belief_set
    agent = belief_set['agent'][1]
    if belief_set['parcels']:
        parcel = list(belief_set['parcels'].values())[0]
        while agent['coordinates'] != parcel['coordinates']:
            if agent['coordinates'][0] < parcel['coordinates'][0]:
                function_2()
            elif agent['coordinates'][0] > parcel['coordinates'][0]:
                function_1()
            if agent['coordinates'][1] < parcel['coordinates'][1]:
                function_4()
            elif agent['coordinates'][1] > parcel['coordinates'][1]:
                function_3()
        function_5()
    delivery_cell = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'delivery_cell'][0]
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

def function_14():
    global belief_set
    max_iterations = 1000
    iteration = 0
    while True:
        if iteration > max_iterations:
            break
        agent_coordinates = belief_set['agent'][1]['coordinates']
        parcel_coordinates = belief_set['parcels'][12]['coordinates']
        delivery_coordinates = [1, 3]
        if agent_coordinates == parcel_coordinates:
            function_5()
        elif agent_coordinates == delivery_coordinates:
            function_6()
            break
        else:
            function_11()
        iteration += 1

def function_15():
    global belief_set
    agent_coordinates = belief_set['agent'][1]['coordinates']
    delivery_coordinates = [1, 3]
    iteration_counter = 0
    while (agent_coordinates != delivery_coordinates and iteration_counter <
        100):
        if agent_coordinates[0] < delivery_coordinates[0]:
            function_2()
        elif agent_coordinates[0] > delivery_coordinates[0]:
            function_1()
        if agent_coordinates[1] < delivery_coordinates[1]:
            function_4()
        elif agent_coordinates[1] > delivery_coordinates[1]:
            function_3()
        iteration_counter += 1
        if iteration_counter == 99:
            break
    function_5()
    while (agent_coordinates != delivery_coordinates and iteration_counter <
        200):
        if agent_coordinates[0] < delivery_coordinates[0]:
            function_2()
        elif agent_coordinates[0] > delivery_coordinates[0]:
            function_1()
        if agent_coordinates[1] < delivery_coordinates[1]:
            function_4()
        elif agent_coordinates[1] > delivery_coordinates[1]:
            function_3()
        iteration_counter += 1
        if iteration_counter == 199:
            break
    function_6()

