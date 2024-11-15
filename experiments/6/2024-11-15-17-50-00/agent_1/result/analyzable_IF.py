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
    parcels = belief_set['parcels']
    batteries = belief_set['batteries']
    if agent['energy'] < 30:
        for battery in batteries.values():
            while agent['coordinates'] != battery['coordinates']:
                if agent['coordinates'][0] < battery['coordinates'][0]:
                    function_2()
                elif agent['coordinates'][0] > battery['coordinates'][0]:
                    function_1()
                elif agent['coordinates'][1] < battery['coordinates'][1]:
                    function_4()
                else:
                    function_3()
        function_5()
    for parcel in parcels.values():
        if parcel['carried_by_id'] is None:
            while agent['coordinates'] != parcel['coordinates']:
                if agent['coordinates'][0] < parcel['coordinates'][0]:
                    function_2()
                elif agent['coordinates'][0] > parcel['coordinates'][0]:
                    function_1()
                elif agent['coordinates'][1] < parcel['coordinates'][1]:
                    function_4()
                else:
                    function_3()
            function_5()
            while agent['coordinates'] != [2, 3]:
                if agent['coordinates'][0] < 2:
                    function_2()
                elif agent['coordinates'][0] > 2:
                    function_1()
                elif agent['coordinates'][1] < 3:
                    function_4()
                else:
                    function_3()
            function_6()

def function_8():
    global belief_set
    agent = belief_set['agent'][1]
    parcels = belief_set['parcels']
    batteries = belief_set['batteries']
    map = belief_set['map']['grid']
    delivery_cell = next((cell for cell in map if cell['cell_type'] ==
        'delivery_cell'), None)
    battery_cell = next((cell for cell in map if cell['cell_type'] ==
        'batteries_spawn'), None)
    parcel_cell = next((cell for cell in map if cell['cell_type'] ==
        'parcels_spawn'), None)
    if agent['energy'] < 30 and battery_cell:
        if agent['coordinates'][0] < battery_cell['cell_coordinates'][0]:
            function_2()
        elif agent['coordinates'][0] > battery_cell['cell_coordinates'][0]:
            function_1()
        elif agent['coordinates'][1] < battery_cell['cell_coordinates'][1]:
            function_4()
        elif agent['coordinates'][1] > battery_cell['cell_coordinates'][1]:
            function_3()
        function_5()
    elif agent['parcels_carried_ids'] and delivery_cell:
        if agent['coordinates'][0] < delivery_cell['cell_coordinates'][0]:
            function_2()
        elif agent['coordinates'][0] > delivery_cell['cell_coordinates'][0]:
            function_1()
        elif agent['coordinates'][1] < delivery_cell['cell_coordinates'][1]:
            function_4()
        elif agent['coordinates'][1] > delivery_cell['cell_coordinates'][1]:
            function_3()
        function_6()
    elif parcels and parcel_cell:
        if agent['coordinates'][0] < parcel_cell['cell_coordinates'][0]:
            function_2()
        elif agent['coordinates'][0] > parcel_cell['cell_coordinates'][0]:
            function_1()
        elif agent['coordinates'][1] < parcel_cell['cell_coordinates'][1]:
            function_4()
        elif agent['coordinates'][1] > parcel_cell['cell_coordinates'][1]:
            function_3()
        function_5()

def function_9():
    global belief_set
    agent = belief_set['agent'][1]
    parcels = belief_set['parcels']
    batteries = belief_set['batteries']
    delivery_cell = next(cell for cell in belief_set['map']['grid'] if cell
        ['cell_type'] == 'delivery_cell')['cell_coordinates']
    if agent['energy'] < 30:
        battery_coordinates = batteries[1]['coordinates']
        if battery_coordinates[0] < agent['coordinates'][0]:
            function_1()
        elif battery_coordinates[0] > agent['coordinates'][0]:
            function_2()
        elif battery_coordinates[1] < agent['coordinates'][1]:
            function_3()
        else:
            function_4()
        function_5()
    for parcel_id, parcel in parcels.items():
        if parcel['carried_by_id'] == None:
            parcel_coordinates = parcel['coordinates']
            if parcel_coordinates[0] < agent['coordinates'][0]:
                function_1()
            elif parcel_coordinates[0] > agent['coordinates'][0]:
                function_2()
            elif parcel_coordinates[1] < agent['coordinates'][1]:
                function_3()
            else:
                function_4()
            function_5()
            break
    if agent['parcels_carried_ids']:
        if delivery_cell[0] < agent['coordinates'][0]:
            function_1()
        elif delivery_cell[0] > agent['coordinates'][0]:
            function_2()
        elif delivery_cell[1] < agent['coordinates'][1]:
            function_3()
        else:
            function_4()
        function_6()

