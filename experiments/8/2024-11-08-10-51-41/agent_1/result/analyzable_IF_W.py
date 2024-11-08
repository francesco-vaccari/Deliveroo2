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
    agent = belief_set['agent'][1]
    delivery_cell = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'delivery_cell'][0]
    if agent['coordinates'][0] > delivery_cell['cell_coordinates'][0]:
        function_1()
    elif agent['coordinates'][0] < delivery_cell['cell_coordinates'][0]:
        function_2()
    elif agent['coordinates'][1] > delivery_cell['cell_coordinates'][1]:
        function_3()
    elif agent['coordinates'][1] < delivery_cell['cell_coordinates'][1]:
        function_4()
    else:
        function_6()

def function_13():
    global belief_set
    delivery_cells = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'delivery_cell']
    delivery_cells.sort(key=lambda x: abs(x['cell_coordinates'][0] -
        belief_set['agent'][1]['coordinates'][0]) + abs(x[
        'cell_coordinates'][1] - belief_set['agent'][1]['coordinates'][1]))
    for cell in delivery_cells:
        dx = cell['cell_coordinates'][0] - belief_set['agent'][1]['coordinates'
            ][0]
        dy = cell['cell_coordinates'][1] - belief_set['agent'][1]['coordinates'
            ][1]
        if dx < 0 and belief_set['agent'][1]['energy'] >= 5:
            function_1()
            break
        elif dx > 0 and belief_set['agent'][1]['energy'] >= 5:
            function_2()
            break
        elif dy < 0 and belief_set['agent'][1]['energy'] >= 5:
            function_3()
            break
        elif dy > 0 and belief_set['agent'][1]['energy'] >= 5:
            function_4()
            break

def function_14():
    global belief_set
    delivery_cells = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'delivery_cell']
    agent = belief_set['agent'][1]
    if agent['coordinates'] in [cell['cell_coordinates'] for cell in
        delivery_cells]:
        function_6()
    else:
        function_13()

def function_33():
    global belief_set
    if belief_set['agent'][1]['coordinates'] == [0, 0]:
        function_6()
    elif belief_set['agent'][1]['energy'] < 20:
        function_14()
    else:
        function_13()

