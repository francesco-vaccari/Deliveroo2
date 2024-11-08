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
    spawn_point = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'parcels_spawn'][0]['cell_coordinates']
    while belief_set['agent']['coordinates'] != spawn_point:
        if belief_set['agent']['coordinates'][0] < spawn_point[0]:
            function_2()
        elif belief_set['agent']['coordinates'][0] > spawn_point[0]:
            function_1()
        elif belief_set['agent']['coordinates'][1] < spawn_point[1]:
            function_4()
        elif belief_set['agent']['coordinates'][1] > spawn_point[1]:
            function_3()
    function_5()

def function_9():
    global belief_set
    current_coords = belief_set['agent']['coordinates']
    new_coords = [current_coords[0] - 1, current_coords[1]]
    for cell in belief_set['map']['grid']:
        if cell['cell_coordinates'] == new_coords and cell['cell_type'
            ] == 'walkable':
            if belief_set['agent']['energy'] > 10:
                function_1()
                break

def function_11():
    global belief_set
    max_actions = 10
    actions_taken = 0
    while actions_taken < max_actions:
        if 'parcels_carried_ids' in belief_set['agent'] and len(belief_set[
            'agent']['parcels_carried_ids']) > 0:
            for cell in belief_set['map']['grid']:
                if cell['cell_type'] == 'delivery_cell' and cell[
                    'cell_coordinates'] == belief_set['agent']['coordinates']:
                    function_6()
                    return
        for cell in belief_set['map']['grid']:
            if cell['cell_type'] == 'delivery_cell' and cell['cell_coordinates'
                ][0] > belief_set['agent']['coordinates'][0] and belief_set[
                'agent']['energy'] > 10:
                function_2()
                actions_taken += 1
            elif cell['cell_type'] == 'delivery_cell' and cell[
                'cell_coordinates'][0] < belief_set['agent']['coordinates'][0
                ] and belief_set['agent']['energy'] > 10:
                function_1()
                actions_taken += 1
            elif cell['cell_type'] == 'delivery_cell' and cell[
                'cell_coordinates'][1] > belief_set['agent']['coordinates'][1
                ] and belief_set['agent']['energy'] > 10:
                function_4()
                actions_taken += 1
            elif cell['cell_type'] == 'delivery_cell' and cell[
                'cell_coordinates'][1] < belief_set['agent']['coordinates'][1
                ] and belief_set['agent']['energy'] > 10:
                function_3()
                actions_taken += 1
        actions_taken += 1
    return

def function_24():
    global belief_set
    if belief_set['agent']['energy'] > 50:
        new_coordinates = [belief_set['agent']['coordinates'][0] + 1,
            belief_set['agent']['coordinates'][1]]
        for cell in belief_set['map']['grid']:
            if cell['cell_coordinates'] == new_coordinates and cell['cell_type'
                ] == 'walkable':
                function_2()
                break