def function_10():
    global belief_set
    agent = belief_set['agent'][1]
    map_grid = belief_set['map']['grid']
    delivery_cell = next(cell for cell in map_grid if cell['cell_type'] ==
        'delivery_cell')
    battery_spawn = next(cell for cell in map_grid if cell['cell_type'] ==
        'batteries_spawn')
    if agent['energy'] < 30:
        if agent['coordinates'][0] < battery_spawn['cell_coordinates'][0]:
            function_2()
        elif agent['coordinates'][0] > battery_spawn['cell_coordinates'][0]:
            function_1()
        elif agent['coordinates'][1] < battery_spawn['cell_coordinates'][1]:
            function_4()
        else:
            function_3()
    else:
        if agent['coordinates'][0] < delivery_cell['cell_coordinates'][0]:
            function_2()
        elif agent['coordinates'][0] > delivery_cell['cell_coordinates'][0]:
            function_1()
        elif agent['coordinates'][1] < delivery_cell['cell_coordinates'][1]:
            function_4()
        else:
            function_3()
        if agent['coordinates'] == delivery_cell['cell_coordinates']:
            function_6()

def function_11():
    global belief_set
    agent = belief_set['agent'][1]
    agent_coords = agent['coordinates']
    if agent['energy'] < 30:
        battery_coords = belief_set['batteries'][1]['coordinates']
        if agent_coords[0] < battery_coords[0]:
            function_2()
        elif agent_coords[0] > battery_coords[0]:
            function_1()
        elif agent_coords[1] < battery_coords[1]:
            function_4()
        else:
            function_3()
    else:
        delivery_coords = [2, 3]
        if agent_coords[0] < delivery_coords[0]:
            function_2()
        elif agent_coords[0] > delivery_coords[0]:
            function_1()
        elif agent_coords[1] < delivery_coords[1]:
            function_4()
        else:
            function_3()
            function_6()

def function_12():
    global belief_set
    agent = belief_set['agent'][1]
    delivery_cell = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'delivery_cell'][0]['cell_coordinates']
    if agent['coordinates'][0] < delivery_cell[0]:
        function_2()
    elif agent['coordinates'][0] > delivery_cell[0]:
        function_1()
    elif agent['coordinates'][1] < delivery_cell[1]:
        function_4()
    elif agent['coordinates'][1] > delivery_cell[1]:
        function_3()
    if belief_set['batteries'][1]['coordinates'] == agent['coordinates'
        ] and agent['energy'] < 50:
        function_5()
    if any(parcel['coordinates'] == agent['coordinates'] and parcel[
        'carried_by_id'] is None for parcel in belief_set['parcels'].values()):
        function_5()
    if agent['coordinates'] == delivery_cell and agent['parcels_carried_ids']:
        function_6()

def function_13():
    global belief_set
    delivery_cell_coordinates = None
    for cell in belief_set['map']['grid']:
        if cell['cell_type'] == 'delivery_cell':
            delivery_cell_coordinates = cell['cell_coordinates']
    while belief_set['agent'][1]['coordinates'] != delivery_cell_coordinates:
        if belief_set['agent'][1]['coordinates'][0
            ] > delivery_cell_coordinates[0]:
            function_1()
        elif belief_set['agent'][1]['coordinates'][0
            ] < delivery_cell_coordinates[0]:
            function_2()
        elif belief_set['agent'][1]['coordinates'][1
            ] > delivery_cell_coordinates[1]:
            function_3()
        else:
            function_4()
    function_6()

