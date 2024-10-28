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
    agent_coords = belief_set['agent']['coordinates']
    if not belief_set['agent']['parcels_carried_ids']:
        parcel_coords = belief_set['parcels'][1]['coordinates']
        if agent_coords[0] < parcel_coords[0]:
            function_2()
        elif agent_coords[0] > parcel_coords[0]:
            function_1()
        elif agent_coords[1] < parcel_coords[1]:
            function_4()
        elif agent_coords[1] > parcel_coords[1]:
            function_3()
        else:
            function_5()
    else:
        delivery_coords = [cell['cell_coordinates'] for cell in belief_set[
            'map']['grid'] if 'delivery' in cell['cell_type']][0]
        if agent_coords[0] < delivery_coords[0]:
            function_2()
        elif agent_coords[0] > delivery_coords[0]:
            function_1()
        elif agent_coords[1] < delivery_coords[1]:
            function_4()
        elif agent_coords[1] > delivery_coords[1]:
            function_3()
        else:
            function_6()

def function_8():
    global belief_set
    agent = belief_set['agent']
    parcel = next(iter(belief_set['parcels'].values()))
    if agent['coordinates'][0] < parcel['coordinates'][0]:
        function_2()
    elif agent['coordinates'][0] > parcel['coordinates'][0]:
        function_1()
    elif agent['coordinates'][1] < parcel['coordinates'][1]:
        function_4()
    elif agent['coordinates'][1] > parcel['coordinates'][1]:
        function_3()

def function_9():
    global belief_set
    function_8()
    function_5()
    function_8()
    function_6()

def function_10():
    global belief_set
    if belief_set['agent']['coordinates'] == belief_set['parcels'][1][
        'coordinates']:
        function_5()
    else:
        function_8()

def function_11():
    global belief_set
    function_8()
    if belief_set['agent']['coordinates'] == belief_set['parcels'][1][
        'coordinates']:
        function_5()
        while belief_set['agent']['coordinates'] != [3, 0]:
            function_2()
        function_6()

def function_12():
    global belief_set
    iteration_count = 0
    while True:
        iteration_count += 1
        if iteration_count > 100:
            break
        agent_coordinates = belief_set['agent']['coordinates']
        if belief_set['parcels'][1]['coordinates'] == agent_coordinates:
            function_5()
        elif belief_set['parcels'][1]['coordinates'][0] > agent_coordinates[0]:
            function_2()
        elif belief_set['parcels'][1]['coordinates'][0] < agent_coordinates[0]:
            function_1()
        elif belief_set['parcels'][1]['coordinates'][1] > agent_coordinates[1]:
            function_4()
        elif belief_set['parcels'][1]['coordinates'][1] < agent_coordinates[1]:
            function_3()
        if belief_set['agent']['parcels_carried_ids']:
            if belief_set['map']['grid'][12]['cell_coordinates'
                ] == agent_coordinates:
                function_6()
            elif belief_set['map']['grid'][12]['cell_coordinates'][0
                ] > agent_coordinates[0]:
                function_2()
            elif belief_set['map']['grid'][12]['cell_coordinates'][0
                ] < agent_coordinates[0]:
                function_1()
            elif belief_set['map']['grid'][12]['cell_coordinates'][1
                ] > agent_coordinates[1]:
                function_4()
            elif belief_set['map']['grid'][12]['cell_coordinates'][1
                ] < agent_coordinates[1]:
                function_3()

def function_13():
    global belief_set
    agent = belief_set['agent']
    parcels = belief_set['parcels']
    map_ = belief_set['map']['grid']
    delivered = False
    while not delivered:
        if not agent['parcels_carried_ids']:
            function_8()
            if agent['coordinates'] == parcels[1]['coordinates']:
                function_5()
        else:
            delivery_cells = [cell['cell_coordinates'] for cell in map_ if 
                'delivery' in cell['cell_type']]
            nearest_delivery_cell = min(delivery_cells, key=lambda x: abs(x
                [0] - agent['coordinates'][0]) + abs(x[1] - agent[
                'coordinates'][1]))
            while agent['coordinates'] != nearest_delivery_cell:
                if agent['coordinates'][0] < nearest_delivery_cell[0]:
                    function_2()
                elif agent['coordinates'][0] > nearest_delivery_cell[0]:
                    function_1()
                elif agent['coordinates'][1] < nearest_delivery_cell[1]:
                    function_4()
                elif agent['coordinates'][1] > nearest_delivery_cell[1]:
                    function_3()
            function_6()
            delivered = True

def function_14():
    global belief_set
    key_coordinates = belief_set['keys'][1]['coordinates']
    agent_coordinates = belief_set['agent']['coordinates']
    if agent_coordinates[0] > key_coordinates[0]:
        function_1()
    elif agent_coordinates[0] < key_coordinates[0]:
        function_2()
    elif agent_coordinates[1] > key_coordinates[1]:
        function_3()
    elif agent_coordinates[1] < key_coordinates[1]:
        function_4()
    else:
        function_5()
        door_coordinates = belief_set['doors'][1]['coordinates']
        if agent_coordinates[0] > door_coordinates[0]:
            function_1()
        elif agent_coordinates[0] < door_coordinates[0]:
            function_2()
        elif agent_coordinates[1] > door_coordinates[1]:
            function_3()
        elif agent_coordinates[1] < door_coordinates[1]:
            function_4()

