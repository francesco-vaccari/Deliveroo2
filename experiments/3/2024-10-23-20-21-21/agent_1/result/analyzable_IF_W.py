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


def function_11():
    global belief_set
    key_coordinates = belief_set['keys'][1]['coordinates']
    agent_coordinates = belief_set['agent']['coordinates']
    counter = 0
    while agent_coordinates != key_coordinates and counter < 100:
        if agent_coordinates[0] < key_coordinates[0]:
            function_2()
        elif agent_coordinates[0] > key_coordinates[0]:
            function_1()
        if agent_coordinates[1] < key_coordinates[1]:
            function_4()
        elif agent_coordinates[1] > key_coordinates[1]:
            function_3()
        agent_coordinates = belief_set['agent']['coordinates']
        counter += 1
    if agent_coordinates == key_coordinates:
        function_5()
    else:
        return (
            'Error: The agent could not reach the key within the maximum number of moves.'
            )

def function_12():
    global belief_set
    agent_coords = belief_set['agent']['coordinates']
    delivery_cells = [c['cell_coordinates'] for c in belief_set['map'][
        'grid'] if 'delivery' in c['cell_type']]
    nearest_delivery_cell = min(delivery_cells, key=lambda c: abs(c[0] -
        agent_coords[0]) + abs(c[1] - agent_coords[1]))
    while agent_coords != nearest_delivery_cell:
        if agent_coords[0] < nearest_delivery_cell[0]:
            function_2()
        elif agent_coords[0] > nearest_delivery_cell[0]:
            function_1()
        if agent_coords[1] < nearest_delivery_cell[1]:
            function_4()
        elif agent_coords[1] > nearest_delivery_cell[1]:
            function_3()
        agent_coords = belief_set['agent']['coordinates']
    function_6()

