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


def function_8():
    global belief_set
    agent_position = belief_set['agent'][1]['coordinates']
    parcel_spawn_location = [cell['cell_coordinates'] for cell in
        belief_set['map']['grid'] if cell['cell_type'] == 'parcels_spawn'][0]
    delivery_cell = [cell['cell_coordinates'] for cell in belief_set['map']
        ['grid'] if cell['cell_type'] == 'delivery_cell'][0]
    max_iterations = 1000
    i = 0
    while agent_position != parcel_spawn_location and i < max_iterations:
        i += 1
        if agent_position[0] < parcel_spawn_location[0]:
            function_2()
            agent_position[0] += 1
        elif agent_position[0] > parcel_spawn_location[0]:
            function_1()
            agent_position[0] -= 1
        elif agent_position[1] < parcel_spawn_location[1]:
            function_4()
            agent_position[1] += 1
        elif agent_position[1] > parcel_spawn_location[1]:
            function_3()
            agent_position[1] -= 1
    function_5()
    i = 0
    while agent_position != delivery_cell and i < max_iterations:
        i += 1
        if agent_position[0] < delivery_cell[0]:
            function_2()
            agent_position[0] += 1
        elif agent_position[0] > delivery_cell[0]:
            function_1()
            agent_position[0] -= 1
        elif agent_position[1] < delivery_cell[1]:
            function_4()
            agent_position[1] += 1
        elif agent_position[1] > delivery_cell[1]:
            function_3()
            agent_position[1] -= 1
    function_6()

def function_12():
    global belief_set
    min_distance = float('inf')
    nearest_parcel = None
    for parcel_id, parcel_info in belief_set['parcels'].items():
        if parcel_info['carried_by_id'] is None:
            distance = abs(belief_set['agent'][1]['coordinates'][0] -
                parcel_info['coordinates'][0]) + abs(belief_set['agent'][1]
                ['coordinates'][1] - parcel_info['coordinates'][1])
            if distance < min_distance:
                min_distance = distance
                nearest_parcel = parcel_info
    while belief_set['agent'][1]['coordinates'] != nearest_parcel['coordinates'
        ]:
        if belief_set['agent'][1]['coordinates'][0] > nearest_parcel[
            'coordinates'][0]:
            function_1()
        elif belief_set['agent'][1]['coordinates'][0] < nearest_parcel[
            'coordinates'][0]:
            function_2()
        elif belief_set['agent'][1]['coordinates'][1] > nearest_parcel[
            'coordinates'][1]:
            function_3()
        else:
            function_4()
    function_5()
    for cell in belief_set['map']['grid']:
        if cell['cell_type'] == 'delivery_cell':
            delivery_cell = cell
            break
    while belief_set['agent'][1]['coordinates'] != delivery_cell[
        'cell_coordinates']:
        if belief_set['agent'][1]['coordinates'][0] > delivery_cell[
            'cell_coordinates'][0]:
            function_1()
        elif belief_set['agent'][1]['coordinates'][0] < delivery_cell[
            'cell_coordinates'][0]:
            function_2()
        elif belief_set['agent'][1]['coordinates'][1] > delivery_cell[
            'cell_coordinates'][1]:
            function_3()
        else:
            function_4()
    function_6()

