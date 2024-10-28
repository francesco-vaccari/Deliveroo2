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


def function_16():
    global belief_set
    current_position = belief_set['agent']['coordinates']
    map_grid = belief_set['map']['grid']
    walkable_cells = [cell['cell_coordinates'] for cell in map_grid if cell
        ['cell_type'] == 'walkable']
    nearest_walkable_cell = min(walkable_cells, key=lambda cell: abs(cell[0
        ] - current_position[0]) + abs(cell[1] - current_position[1]))
    if nearest_walkable_cell[0] < current_position[0]:
        function_1()
    elif nearest_walkable_cell[0] > current_position[0]:
        function_2()
    elif nearest_walkable_cell[1] < current_position[1]:
        function_3()
    elif nearest_walkable_cell[1] > current_position[1]:
        function_4()

def function_17():
    global belief_set
    delivery_cells = [cell['cell_coordinates'] for cell in belief_set['map'
        ]['grid'] if 'delivery' in cell['cell_type']]
    agent_position = belief_set['agent']['coordinates']
    delivery_cells.sort(key=lambda x: abs(x[0] - agent_position[0]) + abs(x
        [1] - agent_position[1]))
    nearest_delivery_cell = delivery_cells[0]
    while belief_set['agent']['coordinates'] != nearest_delivery_cell:
        if belief_set['agent']['coordinates'][0] < nearest_delivery_cell[0]:
            function_2()
        elif belief_set['agent']['coordinates'][0] > nearest_delivery_cell[0]:
            function_1()
        elif belief_set['agent']['coordinates'][1] < nearest_delivery_cell[1]:
            function_4()
        elif belief_set['agent']['coordinates'][1] > nearest_delivery_cell[1]:
            function_3()
    function_6()

