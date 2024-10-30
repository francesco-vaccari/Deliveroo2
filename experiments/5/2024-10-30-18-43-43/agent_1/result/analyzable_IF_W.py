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


def function_12():
    global belief_set
    agent = belief_set['agent'][1]
    spawn_point = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'parcels_spawn'][0]['cell_coordinates']
    if agent['coordinates'] != spawn_point:
        if agent['coordinates'][0] > spawn_point[0]:
            function_1()
        elif agent['coordinates'][0] < spawn_point[0]:
            function_2()
        elif agent['coordinates'][1] > spawn_point[1]:
            function_3()
        else:
            function_4()
    function_5()

def function_14():
    global belief_set
    spawn_point = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'parcels_spawn'][0]['cell_coordinates']
    delivery_point = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'delivery_cell'][0]['cell_coordinates']
    agent_location = belief_set['agent'][1]['coordinates']
    while agent_location != spawn_point:
        if agent_location[0] < spawn_point[0]:
            function_2()
        elif agent_location[0] > spawn_point[0]:
            function_1()
        elif agent_location[1] < spawn_point[1]:
            function_4()
        else:
            function_3()
        agent_location = belief_set['agent'][1]['coordinates']
    function_5()
    while agent_location != delivery_point:
        if agent_location[0] < delivery_point[0]:
            function_2()
        elif agent_location[0] > delivery_point[0]:
            function_1()
        elif agent_location[1] < delivery_point[1]:
            function_4()
        else:
            function_3()
        agent_location = belief_set['agent'][1]['coordinates']
    function_6()


