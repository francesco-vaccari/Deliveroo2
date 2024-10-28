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
    parcel = belief_set['parcel'][1]
    map_grid = belief_set['map']['grid']
    spawn_points = [cell['cell_coordinates'] for cell in map_grid if cell[
        'cell_type'] == 'parcels_spawn']
    delivery_points = [cell['cell_coordinates'] for cell in map_grid if 
        cell['cell_type'] == 'delivery_cell']
    if parcel['carried_by_id'] is None and parcel['coordinates'] == agent[
        'coordinates']:
        function_5()
    elif parcel['carried_by_id'] == agent['id'] and agent['coordinates'
        ] in delivery_points:
        function_6()
    else:
        target = spawn_points[0] if parcel['carried_by_id'
            ] is None else delivery_points[0]
        if agent['coordinates'][0] > target[0]:
            function_1()
        elif agent['coordinates'][0] < target[0]:
            function_2()
        elif agent['coordinates'][1] > target[1]:
            function_3()
        elif agent['coordinates'][1] < target[1]:
            function_4()

def function_8():
    global belief_set
    spawn_point = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'parcels_spawn'][0]['cell_coordinates']
    delivery_point = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'delivery_cell'][0]['cell_coordinates']
    agent_position = belief_set['agent'][1]['coordinates']
    while agent_position != spawn_point:
        if spawn_point[0] < agent_position[0]:
            function_1()
        elif spawn_point[0] > agent_position[0]:
            function_2()
        elif spawn_point[1] < agent_position[1]:
            function_3()
        elif spawn_point[1] > agent_position[1]:
            function_4()
        agent_position = belief_set['agent'][1]['coordinates']
    function_5()
    while agent_position != delivery_point:
        if delivery_point[0] < agent_position[0]:
            function_1()
        elif delivery_point[0] > agent_position[0]:
            function_2()
        elif delivery_point[1] < agent_position[1]:
            function_3()
        elif delivery_point[1] > agent_position[1]:
            function_4()
        agent_position = belief_set['agent'][1]['coordinates']
    function_6()

