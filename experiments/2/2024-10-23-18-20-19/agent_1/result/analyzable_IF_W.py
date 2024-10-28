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
    parcel_coordinates = belief_set['parcel'][1]['coordinates']
    agent_coordinates = belief_set['agent']['coordinates']
    while agent_coordinates != parcel_coordinates:
        if agent_coordinates[0] < parcel_coordinates[0]:
            function_2()
            agent_coordinates[0] += 1
        elif agent_coordinates[0] > parcel_coordinates[0]:
            function_1()
            agent_coordinates[0] -= 1
        if agent_coordinates[1] < parcel_coordinates[1]:
            function_4()
            agent_coordinates[1] += 1
        elif agent_coordinates[1] > parcel_coordinates[1]:
            function_3()
            agent_coordinates[1] -= 1
    function_5()

def function_11():
    global belief_set
    parcel_coord = belief_set['parcel'][1]['coordinates']
    agent_coord = belief_set['agent']['coordinates']
    while agent_coord != parcel_coord:
        if agent_coord[0] < parcel_coord[0]:
            function_2()
        elif agent_coord[0] > parcel_coord[0]:
            function_1()
        if agent_coord[1] < parcel_coord[1]:
            function_4()
        elif agent_coord[1] > parcel_coord[1]:
            function_3()
        agent_coord = belief_set['agent']['coordinates']
    function_5()

def function_12():
    global belief_set
    delivery_cell_coordinates = [cell['cell_coordinates'] for cell in
        belief_set['map']['grid'] if cell['cell_type'] == 'delivery_cell'][0]
    agent_coordinates = belief_set['agent']['coordinates']
    while agent_coordinates != delivery_cell_coordinates:
        if agent_coordinates[0] < delivery_cell_coordinates[0]:
            function_2()
        elif agent_coordinates[0] > delivery_cell_coordinates[0]:
            function_1()
        elif agent_coordinates[1] < delivery_cell_coordinates[1]:
            function_4()
        else:
            function_3()
    function_6()

