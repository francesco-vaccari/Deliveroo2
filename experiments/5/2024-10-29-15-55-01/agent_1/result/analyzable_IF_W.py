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
    spawn_coordinates = [cell['cell_coordinates'] for cell in belief_set[
        'map']['grid'] if cell['cell_type'] == 'parcels_spawn'][0]
    delivery_coordinates = [cell['cell_coordinates'] for cell in belief_set
        ['map']['grid'] if cell['cell_type'] == 'delivery_cell'][0]
    agent_coordinates = belief_set['agent'][1]['coordinates']
    while agent_coordinates != spawn_coordinates:
        if agent_coordinates[0] > spawn_coordinates[0]:
            function_1()
        elif agent_coordinates[0] < spawn_coordinates[0]:
            function_2()
        if agent_coordinates[1] > spawn_coordinates[1]:
            function_3()
        elif agent_coordinates[1] < spawn_coordinates[1]:
            function_4()
        agent_coordinates = belief_set['agent'][1]['coordinates']
    function_5()
    while agent_coordinates != delivery_coordinates:
        if agent_coordinates[0] > delivery_coordinates[0]:
            function_1()
        elif agent_coordinates[0] < delivery_coordinates[0]:
            function_2()
        if agent_coordinates[1] > delivery_coordinates[1]:
            function_3()
        elif agent_coordinates[1] < delivery_coordinates[1]:
            function_4()
        agent_coordinates = belief_set['agent'][1]['coordinates']
    function_6()

def function_12():
    global belief_set
    agent = belief_set['agent'][1]
    map_grid = belief_set['map']['grid']
    agent_x, agent_y = agent['coordinates']
    walkable_cells = [cell for cell in map_grid if cell['cell_type'] ==
        'walkable']
    nearest_walkable_cell = min(walkable_cells, key=lambda cell: abs(cell[
        'cell_coordinates'][0] - agent_x) + abs(cell['cell_coordinates'][1] -
        agent_y))
    if nearest_walkable_cell['cell_coordinates'][0] < agent_x:
        function_1()
    elif nearest_walkable_cell['cell_coordinates'][0] > agent_x:
        function_2()
    elif nearest_walkable_cell['cell_coordinates'][1] < agent_y:
        function_3()
    elif nearest_walkable_cell['cell_coordinates'][1] > agent_y:
        function_4()

