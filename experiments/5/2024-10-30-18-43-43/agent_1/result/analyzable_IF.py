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
    agent_location = belief_set['agent'][1]['coordinates']
    parcel_spawn_location = [cell['cell_coordinates'] for cell in
        belief_set['map']['grid'] if cell['cell_type'] == 'parcels_spawn'][0]
    delivery_location = [cell['cell_coordinates'] for cell in belief_set[
        'map']['grid'] if cell['cell_type'] == 'delivery_cell'][0]
    while agent_location != parcel_spawn_location:
        if agent_location[0] > parcel_spawn_location[0]:
            function_1()
        elif agent_location[0] < parcel_spawn_location[0]:
            function_2()
        if agent_location[1] > parcel_spawn_location[1]:
            function_3()
        elif agent_location[1] < parcel_spawn_location[1]:
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

def function_8():
    global belief_set
    parcel_spawn = [cell['cell_coordinates'] for cell in belief_set['map'][
        'grid'] if cell['cell_type'] == 'parcels_spawn'][0]
    delivery_cell = [cell['cell_coordinates'] for cell in belief_set['map']
        ['grid'] if cell['cell_type'] == 'delivery_cell'][0]
    agent_coordinates = belief_set['agent'][1]['coordinates']
    while agent_coordinates != parcel_spawn:
        if agent_coordinates[0] < parcel_spawn[0]:
            function_2()
        elif agent_coordinates[0] > parcel_spawn[0]:
            function_1()
        if agent_coordinates[1] < parcel_spawn[1]:
            function_4()
        elif agent_coordinates[1] > parcel_spawn[1]:
            function_3()
    function_5()
    while agent_coordinates != delivery_cell:
        if agent_coordinates[0] < delivery_cell[0]:
            function_2()
        elif agent_coordinates[0] > delivery_cell[0]:
            function_1()
        if agent_coordinates[1] < delivery_cell[1]:
            function_4()
        elif agent_coordinates[1] > delivery_cell[1]:
            function_3()
    function_6()

def function_9():
    global belief_set
    agent = belief_set['agent'][1]
    parcel_spawn = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'parcels_spawn'][0]
    delivery_cell = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'delivery_cell'][0]
    while agent['coordinates'] != parcel_spawn['cell_coordinates']:
        if agent['coordinates'][0] < parcel_spawn['cell_coordinates'][0]:
            function_2()
        elif agent['coordinates'][0] > parcel_spawn['cell_coordinates'][0]:
            function_1()
        if agent['coordinates'][1] < parcel_spawn['cell_coordinates'][1]:
            function_4()
        elif agent['coordinates'][1] > parcel_spawn['cell_coordinates'][1]:
            function_3()
        agent['coordinates'] = [agent['coordinates'][0] + (parcel_spawn[
            'cell_coordinates'][0] - agent['coordinates'][0]), agent[
            'coordinates'][1] + (parcel_spawn['cell_coordinates'][1] -
            agent['coordinates'][1])]
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
        agent['coordinates'] = [agent['coordinates'][0] + (delivery_cell[
            'cell_coordinates'][0] - agent['coordinates'][0]), agent[
            'coordinates'][1] + (delivery_cell['cell_coordinates'][1] -
            agent['coordinates'][1])]
    function_6()

def function_10():
    global belief_set
    parcel_spawn = [item for item in belief_set['map']['grid'] if item[
        'cell_type'] == 'parcels_spawn'][0]['cell_coordinates']
    delivery_cell = [item for item in belief_set['map']['grid'] if item[
        'cell_type'] == 'delivery_cell'][0]['cell_coordinates']
    agent_location = belief_set['agent'][1]['coordinates']
    while agent_location != parcel_spawn:
        if parcel_spawn[0] < agent_location[0]:
            function_1()
        elif parcel_spawn[0] > agent_location[0]:
            function_2()
        elif parcel_spawn[1] < agent_location[1]:
            function_3()
        elif parcel_spawn[1] > agent_location[1]:
            function_4()
    function_5()
    while agent_location != delivery_cell:
        if delivery_cell[0] < agent_location[0]:
            function_1()
        elif delivery_cell[0] > agent_location[0]:
            function_2()
        elif delivery_cell[1] < agent_location[1]:
            function_3()
        elif delivery_cell[1] > agent_location[1]:
            function_4()
    function_6()

def function_11():
    global belief_set
    agent = belief_set['agent'][1]
    parcels = belief_set['parcels']
    for parcel_id, parcel_info in parcels.items():
        if parcel_info['carried_by_id'] is None:
            if parcel_info['coordinates'][0] < agent['coordinates'][0]:
                function_1()
                break
            elif parcel_info['coordinates'][0] > agent['coordinates'][0]:
                function_2()
                break
            elif parcel_info['coordinates'][1] < agent['coordinates'][1]:
                function_3()
                break
            elif parcel_info['coordinates'][1] > agent['coordinates'][1]:
                function_4()
                break
    function_5()
    for cell_info in belief_set['map']['grid']:
        if cell_info['cell_type'] == 'delivery_cell':
            if cell_info['cell_coordinates'][0] < agent['coordinates'][0]:
                function_1()
                break
            elif cell_info['cell_coordinates'][0] > agent['coordinates'][0]:
                function_2()
                break
            elif cell_info['cell_coordinates'][1] < agent['coordinates'][1]:
                function_3()
                break
            elif cell_info['cell_coordinates'][1] > agent['coordinates'][1]:
                function_4()
                break

