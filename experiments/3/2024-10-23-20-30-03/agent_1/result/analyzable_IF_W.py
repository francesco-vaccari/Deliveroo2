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
    parcel = list(belief_set['parcels'].values())[0]
    agent = belief_set['agents'][1]
    while parcel['coordinates'] != agent['coordinates']:
        if parcel['coordinates'][0] < agent['coordinates'][0]:
            function_1()
            agent['coordinates'][0] -= 1
        elif parcel['coordinates'][0] > agent['coordinates'][0]:
            function_2()
            agent['coordinates'][0] += 1
        elif parcel['coordinates'][1] < agent['coordinates'][1]:
            function_3()
            agent['coordinates'][1] -= 1
        elif parcel['coordinates'][1] > agent['coordinates'][1]:
            function_4()
            agent['coordinates'][1] += 1
    function_5()
    parcel['carried_by_id'] = 1
    agent['parcels_carried_ids'].append(parcel['id'])

def function_9():
    global belief_set
    max_iterations = 100
    i = 0
    agent = belief_set['agents'][1]
    delivery_cell = [3, 0]
    while i < max_iterations and agent['coordinates'] != delivery_cell:
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
        i += 1
    if agent['coordinates'] == delivery_cell:
        function_6()
    return

