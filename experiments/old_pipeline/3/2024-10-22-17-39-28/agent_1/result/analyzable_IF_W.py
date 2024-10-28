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
    parcel_id = belief_set['agent'][1]['parcels_carried_ids']
    agent_coordinates = belief_set['agent'][1]['coordinates']
    if parcel_id and parcel_id[0] not in belief_set['parcels'].keys():
        function_5()
    delivery_cells = [cell['cell_coordinates'] for cell in belief_set['map'
        ]['grid'] if 'delivery' in cell['cell_type']]
    nearest_delivery_cell = min(delivery_cells, key=lambda x: abs(x[0] -
        agent_coordinates[0]) + abs(x[1] - agent_coordinates[1]))
    if nearest_delivery_cell[0] < agent_coordinates[0]:
        function_1()
    elif nearest_delivery_cell[0] > agent_coordinates[0]:
        function_2()
    elif nearest_delivery_cell[1] < agent_coordinates[1]:
        function_3()
    elif nearest_delivery_cell[1] > agent_coordinates[1]:
        function_4()
    if not parcel_id or parcel_id[0] not in belief_set['parcels'].keys():
        function_5()

