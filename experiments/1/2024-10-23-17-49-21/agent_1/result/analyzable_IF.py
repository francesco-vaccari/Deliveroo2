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
    agent_coords = belief_set['agent']['coordinates']
    parcel_coords = belief_set['parcel'][1]['coordinates']
    if agent_coords[0] > parcel_coords[0]:
        function_1()
    elif agent_coords[0] < parcel_coords[0]:
        function_2()
    if agent_coords[1] > parcel_coords[1]:
        function_3()
    elif agent_coords[1] < parcel_coords[1]:
        function_4()
    else:
        function_5()

def function_8():
    global belief_set
    spawn = [cell['cell_coordinates'] for cell in belief_set['map']['grid'] if
        cell['cell_type'] == 'parcels_spawn'][0]
    delivery = [cell['cell_coordinates'] for cell in belief_set['map'][
        'grid'] if cell['cell_type'] == 'delivery_cell'][0]
    agent = belief_set['agent']['coordinates']
    while agent != spawn:
        if agent[0] < spawn[0]:
            function_2()
        elif agent[0] > spawn[0]:
            function_1()
        elif agent[1] < spawn[1]:
            function_4()
        elif agent[1] > spawn[1]:
            function_3()
    function_5()
    while agent != delivery:
        if agent[0] < delivery[0]:
            function_2()
        elif agent[0] > delivery[0]:
            function_1()
        elif agent[1] < delivery[1]:
            function_4()
        elif agent[1] > delivery[1]:
            function_3()
    function_6()

def function_9():
    global belief_set
    agent = belief_set['agent']
    delivery_cell = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'delivery_cell'][0]['cell_coordinates']
    while agent['coordinates'] != delivery_cell:
        if agent['coordinates'][0] < delivery_cell[0]:
            function_2()
            agent['coordinates'][0] += 1
        elif agent['coordinates'][0] > delivery_cell[0]:
            function_1()
            agent['coordinates'][0] -= 1
        elif agent['coordinates'][1] < delivery_cell[1]:
            function_4()
            agent['coordinates'][1] += 1
        elif agent['coordinates'][1] > delivery_cell[1]:
            function_3()
            agent['coordinates'][1] -= 1
    function_6()

