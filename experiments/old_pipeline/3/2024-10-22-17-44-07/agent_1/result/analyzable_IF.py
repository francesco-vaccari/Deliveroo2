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
    agent = belief_set['agent']
    key = belief_set['keys'][1]
    door = belief_set['doors'][1]
    while agent['coordinates'] != key['coordinates']:
        if agent['coordinates'][0] < key['coordinates'][0]:
            function_2()
        elif agent['coordinates'][0] > key['coordinates'][0]:
            function_1()
        if agent['coordinates'][1] < key['coordinates'][1]:
            function_4()
        elif agent['coordinates'][1] > key['coordinates'][1]:
            function_3()
    function_5()
    while agent['coordinates'] != door['coordinates']:
        if agent['coordinates'][0] < door['coordinates'][0]:
            function_2()
        elif agent['coordinates'][0] > door['coordinates'][0]:
            function_1()
        if agent['coordinates'][1] < door['coordinates'][1]:
            function_4()
        elif agent['coordinates'][1] > door['coordinates'][1]:
            function_3()
    function_5()

def function_8():
    global belief_set
    agent = belief_set['agent']
    key = belief_set['keys'][1]
    door = belief_set['doors'][1]
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

def function_9():
    global belief_set
    if belief_set['parcels'][1]['coordinates'][0] < belief_set['agent'][
        'coordinates'][0]:
        function_1()
    elif belief_set['parcels'][1]['coordinates'][0] > belief_set['agent'][
        'coordinates'][0]:
        function_2()
    elif belief_set['parcels'][1]['coordinates'][1] < belief_set['agent'][
        'coordinates'][1]:
        function_3()
    elif belief_set['parcels'][1]['coordinates'][1] > belief_set['agent'][
        'coordinates'][1]:
        function_4()
    else:
        function_5()

def function_10():
    global belief_set
    while belief_set['agent']['coordinates'] != belief_set['parcels'][1][
        'coordinates']:
        if belief_set['agent']['coordinates'][0] > belief_set['parcels'][1][
            'coordinates'][0]:
            function_1()
        elif belief_set['agent']['coordinates'][0] < belief_set['parcels'][1][
            'coordinates'][0]:
            function_2()
        elif belief_set['agent']['coordinates'][1] > belief_set['parcels'][1][
            'coordinates'][1]:
            function_3()
        elif belief_set['agent']['coordinates'][1] < belief_set['parcels'][1][
            'coordinates'][1]:
            function_4()
    function_5()
    for cell in belief_set['map']['grid']:
        if cell['cell_type'] in ['double_delivery_cell', 'delivery_cell']:
            while belief_set['agent']['coordinates'] != cell['cell_coordinates'
                ]:
                if belief_set['agent']['coordinates'][0] > cell[
                    'cell_coordinates'][0]:
                    function_1()
                elif belief_set['agent']['coordinates'][0] < cell[
                    'cell_coordinates'][0]:
                    function_2()
                elif belief_set['agent']['coordinates'][1] > cell[
                    'cell_coordinates'][1]:
                    function_3()
                elif belief_set['agent']['coordinates'][1] < cell[
                    'cell_coordinates'][1]:
                    function_4()
    function_6()

def function_11():
    global belief_set
    function_3()
    if belief_set['map']['grid'][belief_set['agent']['coordinates'][0]][
        belief_set['agent']['coordinates'][1]]['cell_type'
        ] == 'delivery_cell' or belief_set['map']['grid'][belief_set[
        'agent']['coordinates'][0]][belief_set['agent']['coordinates'][1]][
        'cell_type'] == 'double_delivery_cell':
        function_6()

def function_12():
    global belief_set
    agent = belief_set['agent']
    parcels = belief_set['parcels']
    for parcel_id, parcel_info in parcels.items():
        if parcel_info['coordinates'] == agent['coordinates']:
            function_5()
        elif parcel_info['coordinates'][0] < agent['coordinates'][0]:
            function_1()
        elif parcel_info['coordinates'][0] > agent['coordinates'][0]:
            function_2()
        elif parcel_info['coordinates'][1] < agent['coordinates'][1]:
            function_3()
        elif parcel_info['coordinates'][1] > agent['coordinates'][1]:
            function_4()
    map_grid = belief_set['map']['grid']
    for cell in map_grid:
        if cell['cell_type'] == 'delivery_cell' or cell['cell_type'
            ] == 'double_delivery_cell':
            if cell['cell_coordinates'] == agent['coordinates']:
                function_6()
            elif cell['cell_coordinates'][0] < agent['coordinates'][0]:
                function_1()
            elif cell['cell_coordinates'][0] > agent['coordinates'][0]:
                function_2()
            elif cell['cell_coordinates'][1] < agent['coordinates'][1]:
                function_3()
            elif cell['cell_coordinates'][1] > agent['coordinates'][1]:
                function_4()

