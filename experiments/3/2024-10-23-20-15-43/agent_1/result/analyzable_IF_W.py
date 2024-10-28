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
    agent_coordinates = belief_set['agent']['coordinates']
    nearest_parcel_coordinates = belief_set['parcels'][1]['coordinates']
    while agent_coordinates != nearest_parcel_coordinates:
        if agent_coordinates[0] < nearest_parcel_coordinates[0]:
            function_2()
            if belief_set['agent']['coordinates'] == agent_coordinates:
                break
        elif agent_coordinates[0] > nearest_parcel_coordinates[0]:
            function_1()
            if belief_set['agent']['coordinates'] == agent_coordinates:
                break
        elif agent_coordinates[1] < nearest_parcel_coordinates[1]:
            function_4()
            if belief_set['agent']['coordinates'] == agent_coordinates:
                break
        elif agent_coordinates[1] > nearest_parcel_coordinates[1]:
            function_3()
            if belief_set['agent']['coordinates'] == agent_coordinates:
                break
        agent_coordinates = belief_set['agent']['coordinates']
    function_5()

def function_10():
    global belief_set
    key_positions = [key['coordinates'] for key in belief_set['keys'].
        values() if key['carried_by_id'] is None]
    agent_position = belief_set['agent']['coordinates']
    nearest_key_position = min(key_positions, key=lambda pos: abs(pos[0] -
        agent_position[0]) + abs(pos[1] - agent_position[1]))
    while agent_position != nearest_key_position:
        if agent_position[0] < nearest_key_position[0]:
            function_2()
        elif agent_position[0] > nearest_key_position[0]:
            function_1()
        elif agent_position[1] < nearest_key_position[1]:
            function_4()
        elif agent_position[1] > nearest_key_position[1]:
            function_3()
        agent_position = belief_set['agent']['coordinates']
    function_5()

def function_12():
    global belief_set
    if 'keys' in belief_set and belief_set['keys']:
        function_10()
    else:
        function_9()

