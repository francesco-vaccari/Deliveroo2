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
    if agent['energy'] < 50:
        battery_spawn = next(cell for cell in belief_set['map']['grid'] if 
            cell['cell_type'] == 'batteries_spawn')['cell_coordinates']
        if agent['coordinates'][0] > battery_spawn[0]:
            function_1()
        elif agent['coordinates'][0] < battery_spawn[0]:
            function_2()
        elif agent['coordinates'][1] > battery_spawn[1]:
            function_3()
        else:
            function_4()
    else:
        parcel_spawn = next(cell for cell in belief_set['map']['grid'] if 
            cell['cell_type'] == 'parcels_spawn')['cell_coordinates']
        if agent['coordinates'][0] > parcel_spawn[0]:
            function_1()
        elif agent['coordinates'][0] < parcel_spawn[0]:
            function_2()
        elif agent['coordinates'][1] > parcel_spawn[1]:
            function_3()
        else:
            function_4()

def function_8():
    global belief_set
    agent_coordinates = belief_set['agent'][1]['coordinates']
    parcels_coordinates = belief_set['parcels'][1]['coordinates']
    while agent_coordinates[0] < parcels_coordinates[0]:
        function_2()
        agent_coordinates[0] += 1
    while agent_coordinates[0] > parcels_coordinates[0]:
        function_1()
        agent_coordinates[0] -= 1
    while agent_coordinates[1] < parcels_coordinates[1]:
        function_4()
        agent_coordinates[1] += 1
    while agent_coordinates[1] > parcels_coordinates[1]:
        function_3()
        agent_coordinates[1] -= 1
    function_5()

def function_9():
    global belief_set
    delivery_cell = next(cell for cell in belief_set['map']['grid'] if cell
        ['cell_type'] == 'delivery_cell')
    agent = belief_set['agent'][1]
    while agent['coordinates'] != delivery_cell['cell_coordinates']:
        if agent['coordinates'][0] < delivery_cell['cell_coordinates'][0]:
            function_2()
        elif agent['coordinates'][0] > delivery_cell['cell_coordinates'][0]:
            function_1()
        elif agent['coordinates'][1] < delivery_cell['cell_coordinates'][1]:
            function_4()
        else:
            function_3()
    function_6()
    return

def function_10():
    global belief_set
    delivery_cell = None
    for cell in belief_set['map']['grid']:
        if cell['cell_type'] == 'delivery_cell':
            delivery_cell = cell
            break
    agent = belief_set['agent'][1]
    while agent['coordinates'] != delivery_cell['cell_coordinates']:
        if agent['coordinates'][0] < delivery_cell['cell_coordinates'][0]:
            function_2()
        elif agent['coordinates'][0] > delivery_cell['cell_coordinates'][0]:
            function_1()
        elif agent['coordinates'][1] < delivery_cell['cell_coordinates'][1]:
            function_4()
        else:
            function_3()
    function_6()

def function_11():
    global belief_set
    delivery_cell = [item['cell_coordinates'] for item in belief_set['map']
        ['grid'] if item['cell_type'] == 'delivery_cell'][0]
    agent = belief_set['agent'][1]
    while agent['coordinates'] != delivery_cell:
        if agent['coordinates'][0] > delivery_cell[0]:
            function_1()
        elif agent['coordinates'][0] < delivery_cell[0]:
            function_2()
        elif agent['coordinates'][1] > delivery_cell[1]:
            function_3()
        elif agent['coordinates'][1] < delivery_cell[1]:
            function_4()
        agent = belief_set['agent'][1]
        if agent['coordinates'] == [item['cell_coordinates'] for item in
            belief_set['map']['grid'] if item['cell_type'] == 'batteries_spawn'
            ][0] and agent['energy'] < 50:
            function_5()
    function_6()

def function_12():
    global belief_set
    while belief_set['agent'][1]['coordinates'] != [0, 0]:
        if belief_set['agent'][1]['coordinates'][0] > 0:
            function_1()
        elif belief_set['agent'][1]['coordinates'][1] > 0:
            function_3()
    function_5()
    if belief_set['agent'][1]['energy'] < 50:
        while belief_set['agent'][1]['coordinates'] != [2, 0]:
            if belief_set['agent'][1]['coordinates'][0] < 2:
                function_2()
            elif belief_set['agent'][1]['coordinates'][1] > 0:
                function_3()
        function_5()
    while belief_set['agent'][1]['coordinates'] != [2, 3]:
        if belief_set['agent'][1]['coordinates'][0] < 2:
            function_2()
        elif belief_set['agent'][1]['coordinates'][1] < 3:
            function_4()
    function_6()