def function_13():
    global belief_set
    agent_pos = belief_set['agent']['coordinates']
    parcels_carried = belief_set['agent']['parcels_carried_ids']
    if len(parcels_carried) > 0:
        for cell in belief_set['map']['grid']:
            if cell['cell_type'] in ['delivery_cell', 'double_delivery_cell'
                ] and cell['cell_coordinates'][0] > agent_pos[0]:
                function_2()
                break
            elif cell['cell_type'] in ['delivery_cell', 'double_delivery_cell'
                ] and cell['cell_coordinates'][0] < agent_pos[0]:
                function_1()
                break
            elif cell['cell_type'] in ['delivery_cell', 'double_delivery_cell'
                ] and cell['cell_coordinates'][1] > agent_pos[1]:
                function_4()
                break
            elif cell['cell_type'] in ['delivery_cell', 'double_delivery_cell'
                ] and cell['cell_coordinates'][1] < agent_pos[1]:
                function_3()
                break
        else:
            function_6()
    else:
        return

def function_14():
    global belief_set
    agent_coordinates = belief_set['agent']['coordinates']
    delivery_cell_coordinates = [cell['cell_coordinates'] for cell in
        belief_set['map']['grid'] if cell['cell_type'] in ['delivery_cell',
        'double_delivery_cell']]
    for coordinate in delivery_cell_coordinates:
        if agent_coordinates[0] < coordinate[0]:
            function_2()
        elif agent_coordinates[0] > coordinate[0]:
            function_1()
        if agent_coordinates[1] < coordinate[1]:
            function_4()
        elif agent_coordinates[1] > coordinate[1]:
            function_3()
    function_6()

def function_15():
    global belief_set
    agent_coordinates = belief_set['agent']['coordinates']
    parcel_coordinates = [parcel['coordinates'] for parcel in belief_set[
        'parcels'].values() if parcel['carried_by_id'] is None]
    key_coordinates = [key['coordinates'] for key in belief_set['keys'].
        values() if key['carried_by_id'] is None]
    nearest_coordinates = min(parcel_coordinates + key_coordinates, key=lambda
        c: abs(c[0] - agent_coordinates[0]) + abs(c[1] - agent_coordinates[1]))
    if agent_coordinates != nearest_coordinates:
        if nearest_coordinates[0] > agent_coordinates[0]:
            function_2()
        elif nearest_coordinates[0] < agent_coordinates[0]:
            function_1()
        elif nearest_coordinates[1] > agent_coordinates[1]:
            function_4()
        else:
            function_3()
    else:
        function_5()
        delivery_cell_coordinates = [cell['cell_coordinates'] for cell in
            belief_set['map']['grid'] if 'delivery' in cell['cell_type']]
        nearest_delivery_cell_coordinates = min(delivery_cell_coordinates,
            key=lambda c: abs(c[0] - agent_coordinates[0]) + abs(c[1] -
            agent_coordinates[1]))
        if nearest_delivery_cell_coordinates[0] > agent_coordinates[0]:
            function_2()
        elif nearest_delivery_cell_coordinates[0] < agent_coordinates[0]:
            function_1()
        elif nearest_delivery_cell_coordinates[1] > agent_coordinates[1]:
            function_4()
        else:
            function_3()

def function_16():
    global belief_set
    current_position = belief_set['agent']['coordinates']
    map_grid = belief_set['map']['grid']
    walkable_cells = [cell['cell_coordinates'] for cell in map_grid if cell
        ['cell_type'] == 'walkable']
    nearest_walkable_cell = min(walkable_cells, key=lambda cell: abs(cell[0
        ] - current_position[0]) + abs(cell[1] - current_position[1]))
    if nearest_walkable_cell[0] < current_position[0]:
        function_1()
    elif nearest_walkable_cell[0] > current_position[0]:
        function_2()
    elif nearest_walkable_cell[1] < current_position[1]:
        function_3()
    elif nearest_walkable_cell[1] > current_position[1]:
        function_4()

def function_17():
    global belief_set
    delivery_cells = [cell['cell_coordinates'] for cell in belief_set['map'
        ]['grid'] if 'delivery' in cell['cell_type']]
    agent_position = belief_set['agent']['coordinates']
    delivery_cells.sort(key=lambda x: abs(x[0] - agent_position[0]) + abs(x
        [1] - agent_position[1]))
    nearest_delivery_cell = delivery_cells[0]
    while belief_set['agent']['coordinates'] != nearest_delivery_cell:
        if belief_set['agent']['coordinates'][0] < nearest_delivery_cell[0]:
            function_2()
        elif belief_set['agent']['coordinates'][0] > nearest_delivery_cell[0]:
            function_1()
        elif belief_set['agent']['coordinates'][1] < nearest_delivery_cell[1]:
            function_4()
        elif belief_set['agent']['coordinates'][1] > nearest_delivery_cell[1]:
            function_3()
    function_6()

