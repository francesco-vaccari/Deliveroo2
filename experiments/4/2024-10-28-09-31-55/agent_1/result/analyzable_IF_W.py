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
    agent = belief_set['agent']
    parcel = next(iter(belief_set['parcels'].values()))
    if agent['coordinates'][0] < parcel['coordinates'][0]:
        function_2()
    elif agent['coordinates'][0] > parcel['coordinates'][0]:
        function_1()
    elif agent['coordinates'][1] < parcel['coordinates'][1]:
        function_4()
    elif agent['coordinates'][1] > parcel['coordinates'][1]:
        function_3()

def function_10():
    global belief_set
    if belief_set['agent']['coordinates'] == belief_set['parcels'][1][
        'coordinates']:
        function_5()
    else:
        function_8()

def function_20():
    global belief_set
    if belief_set['agent']['coordinates'] == belief_set['parcels'][1][
        'coordinates']:
        function_5()
    else:
        function_8()