def function_13():
    global belief_set
    agent = belief_set['agent'][1]
    if agent['energy'] < 50:
        function_2()
        function_5()
    elif agent['coordinates'][0] < belief_set['map']['width'] - 1:
        function_2()
    elif agent['coordinates'][1] < belief_set['map']['height'] - 1:
        function_4()
    else:
        function_1()
        function_3()

def function_14():
    global belief_set
    agent = belief_set['agent'][1]
    if agent['energy'] < 50:
        function_2()
    else:
        function_12()

def function_15():
    global belief_set
    agent = belief_set['agent'][1]
    location = agent['coordinates']
    energy = agent['energy']
    if energy < 50:
        function_14()
    else:
        unexplored_cells = [cell for cell in belief_set['map']['grid'] if 
            cell['cell_type'] == 'walkable' and cell['cell_coordinates'] !=
            location]
        if unexplored_cells:
            nearest_cell = min(unexplored_cells, key=lambda cell: abs(cell[
                'cell_coordinates'][0] - location[0]) + abs(cell[
                'cell_coordinates'][1] - location[1]))
            while location != nearest_cell['cell_coordinates']:
                if nearest_cell['cell_coordinates'][0] < location[0]:
                    function_1()
                elif nearest_cell['cell_coordinates'][0] > location[0]:
                    function_2()
                elif nearest_cell['cell_coordinates'][1] < location[1]:
                    function_3()
                elif nearest_cell['cell_coordinates'][1] > location[1]:
                    function_4()
                location = belief_set['agent'][1]['coordinates']

def function_16():
    global belief_set
    if belief_set['agent'][1]['energy'] < 50:
        function_14()
    else:
        function_12()

def function_17():
    global belief_set
    agent = belief_set['agent'][1]
    if agent['energy'] < 50:
        function_14()
    elif agent['coordinates'][0] + 1 < belief_set['map']['width'] and {
        'cell_coordinates': [agent['coordinates'][0] + 1, agent[
        'coordinates'][1]], 'cell_type': 'walkable'} in belief_set['map'][
        'grid']:
        function_2()
    elif agent['coordinates'][0] - 1 >= 0 and {'cell_coordinates': [agent[
        'coordinates'][0] - 1, agent['coordinates'][1]], 'cell_type':
        'walkable'} in belief_set['map']['grid']:
        function_1()
    elif agent['coordinates'][1] + 1 < belief_set['map']['height'] and {
        'cell_coordinates': [agent['coordinates'][0], agent['coordinates'][
        1] + 1], 'cell_type': 'walkable'} in belief_set['map']['grid']:
        function_4()
    elif agent['coordinates'][1] - 1 >= 0 and {'cell_coordinates': [agent[
        'coordinates'][0], agent['coordinates'][1] - 1], 'cell_type':
        'walkable'} in belief_set['map']['grid']:
        function_3()

def function_18():
    global belief_set
    agent = belief_set['agent'][1]
    if agent['energy'] > 50:
        if not agent['parcels_carried_ids']:
            if belief_set['parcels'] and agent['coordinates'][0] > belief_set[
                'parcels'][list(belief_set['parcels'].keys())[0]]['coordinates'
                ][0]:
                function_1()
            elif belief_set['parcels'] and agent['coordinates'][0
                ] < belief_set['parcels'][list(belief_set['parcels'].keys())[0]
                ]['coordinates'][0]:
                function_2()
            elif belief_set['parcels'] and agent['coordinates'][1
                ] > belief_set['parcels'][list(belief_set['parcels'].keys())[0]
                ]['coordinates'][1]:
                function_3()
            elif belief_set['parcels'] and agent['coordinates'][1
                ] < belief_set['parcels'][list(belief_set['parcels'].keys())[0]
                ]['coordinates'][1]:
                function_4()
            else:
                function_5()
        elif agent['coordinates'][0] > belief_set['map']['grid'][11][
            'cell_coordinates'][0]:
            function_1()
        elif agent['coordinates'][0] < belief_set['map']['grid'][11][
            'cell_coordinates'][0]:
            function_2()
        elif agent['coordinates'][1] > belief_set['map']['grid'][11][
            'cell_coordinates'][1]:
            function_3()
        elif agent['coordinates'][1] < belief_set['map']['grid'][11][
            'cell_coordinates'][1]:
            function_4()
        else:
            function_6()
    elif belief_set['batteries'] and agent['coordinates'][0] > belief_set[
        'batteries'][list(belief_set['batteries'].keys())[0]]['coordinates'][0
        ]:
        function_1()
    elif belief_set['batteries'] and agent['coordinates'][0] < belief_set[
        'batteries'][list(belief_set['batteries'].keys())[0]]['coordinates'][0
        ]:
        function_2()
    elif belief_set['batteries'] and agent['coordinates'][1] > belief_set[
        'batteries'][list(belief_set['batteries'].keys())[0]]['coordinates'][1
        ]:
        function_3()
    elif belief_set['batteries'] and agent['coordinates'][1] < belief_set[
        'batteries'][list(belief_set['batteries'].keys())[0]]['coordinates'][1
        ]:
        function_4()
    else:
        function_5()