def function_12():
    global belief_set
    agent = belief_set['agent'][1]
    spawn_point = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'parcels_spawn'][0]['cell_coordinates']
    if agent['coordinates'] != spawn_point:
        if agent['coordinates'][0] > spawn_point[0]:
            function_1()
        elif agent['coordinates'][0] < spawn_point[0]:
            function_2()
        elif agent['coordinates'][1] > spawn_point[1]:
            function_3()
        else:
            function_4()
    function_5()

def function_13():
    global belief_set
    agent = belief_set['agent'][1]
    map_grid = belief_set['map']['grid']
    delivery_cell_coordinates = next(cell['cell_coordinates'] for cell in
        map_grid if cell['cell_type'] == 'delivery_cell')
    while agent['coordinates'] != delivery_cell_coordinates:
        if agent['coordinates'][0] < delivery_cell_coordinates[0]:
            function_2()
        elif agent['coordinates'][0] > delivery_cell_coordinates[0]:
            function_1()
        if agent['coordinates'][1] < delivery_cell_coordinates[1]:
            function_4()
        elif agent['coordinates'][1] > delivery_cell_coordinates[1]:
            function_3()
    function_6()

def function_14():
    global belief_set
    spawn_point = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'parcels_spawn'][0]['cell_coordinates']
    delivery_point = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'delivery_cell'][0]['cell_coordinates']
    agent_location = belief_set['agent'][1]['coordinates']
    while agent_location != spawn_point:
        if agent_location[0] < spawn_point[0]:
            function_2()
        elif agent_location[0] > spawn_point[0]:
            function_1()
        elif agent_location[1] < spawn_point[1]:
            function_4()
        else:
            function_3()
        agent_location = belief_set['agent'][1]['coordinates']
    function_5()
    while agent_location != delivery_point:
        if agent_location[0] < delivery_point[0]:
            function_2()
        elif agent_location[0] > delivery_point[0]:
            function_1()
        elif agent_location[1] < delivery_point[1]:
            function_4()
        else:
            function_3()
        agent_location = belief_set['agent'][1]['coordinates']
    function_6()

def function_15():
    global belief_set
    agent = belief_set['agent'][1]
    parcel_spawn = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'parcels_spawn'][0]['cell_coordinates']
    delivery_cell = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'delivery_cell'][0]['cell_coordinates']
    if not agent['parcels_carried_ids']:
        if agent['coordinates'][0] < parcel_spawn[0]:
            function_2()
        elif agent['coordinates'][0] > parcel_spawn[0]:
            function_1()
        elif agent['coordinates'][1] < parcel_spawn[1]:
            function_4()
        elif agent['coordinates'][1] > parcel_spawn[1]:
            function_3()
        else:
            function_5()
    elif agent['coordinates'][0] < delivery_cell[0]:
        function_2()
    elif agent['coordinates'][0] > delivery_cell[0]:
        function_1()
    elif agent['coordinates'][1] < delivery_cell[1]:
        function_4()
    elif agent['coordinates'][1] > delivery_cell[1]:
        function_3()
    else:
        function_6()

def function_16():
    global belief_set
    agent_coordinates = belief_set['agent'][1]['coordinates']
    parcels_coordinates = [p['coordinates'] for p in belief_set['parcels'].
        values() if p['carried_by_id'] == None]
    parcel_coordinates = min(parcels_coordinates, key=lambda c: abs(c[0] -
        agent_coordinates[0]) + abs(c[1] - agent_coordinates[1]))
    while agent_coordinates != parcel_coordinates:
        if agent_coordinates[0] > parcel_coordinates[0]:
            function_1()
            agent_coordinates[0] -= 1
        elif agent_coordinates[0] < parcel_coordinates[0]:
            function_2()
            agent_coordinates[0] += 1
        elif agent_coordinates[1] > parcel_coordinates[1]:
            function_3()
            agent_coordinates[1] -= 1
        elif agent_coordinates[1] < parcel_coordinates[1]:
            function_4()
            agent_coordinates[1] += 1
    function_5()
    delivery_coordinates = [cell['cell_coordinates'] for cell in belief_set
        ['map']['grid'] if cell['cell_type'] == 'delivery_cell'][0]
    while agent_coordinates != delivery_coordinates:
        if agent_coordinates[0] > delivery_coordinates[0]:
            function_1()
            agent_coordinates[0] -= 1
        elif agent_coordinates[0] < delivery_coordinates[0]:
            function_2()
            agent_coordinates[0] += 1
        elif agent_coordinates[1] > delivery_coordinates[1]:
            function_3()
            agent_coordinates[1] -= 1
        elif agent_coordinates[1] < delivery_coordinates[1]:
            function_4()
            agent_coordinates[1] += 1
    function_6()

def function_17():
    global belief_set
    agent = belief_set['agent'][1]
    delivery_cell = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'delivery_cell'][0]
    if agent['parcels_carried_ids']:
        if agent['coordinates'][0] > delivery_cell['cell_coordinates'][0]:
            function_1()
        elif agent['coordinates'][0] < delivery_cell['cell_coordinates'][0]:
            function_2()
        elif agent['coordinates'][1] > delivery_cell['cell_coordinates'][1]:
            function_3()
        elif agent['coordinates'][1] < delivery_cell['cell_coordinates'][1]:
            function_4()
        if agent['coordinates'] == delivery_cell['cell_coordinates']:
            function_6()

