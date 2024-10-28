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
    while belief_set['agent']['coordinates'][0] > belief_set['parcel'][1][
        'coordinates'][0]:
        function_1()
    while belief_set['agent']['coordinates'][0] < belief_set['parcel'][1][
        'coordinates'][0]:
        function_2()
    while belief_set['agent']['coordinates'][1] > belief_set['parcel'][1][
        'coordinates'][1]:
        function_3()
    while belief_set['agent']['coordinates'][1] < belief_set['parcel'][1][
        'coordinates'][1]:
        function_4()
    function_5()
    delivery_cell_coordinates = None
    for cell in belief_set['map']['grid']:
        if cell['cell_type'] == 'delivery_cell':
            delivery_cell_coordinates = cell['cell_coordinates']
            break
    while belief_set['agent']['coordinates'][0] > delivery_cell_coordinates[0]:
        function_1()
    while belief_set['agent']['coordinates'][0] < delivery_cell_coordinates[0]:
        function_2()
    while belief_set['agent']['coordinates'][1] > delivery_cell_coordinates[1]:
        function_3()
    while belief_set['agent']['coordinates'][1] < delivery_cell_coordinates[1]:
        function_4()
    function_6()

def function_8():
    global belief_set
    agent_position = belief_set['agent']['coordinates']
    delivery_position = [cell['cell_coordinates'] for cell in belief_set[
        'map']['grid'] if cell['cell_type'] == 'delivery_cell'][0]
    if agent_position[0] > delivery_position[0]:
        function_1()
    elif agent_position[0] < delivery_position[0]:
        function_2()
    if agent_position[1] > delivery_position[1]:
        function_3()
    elif agent_position[1] < delivery_position[1]:
        function_4()
    function_6()

def function_9():
    global belief_set
    for parcel in belief_set['parcel'].values():
        if parcel['coordinates'] == belief_set['agent']['coordinates'
            ] and parcel['carried_by_id'] is None:
            function_5()
            break
    for cell in belief_set['map']['grid']:
        if cell['cell_type'] == 'delivery_cell':
            delivery_cell_coordinates = cell['cell_coordinates']
            while belief_set['agent']['coordinates'
                ] != delivery_cell_coordinates:
                if belief_set['agent']['coordinates'][0
                    ] < delivery_cell_coordinates[0]:
                    function_2()
                elif belief_set['agent']['coordinates'][0
                    ] > delivery_cell_coordinates[0]:
                    function_1()
                elif belief_set['agent']['coordinates'][1
                    ] < delivery_cell_coordinates[1]:
                    function_4()
                elif belief_set['agent']['coordinates'][1
                    ] > delivery_cell_coordinates[1]:
                    function_3()
    function_6()

def function_10():
    global belief_set
    parcel_coordinates = belief_set['parcel'][1]['coordinates']
    agent_coordinates = belief_set['agent']['coordinates']
    while agent_coordinates != parcel_coordinates:
        if agent_coordinates[0] < parcel_coordinates[0]:
            function_2()
        elif agent_coordinates[0] > parcel_coordinates[0]:
            function_1()
        elif agent_coordinates[1] < parcel_coordinates[1]:
            function_4()
        elif agent_coordinates[1] > parcel_coordinates[1]:
            function_3()
        agent_coordinates = belief_set['agent']['coordinates']
    function_5()

def function_11():
    global belief_set
    delivery_cell_coords = next(cell['cell_coordinates'] for cell in
        belief_set['map']['grid'] if cell['cell_type'] == 'delivery_cell')
    agent_coords = belief_set['agent']['coordinates']
    while agent_coords != delivery_cell_coords:
        if agent_coords[0] < delivery_cell_coords[0]:
            function_2()
        elif agent_coords[0] > delivery_cell_coords[0]:
            function_1()
        elif agent_coords[1] < delivery_cell_coords[1]:
            function_4()
        elif agent_coords[1] > delivery_cell_coords[1]:
            function_3()
        agent_coords = belief_set['agent']['coordinates']
    function_6()

def function_12():
    global belief_set
    agent_coordinates = belief_set['agent']['coordinates']
    delivery_cells = [cell['cell_coordinates'] for cell in belief_set['map'
        ]['grid'] if cell['cell_type'] == 'delivery_cell']
    for cell in delivery_cells:
        if cell[0] > agent_coordinates[0]:
            return function_2()
        elif cell[0] < agent_coordinates[0]:
            return function_1()
        elif cell[1] > agent_coordinates[1]:
            return function_4()
        elif cell[1] < agent_coordinates[1]:
            return function_3()
    return function_6()

