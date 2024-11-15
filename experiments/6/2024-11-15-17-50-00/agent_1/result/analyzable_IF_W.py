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

def function_17():
    global belief_set
    function_15()
    while belief_set['agent'][1]['parcels_carried_ids']:
        function_13()

def function_19():
    global belief_set
    function_15()
    if belief_set['agent'][1]['parcels_carried_ids']:
        function_13()