def function_15():
    global belief_set
    agent = belief_set['agent']
    parcels = belief_set['parcels']
    if len(agent['parcels_carried_ids']) > 0:
        for parcel_id in agent['parcels_carried_ids']:
            if parcels[parcel_id]['coordinates'] == agent['coordinates']:
                function_6()
                return
        if agent['coordinates'][0] < 3:
            function_2()
        elif agent['coordinates'][0] > 3:
            function_1()
        elif agent['coordinates'][1] < 0:
            function_4()
        elif agent['coordinates'][1] > 0:
            function_3()
    else:
        function_10()

def function_16():
    global belief_set
    if not belief_set['agent']['parcels_carried_ids']:
        function_8()
        function_5()
    else:
        function_6()
        function_4()

def function_17():
    global belief_set
    agent_position = belief_set['agent']['coordinates']
    for cell in belief_set['map']['grid']:
        if cell['cell_type'] == 'delivery_cell' or cell['cell_type'
            ] == 'double_points_delivery_cell':
            delivery_position = cell['cell_coordinates']
            break
    if agent_position[0] > delivery_position[0]:
        function_1()
    elif agent_position[0] < delivery_position[0]:
        function_2()
    elif agent_position[1] > delivery_position[1]:
        function_3()
    elif agent_position[1] < delivery_position[1]:
        function_4()
    else:
        function_6()

def function_18():
    global belief_set
    agent = belief_set['agent']
    delivery_cell = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] in ['delivery_cell', 'double_points_delivery_cell']][0]
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

def function_19():
    global belief_set
    delivery_cell = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] in ['delivery_cell', 'double_points_delivery_cell']][0]
    agent_position = belief_set['agent']['coordinates']
    parcel_carried = belief_set['agent']['parcels_carried_ids']
    if parcel_carried:
        while agent_position != delivery_cell['cell_coordinates']:
            if agent_position[0] < delivery_cell['cell_coordinates'][0]:
                function_2()
            elif agent_position[0] > delivery_cell['cell_coordinates'][0]:
                function_1()
            if agent_position[1] < delivery_cell['cell_coordinates'][1]:
                function_4()
            elif agent_position[1] > delivery_cell['cell_coordinates'][1]:
                function_3()
            if agent_position == belief_set['agent']['coordinates']:
                break
        function_6()
    else:
        function_10()

def function_20():
    global belief_set
    if belief_set['agent']['coordinates'] == belief_set['parcels'][1][
        'coordinates']:
        function_5()
    else:
        function_8()

def function_21():
    global belief_set
    parcel_coords = belief_set['agent']['coordinates']
    delivery_cells = [cell['cell_coordinates'] for cell in belief_set['map'
        ]['grid'] if 'delivery' in cell['cell_type']]
    nearest_delivery_cell = min(delivery_cells, key=lambda x: abs(x[0] -
        parcel_coords[0]) + abs(x[1] - parcel_coords[1]))
    while belief_set['agent']['coordinates'] != nearest_delivery_cell:
        if nearest_delivery_cell[0] < belief_set['agent']['coordinates'][0]:
            function_1()
        elif nearest_delivery_cell[0] > belief_set['agent']['coordinates'][0]:
            function_2()
        elif nearest_delivery_cell[1] < belief_set['agent']['coordinates'][1]:
            function_3()
        else:
            function_4()
    function_6()

def function_22():
    global belief_set
    step_counter = 0
    max_steps = 100
    agent_pos = belief_set['agent']['coordinates']
    delivery_cells = [cell['cell_coordinates'] for cell in belief_set['map'
        ]['grid'] if 'delivery' in cell['cell_type']]
    while step_counter < max_steps and agent_pos not in delivery_cells:
        function_8()
        step_counter += 1
        agent_pos = belief_set['agent']['coordinates']
    if agent_pos in delivery_cells:
        function_6()
    else:
        function_20()
        function_10()

def function_23():
    global belief_set
    delivery_cells = [cell['cell_coordinates'] for cell in belief_set['map'
        ]['grid'] if 'delivery' in cell['cell_type']]
    agent_coords = belief_set['agent']['coordinates']
    nearest_delivery_cell = min(delivery_cells, key=lambda x: abs(x[0] -
        agent_coords[0]) + abs(x[1] - agent_coords[1]))
    while agent_coords != nearest_delivery_cell:
        if agent_coords[0] < nearest_delivery_cell[0]:
            function_2()
        elif agent_coords[0] > nearest_delivery_cell[0]:
            function_1()
        if agent_coords[1] < nearest_delivery_cell[1]:
            function_4()
        elif agent_coords[1] > nearest_delivery_cell[1]:
            function_3()
        agent_coords = belief_set['agent']['coordinates']
    function_6()

