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
    agent_pos = belief_set['agent']['coordinates']
    key_pos = belief_set['keys'][1]['coordinates']
    while agent_pos != key_pos:
        if agent_pos[0] > key_pos[0]:
            function_1()
        elif agent_pos[0] < key_pos[0]:
            function_2()
        if agent_pos[1] > key_pos[1]:
            function_3()
        elif agent_pos[1] < key_pos[1]:
            function_4()
    function_5()

def function_8():
    global belief_set
    agent = belief_set['agent']
    keys = belief_set['keys']
    for key in keys.values():
        if key['coordinates'][0] > agent['coordinates'][0]:
            function_2()
        elif key['coordinates'][0] < agent['coordinates'][0]:
            function_1()
        elif key['coordinates'][1] > agent['coordinates'][1]:
            function_4()
        elif key['coordinates'][1] < agent['coordinates'][1]:
            function_3()
    function_5()

def function_9():
    global belief_set
    agent_coordinates = belief_set['agent']['coordinates']
    for cell in belief_set['map']['grid']:
        if cell['cell_type'] == 'walkable':
            cell_coordinates = cell['cell_coordinates']
            while agent_coordinates != cell_coordinates:
                if agent_coordinates[0] < cell_coordinates[0]:
                    function_2()
                    agent_coordinates[0] += 1
                elif agent_coordinates[0] > cell_coordinates[0]:
                    function_1()
                    agent_coordinates[0] -= 1
                if agent_coordinates[1] < cell_coordinates[1]:
                    function_4()
                    agent_coordinates[1] += 1
                elif agent_coordinates[1] > cell_coordinates[1]:
                    function_3()
                    agent_coordinates[1] -= 1
            function_5()
            break

def function_10():
    global belief_set
    agent_coord = belief_set['agent']['coordinates']
    keys = belief_set['keys']
    for key in keys.values():
        if key['coordinates'] == agent_coord and key['carried_by_id'] is None:
            function_5()
            break
    if agent_coord[0] > 0 and belief_set['map']['grid'][agent_coord[0] - 1][
        agent_coord[1]]['cell_type'] == 'walkable':
        function_1()
    elif agent_coord[0] < belief_set['map']['width'] - 1 and belief_set['map'][
        'grid'][agent_coord[0] + 1][agent_coord[1]]['cell_type'] == 'walkable':
        function_2()
    elif agent_coord[1] > 0 and belief_set['map']['grid'][agent_coord[0]][
        agent_coord[1] - 1]['cell_type'] == 'walkable':
        function_3()
    elif agent_coord[1] < belief_set['map']['height'] - 1 and belief_set['map'
        ]['grid'][agent_coord[0]][agent_coord[1] + 1]['cell_type'
        ] == 'walkable':
        function_4()

def function_11():
    global belief_set
    agent_coordinates = belief_set['agent']['coordinates']
    parcel_coordinates = None
    for parcel in belief_set['parcels'].values():
        if parcel['carried_by_id'] is None:
            parcel_coordinates = parcel['coordinates']
            break
    if parcel_coordinates is None:
        return
    dx = parcel_coordinates[0] - agent_coordinates[0]
    dy = parcel_coordinates[1] - agent_coordinates[1]
    if dx > 0:
        for i in range(dx):
            function_2()
    elif dx < 0:
        for i in range(abs(dx)):
            function_1()
    if dy > 0:
        for i in range(dy):
            function_4()
    elif dy < 0:
        for i in range(abs(dy)):
            function_3()
    function_5()

def function_12():
    global belief_set
    for cell in belief_set['map']['grid']:
        if cell['cell_type'] == 'walkable' and 'id' in [parcel for parcel in
            belief_set['parcels'].values() if parcel['coordinates'] == cell
            ['cell_coordinates']]:
            while belief_set['agent']['coordinates'] != cell['cell_coordinates'
                ]:
                if belief_set['agent']['coordinates'][0] < cell[
                    'cell_coordinates'][0]:
                    function_2()
                elif belief_set['agent']['coordinates'][0] > cell[
                    'cell_coordinates'][0]:
                    function_1()
                elif belief_set['agent']['coordinates'][1] < cell[
                    'cell_coordinates'][1]:
                    function_4()
                else:
                    function_3()
            function_5()
            break

def function_13():
    global belief_set
    for cell in belief_set['map']['grid']:
        if cell['cell_type'] == 'walkable':
            agent_coordinates = belief_set['agent']['coordinates']
            if cell['cell_coordinates'][0] > agent_coordinates[0]:
                function_2()
            elif cell['cell_coordinates'][0] < agent_coordinates[0]:
                function_1()
            if cell['cell_coordinates'][1] > agent_coordinates[1]:
                function_4()
            elif cell['cell_coordinates'][1] < agent_coordinates[1]:
                function_3()
            for key in belief_set['keys'].values():
                if key['coordinates'] == cell['cell_coordinates'] and key[
                    'carried_by_id'] is None:
                    function_5()
                    break
            for parcel in belief_set['parcels'].values():
                if parcel['coordinates'] == cell['cell_coordinates'
                    ] and parcel['carried_by_id'] is None:
                    function_5()
                    break

def function_14():
    global belief_set
    function_12()
    function_9()

def function_15():
    global belief_set
    if belief_set['agent']['parcels_carried_ids']:
        parcel_id = belief_set['agent']['parcels_carried_ids'][0]
        for cell in belief_set['map']['grid']:
            if cell['cell_type'] == 'delivery_cell':
                delivery_cell = cell['cell_coordinates']
                break
        while belief_set['agent']['coordinates'] != delivery_cell:
            if belief_set['agent']['coordinates'][0] > delivery_cell[0]:
                function_1()
            elif belief_set['agent']['coordinates'][0] < delivery_cell[0]:
                function_2()
            elif belief_set['agent']['coordinates'][1] > delivery_cell[1]:
                function_3()
            else:
                function_4()
        function_6()

