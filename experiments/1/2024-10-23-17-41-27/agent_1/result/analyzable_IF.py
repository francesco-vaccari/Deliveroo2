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
    spawn_location = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'parcels_spawn'][0]['cell_coordinates']
    delivery_location = [cell for cell in belief_set['map']['grid'] if cell
        ['cell_type'] == 'delivery_cell'][0]['cell_coordinates']
    while belief_set['agent']['coordinates'] != spawn_location:
        if belief_set['agent']['coordinates'][0] < spawn_location[0]:
            function_2()
        elif belief_set['agent']['coordinates'][0] > spawn_location[0]:
            function_1()
        elif belief_set['agent']['coordinates'][1] < spawn_location[1]:
            function_4()
        elif belief_set['agent']['coordinates'][1] > spawn_location[1]:
            function_3()
    function_5()
    while belief_set['agent']['coordinates'] != delivery_location:
        if belief_set['agent']['coordinates'][0] < delivery_location[0]:
            function_2()
        elif belief_set['agent']['coordinates'][0] > delivery_location[0]:
            function_1()
        elif belief_set['agent']['coordinates'][1] < delivery_location[1]:
            function_4()
        elif belief_set['agent']['coordinates'][1] > delivery_location[1]:
            function_3()
    function_6()