def function_13():
    global belief_set
    agent_coordinates = belief_set['agent']['coordinates']
    delivery_coordinates = [cell['cell_coordinates'] for cell in belief_set
        ['map']['grid'] if cell['cell_type'] == 'delivery_cell'][0]
    if agent_coordinates[0] < delivery_coordinates[0]:
        function_2()
    elif agent_coordinates[0] > delivery_coordinates[0]:
        function_1()
    elif agent_coordinates[1] < delivery_coordinates[1]:
        function_4()
    elif agent_coordinates[1] > delivery_coordinates[1]:
        function_3()
    if agent_coordinates == delivery_coordinates and belief_set['agent'][
        'parcels_carried_ids']:
        function_6()

def function_14():
    global belief_set
    key_coordinates = belief_set['key'][1]['coordinates']
    agent_coordinates = belief_set['agent']['coordinates']
    while agent_coordinates != key_coordinates:
        if agent_coordinates[0] < key_coordinates[0]:
            function_2()
        elif agent_coordinates[0] > key_coordinates[0]:
            function_1()
        elif agent_coordinates[1] < key_coordinates[1]:
            function_4()
        elif agent_coordinates[1] > key_coordinates[1]:
            function_3()
    function_5()

def function_15():
    global belief_set
    agent_coords = belief_set['agent']['coordinates']
    delivery_cell_coords = [cell['cell_coordinates'] for cell in belief_set
        ['map']['grid'] if cell['cell_type'] == 'delivery_cell'][0]
    if agent_coords[0] < delivery_cell_coords[0]:
        function_2()
    elif agent_coords[0] > delivery_cell_coords[0]:
        function_1()
    elif agent_coords[1] < delivery_cell_coords[1]:
        function_4()
    elif agent_coords[1] > delivery_cell_coords[1]:
        function_3()

def function_16():
    global belief_set
    agent = belief_set['agent']
    delivery_cell = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'delivery_cell'][0]['cell_coordinates']
    while agent['coordinates'] != delivery_cell:
        if agent['coordinates'][0] < delivery_cell[0] and [cell for cell in
            belief_set['map']['grid'] if cell['cell_coordinates'] == [agent
            ['coordinates'][0] + 1, agent['coordinates'][1]]][0]['cell_type'
            ] == 'walkable':
            function_2()
        elif agent['coordinates'][0] > delivery_cell[0] and [cell for cell in
            belief_set['map']['grid'] if cell['cell_coordinates'] == [agent
            ['coordinates'][0] - 1, agent['coordinates'][1]]][0]['cell_type'
            ] == 'walkable':
            function_1()
        elif agent['coordinates'][1] < delivery_cell[1] and [cell for cell in
            belief_set['map']['grid'] if cell['cell_coordinates'] == [agent
            ['coordinates'][0], agent['coordinates'][1] + 1]][0]['cell_type'
            ] == 'walkable':
            function_4()
        elif agent['coordinates'][1] > delivery_cell[1] and [cell for cell in
            belief_set['map']['grid'] if cell['cell_coordinates'] == [agent
            ['coordinates'][0], agent['coordinates'][1] - 1]][0]['cell_type'
            ] == 'walkable':
            function_3()
        else:
            break
    if agent['coordinates'] == delivery_cell:
        function_6()

def function_17():
    global belief_set
    agent = belief_set['agent']
    delivery_cell = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'delivery_cell'][0]
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

def function_18():
    global belief_set
    agent_position = belief_set['agent']['coordinates']
    delivery_cell_position = [cell['cell_coordinates'] for cell in
        belief_set['map']['grid'] if cell['cell_type'] == 'delivery_cell'][0]
    if 'parcel' in belief_set and belief_set['parcel'][1]['coordinates'
        ] == agent_position:
        function_5()
    elif 'key' in belief_set and belief_set['key'][1]['coordinates'
        ] == agent_position:
        function_5()
    elif agent_position[0] < delivery_cell_position[0]:
        function_2()
    elif agent_position[0] > delivery_cell_position[0]:
        function_1()
    elif agent_position[1] < delivery_cell_position[1]:
        function_4()
    elif agent_position[1] > delivery_cell_position[1]:
        function_3()

def function_19():
    global belief_set
    function_10()
    if belief_set['agent']['coordinates'] != belief_set['map']['grid'][7][
        'cell_coordinates']:
        function_2()
        function_4()
    function_5()

