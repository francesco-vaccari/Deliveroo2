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


def function_9():
    global belief_set
    agent = belief_set['agents'][1]
    if not agent['parcels_carried_ids']:
        parcel = min(belief_set['parcels'].values(), key=lambda p: abs(p[
            'coordinates'][0] - agent['coordinates'][0]) + abs(p[
            'coordinates'][1] - agent['coordinates'][1]))
        dx = parcel['coordinates'][0] - agent['coordinates'][0]
        dy = parcel['coordinates'][1] - agent['coordinates'][1]
        if dx > 0:
            function_2()
        elif dx < 0:
            function_1()
        elif dy > 0:
            function_4()
        elif dy < 0:
            function_3()
        if parcel['coordinates'] == agent['coordinates']:
            function_5()

def function_18():
    global belief_set
    agent = belief_set['agents'][1]
    key = belief_set['keys'][1]
    previous_coordinates = agent['coordinates'].copy()
    while agent['coordinates'] != key['coordinates'] or not agent['has_key']:
        if agent['coordinates'][0] < key['coordinates'][0]:
            function_2()
        elif agent['coordinates'][0] > key['coordinates'][0]:
            function_1()
        elif agent['coordinates'][1] < key['coordinates'][1]:
            function_4()
        elif agent['coordinates'][1] > key['coordinates'][1]:
            function_3()
        if agent['coordinates'] == key['coordinates'] and not agent['has_key']:
            function_5()
        if agent['coordinates'] == previous_coordinates:
            break
        previous_coordinates = agent['coordinates'].copy()

def function_21():
    global belief_set
    if len(belief_set['agents'][1]['parcels_carried_ids']) == 0:
        function_9()
    else:
        parcel_coord = belief_set['parcels'][belief_set['agents'][1][
            'parcels_carried_ids'][0]]['coordinates']
        delivery_cells = [cell for cell in belief_set['map']['grid'] if 
            cell['cell_type'] in ['delivery_cell',
            'double_points_delivery_cell']]
        delivery_cells.sort(key=lambda cell: abs(cell['cell_coordinates'][0
            ] - parcel_coord[0]) + abs(cell['cell_coordinates'][1] -
            parcel_coord[1]))
        target_delivery_cell = delivery_cells[0]
        while belief_set['agents'][1]['coordinates'] != target_delivery_cell[
            'cell_coordinates']:
            if belief_set['agents'][1]['coordinates'][0
                ] > target_delivery_cell['cell_coordinates'][0]:
                function_1()
            elif belief_set['agents'][1]['coordinates'][0
                ] < target_delivery_cell['cell_coordinates'][0]:
                function_2()
            elif belief_set['agents'][1]['coordinates'][1
                ] > target_delivery_cell['cell_coordinates'][1]:
                function_3()
            elif belief_set['agents'][1]['coordinates'][1
                ] < target_delivery_cell['cell_coordinates'][1]:
                function_4()
            if belief_set['agents'][1]['coordinates'] in [door[
                'coordinates'] for door in belief_set['doors'].values()
                ] and belief_set['agents'][1]['has_key']:
                function_18()
        function_6()

