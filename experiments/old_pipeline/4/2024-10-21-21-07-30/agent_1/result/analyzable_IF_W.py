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
    key_coordinates = belief_set['key'][1]['coordinates']
    agent_coordinates = belief_set['agent']['coordinates']
    while agent_coordinates[0] < key_coordinates[0]:
        function_2()
        agent_coordinates = belief_set['agent']['coordinates']
    while agent_coordinates[0] > key_coordinates[0]:
        function_1()
        agent_coordinates = belief_set['agent']['coordinates']
    while agent_coordinates[1] < key_coordinates[1]:
        function_4()
        agent_coordinates = belief_set['agent']['coordinates']
    while agent_coordinates[1] > key_coordinates[1]:
        function_3()
        agent_coordinates = belief_set['agent']['coordinates']
    function_5()

def function_9():
    global belief_set
    agent = belief_set['agent']
    parcels = belief_set['parcel']
    for parcel in parcels.values():
        if parcel['coordinates'] == agent['coordinates'] and not agent[
            'parcels_carried_ids']:
            function_5()
            break

def function_19():
    global belief_set
    agent = belief_set['agent']
    parcel = belief_set['parcel'][1]
    map = belief_set['map']['grid']
    delivery_cells = [cell for cell in map if cell['cell_type'] in [
        'delivery_cell', 'double_delivery_cell']]
    target_cell = min(delivery_cells, key=lambda cell: abs(cell[
        'cell_coordinates'][0] - agent['coordinates'][0]) + abs(cell[
        'cell_coordinates'][1] - agent['coordinates'][1]))
    if target_cell['cell_coordinates'][0] > agent['coordinates'][0]:
        function_2()
    elif target_cell['cell_coordinates'][0] < agent['coordinates'][0]:
        function_1()
    elif target_cell['cell_coordinates'][1] > agent['coordinates'][1]:
        function_4()
    elif target_cell['cell_coordinates'][1] < agent['coordinates'][1]:
        function_3()
    elif parcel['id'] in agent['parcels_carried_ids']:
        function_6()

