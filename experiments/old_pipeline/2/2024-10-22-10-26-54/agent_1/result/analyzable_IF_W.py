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


def function_8():
    global belief_set
    agent_position = belief_set['agent']['coordinates']
    parcel_position = belief_set['parcels'][1]['coordinates']
    while agent_position != parcel_position:
        if agent_position[0] < parcel_position[0]:
            function_2()
            agent_position[0] += 1
        elif agent_position[0] > parcel_position[0]:
            function_1()
            agent_position[0] -= 1
        if agent_position[1] < parcel_position[1]:
            function_4()
            agent_position[1] += 1
        elif agent_position[1] > parcel_position[1]:
            function_3()
            agent_position[1] -= 1
    function_5()

def function_11():
    global belief_set
    agent_coordinates = belief_set['agent']['coordinates']
    delivery_cell_coordinates = [cell['cell_coordinates'] for cell in
        belief_set['map']['grid'] if cell['cell_type'] == 'delivery_cell'][0]
    while agent_coordinates != delivery_cell_coordinates:
        if agent_coordinates[0] < delivery_cell_coordinates[0]:
            function_2()
        elif agent_coordinates[0] > delivery_cell_coordinates[0]:
            function_1()
        elif agent_coordinates[1] < delivery_cell_coordinates[1]:
            function_4()
        elif agent_coordinates[1] > delivery_cell_coordinates[1]:
            function_3()
        agent_coordinates = belief_set['agent']['coordinates']
    function_6()

