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
    parcel_carrying = False
    while not parcel_carrying:
        if belief_set['agent'][1]['coordinates'] == belief_set['map']['grid'][0
            ]['cell_coordinates']:
            function_5()
            parcel_carrying = True
        elif belief_set['agent'][1]['coordinates'][0] > belief_set['map'][
            'grid'][0]['cell_coordinates'][0]:
            function_1()
        elif belief_set['agent'][1]['coordinates'][0] < belief_set['map'][
            'grid'][0]['cell_coordinates'][0]:
            function_2()
        elif belief_set['agent'][1]['coordinates'][1] > belief_set['map'][
            'grid'][0]['cell_coordinates'][1]:
            function_3()
        else:
            function_4()
    while belief_set['agent'][1]['coordinates'] != belief_set['map']['grid'][7
        ]['cell_coordinates']:
        if belief_set['agent'][1]['coordinates'][0] > belief_set['map']['grid'
            ][7]['cell_coordinates'][0]:
            function_1()
        elif belief_set['agent'][1]['coordinates'][0] < belief_set['map'][
            'grid'][7]['cell_coordinates'][0]:
            function_2()
        elif belief_set['agent'][1]['coordinates'][1] > belief_set['map'][
            'grid'][7]['cell_coordinates'][1]:
            function_3()
        else:
            function_4()
    function_6()
    return

def function_9():
    global belief_set
    parcel_coordinates = [parcel['coordinates'] for parcel in belief_set[
        'parcels'].values() if parcel['carried_by_id'] is None]
    delivery_coordinates = [cell['cell_coordinates'] for cell in belief_set
        ['map']['grid'] if cell['cell_type'] == 'delivery_cell'][0]
    agent_coordinates = belief_set['agent'][1]['coordinates']
    while agent_coordinates != parcel_coordinates[0]:
        if agent_coordinates[0] < parcel_coordinates[0][0]:
            function_2()
        elif agent_coordinates[0] > parcel_coordinates[0][0]:
            function_1()
        if agent_coordinates[1] < parcel_coordinates[0][1]:
            function_4()
        elif agent_coordinates[1] > parcel_coordinates[0][1]:
            function_3()
        agent_coordinates = belief_set['agent'][1]['coordinates']
    function_5()
    while agent_coordinates != delivery_coordinates:
        if agent_coordinates[0] < delivery_coordinates[0]:
            function_2()
        elif agent_coordinates[0] > delivery_coordinates[0]:
            function_1()
        if agent_coordinates[1] < delivery_coordinates[1]:
            function_4()
        elif agent_coordinates[1] > delivery_coordinates[1]:
            function_3()
        agent_coordinates = belief_set['agent'][1]['coordinates']
    function_6()

def function_14():
    global belief_set
    max_iterations = 100
    iteration_count = 0
    while iteration_count < max_iterations and belief_set['agent'][1][
        'coordinates'] != belief_set['parcels'][12]['coordinates']:
        if belief_set['agent'][1]['coordinates'][0] < belief_set['parcels'][12
            ]['coordinates'][0]:
            function_2()
        elif belief_set['agent'][1]['coordinates'][0] > belief_set['parcels'][
            12]['coordinates'][0]:
            function_1()
        elif belief_set['agent'][1]['coordinates'][1] < belief_set['parcels'][
            12]['coordinates'][1]:
            function_4()
        else:
            function_3()
        iteration_count += 1
    function_5()
    while iteration_count < max_iterations and belief_set['agent'][1][
        'coordinates'] != [1, 3]:
        if belief_set['agent'][1]['coordinates'][0] < 1:
            function_2()
        elif belief_set['agent'][1]['coordinates'][0] > 1:
            function_1()
        elif belief_set['agent'][1]['coordinates'][1] < 3:
            function_4()
        else:
            function_3()
        iteration_count += 1
    function_6()