def function_19():
    global belief_set
    agent_location = belief_set['agent'][1]['coordinates']
    parcels_spawn_location = [cell['cell_coordinates'] for cell in
        belief_set['map']['grid'] if cell['cell_type'] == 'parcels_spawn'][0]
    batteries_spawn_location = [cell['cell_coordinates'] for cell in
        belief_set['map']['grid'] if cell['cell_type'] == 'batteries_spawn'][0]
    delivery_cell_location = [cell['cell_coordinates'] for cell in
        belief_set['map']['grid'] if cell['cell_type'] == 'delivery_cell'][0]
    while agent_location != parcels_spawn_location:
        if agent_location[0] < parcels_spawn_location[0]:
            function_2()
        elif agent_location[0] > parcels_spawn_location[0]:
            function_1()
        elif agent_location[1] < parcels_spawn_location[1]:
            function_4()
        else:
            function_3()
        function_5()
    while agent_location != batteries_spawn_location:
        if agent_location[0] < batteries_spawn_location[0]:
            function_2()
        elif agent_location[0] > batteries_spawn_location[0]:
            function_1()
        elif agent_location[1] < batteries_spawn_location[1]:
            function_4()
        else:
            function_3()
        if belief_set['agent'][1]['energy'] < 50:
            function_5()
    while agent_location != delivery_cell_location:
        if agent_location[0] < delivery_cell_location[0]:
            function_2()
        elif agent_location[0] > delivery_cell_location[0]:
            function_1()
        elif agent_location[1] < delivery_cell_location[1]:
            function_4()
        else:
            function_3()
    function_6()

def function_20():
    global belief_set
    agent = belief_set['agent'][1]
    parcels_spawn = next(cell['cell_coordinates'] for cell in belief_set[
        'map']['grid'] if cell['cell_type'] == 'parcels_spawn')
    batteries_spawn = next(cell['cell_coordinates'] for cell in belief_set[
        'map']['grid'] if cell['cell_type'] == 'batteries_spawn')
    delivery_cell = next(cell['cell_coordinates'] for cell in belief_set[
        'map']['grid'] if cell['cell_type'] == 'delivery_cell')
    while agent['coordinates'] != parcels_spawn:
        if agent['coordinates'][0] < parcels_spawn[0]:
            function_2()
        elif agent['coordinates'][0] > parcels_spawn[0]:
            function_1()
        elif agent['coordinates'][1] < parcels_spawn[1]:
            function_4()
        elif agent['coordinates'][1] > parcels_spawn[1]:
            function_3()
        agent = belief_set['agent'][1]
    function_5()
    while agent['coordinates'] != batteries_spawn:
        if agent['coordinates'][0] < batteries_spawn[0]:
            function_2()
        elif agent['coordinates'][0] > batteries_spawn[0]:
            function_1()
        elif agent['coordinates'][1] < batteries_spawn[1]:
            function_4()
        elif agent['coordinates'][1] > batteries_spawn[1]:
            function_3()
        agent = belief_set['agent'][1]
    if agent['energy'] < 50:
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
        agent = belief_set['agent'][1]
    function_6()

def function_21():
    global belief_set
    function_20()
    agent = belief_set['agent'][1]
    if agent['energy'] < 50:
        for cell in belief_set['map']['grid']:
            if cell['cell_type'] == 'batteries_spawn' and cell[
                'cell_coordinates'] == agent['coordinates']:
                function_5()
    function_11()

def function_22():
    global belief_set
    function_20()
    if belief_set['agent'][1]['energy'] < 50:
        function_5()
    function_11()
    function_6()

def function_23():
    global belief_set
    function_20()
    if belief_set['agent'][1]['energy'] < 50:
        function_5()
    function_11()

