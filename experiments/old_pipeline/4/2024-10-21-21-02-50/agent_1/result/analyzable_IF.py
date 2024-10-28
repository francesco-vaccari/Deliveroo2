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
    agent = belief_set['agents'][1]
    key = belief_set['keys'][1]
    if agent['coordinates'] == key['coordinates']:
        function_5()
    elif agent['coordinates'][0] > key['coordinates'][0]:
        function_1()
    elif agent['coordinates'][0] < key['coordinates'][0]:
        function_2()
    elif agent['coordinates'][1] > key['coordinates'][1]:
        function_3()
    elif agent['coordinates'][1] < key['coordinates'][1]:
        function_4()
    else:
        pass

def function_8():
    global belief_set
    agent_location = belief_set['agents'][1]['coordinates']
    key_location = belief_set['keys'][1]['coordinates']
    while agent_location != key_location:
        if agent_location[0] < key_location[0]:
            function_2()
        elif agent_location[0] > key_location[0]:
            function_1()
        elif agent_location[1] < key_location[1]:
            function_4()
        elif agent_location[1] > key_location[1]:
            function_3()
        agent_location = belief_set['agents'][1]['coordinates']
    function_5()

def function_9():
    global belief_set
    while belief_set['agents'][1]['coordinates'] != belief_set['parcels'][1][
        'coordinates']:
        if belief_set['agents'][1]['coordinates'][0] < belief_set['parcels'][1
            ]['coordinates'][0]:
            function_2()
        elif belief_set['agents'][1]['coordinates'][0] > belief_set['parcels'][
            1]['coordinates'][0]:
            function_1()
        if belief_set['agents'][1]['coordinates'][1] < belief_set['parcels'][1
            ]['coordinates'][1]:
            function_4()
        elif belief_set['agents'][1]['coordinates'][1] > belief_set['parcels'][
            1]['coordinates'][1]:
            function_3()
    function_5()

def function_10():
    global belief_set
    agent = belief_set['agents'][1]
    delivery_cells = [cell for cell in belief_set['map']['grid'] if 
        'delivery' in cell['cell_type']]
    closest_delivery_cell = min(delivery_cells, key=lambda cell: abs(cell[
        'cell_coordinates'][0] - agent['coordinates'][0]) + abs(cell[
        'cell_coordinates'][1] - agent['coordinates'][1]))
    while agent['coordinates'] != closest_delivery_cell['cell_coordinates']:
        if agent['coordinates'][0] < closest_delivery_cell['cell_coordinates'][
            0]:
            function_2()
        elif agent['coordinates'][0] > closest_delivery_cell['cell_coordinates'
            ][0]:
            function_1()
        if agent['coordinates'][1] < closest_delivery_cell['cell_coordinates'][
            1]:
            function_4()
        elif agent['coordinates'][1] > closest_delivery_cell['cell_coordinates'
            ][1]:
            function_3()
    function_6()

def function_11():
    global belief_set
    agent = belief_set['agents'][1]
    delivery_cells = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] in ['delivery_cell', 'double_delivery_cell']]
    for cell in delivery_cells:
        if agent['coordinates'][0] < cell['cell_coordinates'][0]:
            function_2()
        elif agent['coordinates'][0] > cell['cell_coordinates'][0]:
            function_1()
        elif agent['coordinates'][1] < cell['cell_coordinates'][1]:
            function_4()
        elif agent['coordinates'][1] > cell['cell_coordinates'][1]:
            function_3()
    function_6()

