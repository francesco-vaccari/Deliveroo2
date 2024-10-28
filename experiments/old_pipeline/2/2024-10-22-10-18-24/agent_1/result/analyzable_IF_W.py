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


def function_10():
    global belief_set
    parcel_coordinates = belief_set['parcel'][1]['coordinates']
    agent_coordinates = belief_set['agent']['coordinates']
    while agent_coordinates != parcel_coordinates:
        if agent_coordinates[0] < parcel_coordinates[0]:
            function_2()
        elif agent_coordinates[0] > parcel_coordinates[0]:
            function_1()
        elif agent_coordinates[1] < parcel_coordinates[1]:
            function_4()
        elif agent_coordinates[1] > parcel_coordinates[1]:
            function_3()
        agent_coordinates = belief_set['agent']['coordinates']
    function_5()

