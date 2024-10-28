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
    parcel_spawn = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'parcels_spawn'][0]['cell_coordinates']
    agent_pos = belief_set['agent']['coordinates']
    while agent_pos[0] > parcel_spawn[0]:
        function_1()
        agent_pos[0] -= 1
    while agent_pos[0] < parcel_spawn[0]:
        function_2()
        agent_pos[0] += 1
    while agent_pos[1] > parcel_spawn[1]:
        function_3()
        agent_pos[1] -= 1
    while agent_pos[1] < parcel_spawn[1]:
        function_4()
        agent_pos[1] += 1
    function_5()

def function_8():
    global belief_set
    delivery_cell_coordinates = [cell['cell_coordinates'] for cell in
        belief_set['map']['grid'] if cell['cell_type'] == 'delivery_cell'][0]
    while belief_set['agent']['coordinates'] != delivery_cell_coordinates:
        if belief_set['agent']['coordinates'][0] < delivery_cell_coordinates[0
            ]:
            function_2()
        elif belief_set['agent']['coordinates'][0] > delivery_cell_coordinates[
            0]:
            function_1()
        elif belief_set['agent']['coordinates'][1] < delivery_cell_coordinates[
            1]:
            function_4()
        elif belief_set['agent']['coordinates'][1] > delivery_cell_coordinates[
            1]:
            function_3()
    function_6()

