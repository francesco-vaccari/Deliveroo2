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
    spawn_point = [cell['cell_coordinates'] for cell in belief_set['map'][
        'grid'] if cell['cell_type'] == 'parcels_spawn'][0]
    agent_coordinates = belief_set['agent']['coordinates']
    while agent_coordinates != spawn_point:
        if agent_coordinates[0] > spawn_point[0]:
            function_1()
        elif agent_coordinates[0] < spawn_point[0]:
            function_2()
        elif agent_coordinates[1] > spawn_point[1]:
            function_3()
        elif agent_coordinates[1] < spawn_point[1]:
            function_4()
        agent_coordinates = belief_set['agent']['coordinates']
    function_5()

def function_14():
    global belief_set
    agent_coords = belief_set['agent']['coordinates']
    parcel_coords = belief_set['parcel'][1]['coordinates']
    delivery_coords = [cell['cell_coordinates'] for cell in belief_set[
        'map']['grid'] if cell['cell_type'] in ['delivery_cell',
        'double_delivery_cell']][0]
    while agent_coords != delivery_coords:
        if agent_coords[0] < delivery_coords[0]:
            function_2()
            agent_coords[0] += 1
        elif agent_coords[0] > delivery_coords[0]:
            function_1()
            agent_coords[0] -= 1
        elif agent_coords[1] < delivery_coords[1]:
            function_4()
            agent_coords[1] += 1
        elif agent_coords[1] > delivery_coords[1]:
            function_3()
            agent_coords[1] -= 1
    function_6()

