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


def function_17():
    global belief_set
    agent_x, agent_y = belief_set['agent']['coordinates']
    delivery_cell = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'delivery_cell'][0]['cell_coordinates']
    delivery_x, delivery_y = delivery_cell
    max_steps = belief_set['map']['width'] * belief_set['map']['height']
    steps = 0
    while (agent_x, agent_y) != (delivery_x, delivery_y) and steps < max_steps:
        if agent_x > delivery_x:
            function_1()
            agent_x -= 1
        elif agent_x < delivery_x:
            function_2()
            agent_x += 1
        if agent_y > delivery_y:
            function_3()
            agent_y -= 1
        elif agent_y < delivery_y:
            function_4()
            agent_y += 1
        steps += 1
    function_6()

