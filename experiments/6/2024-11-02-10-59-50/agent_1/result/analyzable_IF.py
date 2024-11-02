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
    agent_loc = belief_set['agent'][1]['coordinates']
    parcel_loc = belief_set['parcels'][1]['coordinates']
    delivery_loc = [cell['cell_coordinates'] for cell in belief_set['map'][
        'grid'] if cell['cell_type'] == 'delivery_cell'][0]
    while agent_loc != parcel_loc:
        if agent_loc[0] < parcel_loc[0]:
            function_2()
        elif agent_loc[0] > parcel_loc[0]:
            function_1()
        elif agent_loc[1] < parcel_loc[1]:
            function_4()
        else:
            function_3()
        agent_loc = belief_set['agent'][1]['coordinates']
    function_5()
    while agent_loc != delivery_loc:
        if agent_loc[0] < delivery_loc[0]:
            function_2()
        elif agent_loc[0] > delivery_loc[0]:
            function_1()
        elif agent_loc[1] < delivery_loc[1]:
            function_4()
        else:
            function_3()
        agent_loc = belief_set['agent'][1]['coordinates']
    function_6()

def function_8():
    global belief_set
    agent = belief_set['agent'][1]
    parcel_spawn_cell = [cell for cell in belief_set['map']['grid'] if cell
        ['cell_type'] == 'parcels_spawn'][0]
    parcel_spawn_coordinates = parcel_spawn_cell['cell_coordinates']
    while agent['coordinates'] != parcel_spawn_coordinates:
        if agent['coordinates'][0] > parcel_spawn_coordinates[0]:
            function_1()
        elif agent['coordinates'][0] < parcel_spawn_coordinates[0]:
            function_2()
        elif agent['coordinates'][1] > parcel_spawn_coordinates[1]:
            function_3()
        elif agent['coordinates'][1] < parcel_spawn_coordinates[1]:
            function_4()
    function_5()

def function_9():
    global belief_set
    agent = belief_set['agent'][1]
    target_cell = None
    for cell in belief_set['map']['grid']:
        if cell['cell_type'] == 'parcels_spawn':
            target_cell = cell['cell_coordinates']
    if target_cell is None:
        return
    x_diff = target_cell[0] - agent['coordinates'][0]
    y_diff = target_cell[1] - agent['coordinates'][1]
    attempt_count = 0
    while agent['coordinates'] != target_cell and attempt_count < 100:
        if x_diff > 0:
            function_2()
            x_diff -= 1
        elif x_diff < 0:
            function_1()
            x_diff += 1
        if y_diff > 0:
            function_4()
            y_diff -= 1
        elif y_diff < 0:
            function_3()
            y_diff += 1
        attempt_count += 1

def function_10():
    global belief_set
    agent = belief_set['agent'][1]
    battery_spawn = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'batteries_spawn'][0]['cell_coordinates']
    if agent['energy'] < 30:
        if agent['coordinates'] == battery_spawn:
            function_5()
        else:
            function_9()
    elif agent['coordinates'][0] < battery_spawn[0]:
        function_2()
    elif agent['coordinates'][0] > battery_spawn[0]:
        function_1()
    elif agent['coordinates'][1] < battery_spawn[1]:
        function_4()
    elif agent['coordinates'][1] > battery_spawn[1]:
        function_3()

def function_11():
    global belief_set
    agent_coordinates = belief_set['agent'][1]['coordinates']
    for cell in belief_set['map']['grid']:
        if cell['cell_type'] == 'parcels_spawn':
            spawn_coordinates = cell['cell_coordinates']
            break
    if agent_coordinates == spawn_coordinates:
        function_5()
    else:
        function_9()

def function_12():
    global belief_set
    current_position = belief_set['agent'][1]['coordinates']
    parcel_spawn = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'parcels_spawn'][0]['cell_coordinates']
    delivery_cell = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'delivery_cell'][0]['cell_coordinates']
    while current_position != parcel_spawn:
        if parcel_spawn[0] < current_position[0]:
            function_1()
        elif parcel_spawn[0] > current_position[0]:
            function_2()
        if parcel_spawn[1] < current_position[1]:
            function_3()
        elif parcel_spawn[1] > current_position[1]:
            function_4()
        current_position = belief_set['agent'][1]['coordinates']
    function_5()
    while current_position != delivery_cell:
        if delivery_cell[0] < current_position[0]:
            function_1()
        elif delivery_cell[0] > current_position[0]:
            function_2()
        if delivery_cell[1] < current_position[1]:
            function_3()
        elif delivery_cell[1] > current_position[1]:
            function_4()
        current_position = belief_set['agent'][1]['coordinates']
    function_6()

def function_13():
    global belief_set
    function_9()
    function_5()
    function_12()
    function_6()

