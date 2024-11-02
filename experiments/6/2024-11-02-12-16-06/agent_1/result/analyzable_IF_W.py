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
    delivery_cell = [item['cell_coordinates'] for item in belief_set['map']
        ['grid'] if item['cell_type'] == 'delivery_cell'][0]
    agent = belief_set['agent'][1]
    while agent['coordinates'] != delivery_cell:
        if agent['coordinates'][0] > delivery_cell[0]:
            function_1()
        elif agent['coordinates'][0] < delivery_cell[0]:
            function_2()
        elif agent['coordinates'][1] > delivery_cell[1]:
            function_3()
        elif agent['coordinates'][1] < delivery_cell[1]:
            function_4()
        agent = belief_set['agent'][1]
        if agent['coordinates'] == [item['cell_coordinates'] for item in
            belief_set['map']['grid'] if item['cell_type'] == 'batteries_spawn'
            ][0] and agent['energy'] < 50:
            function_5()
    function_6()

def function_20():
    global belief_set
    agent = belief_set['agent'][1]
    parcels_spawn = next(cell['cell_coordinates'] for cell in belief_set[
        'map']['grid'] if cell['cell_type'] == 'parcels_spawn')
    batteries_spawn = next(cell['cell_coordinates'] for cell in belief_set[
        'map']['grid'] if cell['cell_type'] == 'batteries_spawn')
    delivery_cell = next(cell['cell_coordinates'] for cell in belief_set[
        'map']['grid'] if cell['cell_type'] == 'delivery_cell')
    while agent['coordinates'] != parcels_spawn:
        if agent['coordinates'][0] < parcels_spawn[0]:
            function_2()
        elif agent['coordinates'][0] > parcels_spawn[0]:
            function_1()
        elif agent['coordinates'][1] < parcels_spawn[1]:
            function_4()
        elif agent['coordinates'][1] > parcels_spawn[1]:
            function_3()
        agent = belief_set['agent'][1]
    function_5()
    while agent['coordinates'] != batteries_spawn:
        if agent['coordinates'][0] < batteries_spawn[0]:
            function_2()
        elif agent['coordinates'][0] > batteries_spawn[0]:
            function_1()
        elif agent['coordinates'][1] < batteries_spawn[1]:
            function_4()
        elif agent['coordinates'][1] > batteries_spawn[1]:
            function_3()
        agent = belief_set['agent'][1]
    if agent['energy'] < 50:
        function_5()
    while agent['coordinates'] != delivery_cell:
        if agent['coordinates'][0] < delivery_cell[0]:
            function_2()
        elif agent['coordinates'][0] > delivery_cell[0]:
            function_1()
        elif agent['coordinates'][1] < delivery_cell[1]:
            function_4()
        elif agent['coordinates'][1] > delivery_cell[1]:
            function_3()
        agent = belief_set['agent'][1]
    function_6()

def function_21():
    global belief_set
    function_20()
    agent = belief_set['agent'][1]
    if agent['energy'] < 50:
        for cell in belief_set['map']['grid']:
            if cell['cell_type'] == 'batteries_spawn' and cell[
                'cell_coordinates'] == agent['coordinates']:
                function_5()
    function_11()

def function_23():
    global belief_set
    function_20()
    if belief_set['agent'][1]['energy'] < 50:
        function_5()
    function_11()

