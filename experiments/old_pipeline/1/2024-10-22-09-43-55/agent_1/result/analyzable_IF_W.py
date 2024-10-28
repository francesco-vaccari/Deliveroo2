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
    spawn_point = [cell['cell_coordinates'] for cell in belief_set['map'][
        'grid'] if cell['cell_type'] == 'parcels_spawn'][0]
    agent_position = belief_set['agent']['coordinates']
    while agent_position != spawn_point:
        if agent_position[0] > spawn_point[0]:
            function_1()
        elif agent_position[0] < spawn_point[0]:
            function_2()
        elif agent_position[1] > spawn_point[1]:
            function_3()
        else:
            function_4()
        agent_position = belief_set['agent']['coordinates']
    function_5()

def function_11():
    global belief_set
    while belief_set['agent']['coordinates'] != [1, 3]:
        if belief_set['agent']['coordinates'][1] < 3:
            function_4()
        elif belief_set['agent']['coordinates'][0] > 1:
            function_1()
    function_6()

