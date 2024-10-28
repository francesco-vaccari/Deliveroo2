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


def function_9():
    global belief_set
    parcel_location = belief_set['parcel'][1]['coordinates']
    agent_location = belief_set['agent'][1]['coordinates']
    while agent_location != parcel_location:
        if agent_location[0] < parcel_location[0]:
            function_2()
        elif agent_location[0] > parcel_location[0]:
            function_1()
        elif agent_location[1] < parcel_location[1]:
            function_4()
        elif agent_location[1] > parcel_location[1]:
            function_3()
        agent_location = belief_set['agent'][1]['coordinates']
    function_5()

def function_13():
    global belief_set
    key_coordinates = belief_set['key'][1]['coordinates']
    agent_coordinates = belief_set['agent'][1]['coordinates']
    while agent_coordinates[0] != key_coordinates[0]:
        if agent_coordinates[0] > key_coordinates[0]:
            function_1()
        else:
            function_2()
        agent_coordinates = belief_set['agent'][1]['coordinates']
    while agent_coordinates[1] != key_coordinates[1]:
        if agent_coordinates[1] > key_coordinates[1]:
            function_3()
        else:
            function_4()
        agent_coordinates = belief_set['agent'][1]['coordinates']
    function_5()

def function_14():
    global belief_set
    delivery_coordinates = [cell['cell_coordinates'] for cell in belief_set
        ['map']['grid'] if cell['cell_type'] == 'delivery_cell'][0]
    agent_coordinates = belief_set['agent'][1]['coordinates']
    while agent_coordinates != delivery_coordinates:
        if agent_coordinates[0] > delivery_coordinates[0]:
            function_1()
        elif agent_coordinates[0] < delivery_coordinates[0]:
            function_2()
        if agent_coordinates[1] > delivery_coordinates[1]:
            function_3()
        elif agent_coordinates[1] < delivery_coordinates[1]:
            function_4()
        agent_coordinates = belief_set['agent'][1]['coordinates']
    function_6()