def function_14():
    global belief_set
    battery_spawn_coordinates = next(cell['cell_coordinates'] for cell in
        belief_set['map']['grid'] if cell['cell_type'] == 'batteries_spawn')
    while belief_set['agent'][1]['coordinates'] != battery_spawn_coordinates:
        if belief_set['agent'][1]['coordinates'][0
            ] > battery_spawn_coordinates[0]:
            function_1()
        elif belief_set['agent'][1]['coordinates'][0
            ] < battery_spawn_coordinates[0]:
            function_2()
        elif belief_set['agent'][1]['coordinates'][1
            ] > battery_spawn_coordinates[1]:
            function_3()
        elif belief_set['agent'][1]['coordinates'][1
            ] < battery_spawn_coordinates[1]:
            function_4()
    function_5()

def function_15():
    global belief_set
    parcel_spawn_location = [cell['cell_coordinates'] for cell in
        belief_set['map']['grid'] if cell['cell_type'] == 'parcels_spawn'][0]
    agent_location = belief_set['agent'][1]['coordinates']
    while agent_location[0] > parcel_spawn_location[0]:
        function_1()
        agent_location[0] -= 1
    while agent_location[0] < parcel_spawn_location[0]:
        function_2()
        agent_location[0] += 1
    while agent_location[1] > parcel_spawn_location[1]:
        function_3()
        agent_location[1] -= 1
    while agent_location[1] < parcel_spawn_location[1]:
        function_4()
        agent_location[1] += 1
    function_5()
    delivery_cell_location = [cell['cell_coordinates'] for cell in
        belief_set['map']['grid'] if cell['cell_type'] == 'delivery_cell'][0]
    while agent_location[0] > delivery_cell_location[0]:
        function_1()
        agent_location[0] -= 1
    while agent_location[0] < delivery_cell_location[0]:
        function_2()
        agent_location[0] += 1
    while agent_location[1] > delivery_cell_location[1]:
        function_3()
        agent_location[1] -= 1
    while agent_location[1] < delivery_cell_location[1]:
        function_4()
        agent_location[1] += 1
    function_6()

def function_16():
    global belief_set
    agent = belief_set['agent'][1]
    locations = {'parcels_spawn': [], 'batteries_spawn': [],
        'delivery_cell': []}
    for cell in belief_set['map']['grid']:
        if cell['cell_type'] in locations:
            locations[cell['cell_type']].append(cell['cell_coordinates'])
    for location in locations.values():
        if location:
            closest = min(location, key=lambda x: abs(x[0] - agent[
                'coordinates'][0]) + abs(x[1] - agent['coordinates'][1]))
            if closest[0] < agent['coordinates'][0]:
                function_1()
            elif closest[0] > agent['coordinates'][0]:
                function_2()
            elif closest[1] < agent['coordinates'][1]:
                function_3()
            elif closest[1] > agent['coordinates'][1]:
                function_4()

def function_17():
    global belief_set
    function_15()
    while belief_set['agent'][1]['parcels_carried_ids']:
        function_13()

def function_18():
    global belief_set
    function_15()

def function_19():
    global belief_set
    function_15()
    if belief_set['agent'][1]['parcels_carried_ids']:
        function_13()

def function_20():
    global belief_set
    function_15()
    return

def function_21():
    global belief_set
    function_14()
    function_5()

def function_22():
    global belief_set
    battery_spawn_location = [cell['cell_coordinates'] for cell in
        belief_set['map']['grid'] if cell['cell_type'] == 'batteries_spawn'][0]
    agent_location = belief_set['agent'][1]['coordinates']
    while agent_location != battery_spawn_location:
        if agent_location[0] < battery_spawn_location[0]:
            function_2()
        elif agent_location[0] > battery_spawn_location[0]:
            function_1()
        elif agent_location[1] < battery_spawn_location[1]:
            function_4()
        elif agent_location[1] > battery_spawn_location[1]:
            function_3()
        if belief_set['agent'][1]['coordinates'] == agent_location:
            break
        else:
            agent_location = belief_set['agent'][1]['coordinates']
    function_5()

