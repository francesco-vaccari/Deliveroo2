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
    parcel_coordinates = belief_set['parcels'][1]['coordinates']
    agent_coordinates = belief_set['agent']['coordinates']
    while agent_coordinates != parcel_coordinates:
        if parcel_coordinates[0] < agent_coordinates[0]:
            function_1()
        elif parcel_coordinates[0] > agent_coordinates[0]:
            function_2()
        elif parcel_coordinates[1] < agent_coordinates[1]:
            function_3()
        elif parcel_coordinates[1] > agent_coordinates[1]:
            function_4()
        agent_coordinates = belief_set['agent']['coordinates']
    function_5()

def function_10():
    global belief_set
    agent_coords = belief_set['agent']['coordinates']
    parcel_coords = belief_set['parcels'][1]['coordinates']
    if agent_coords[0] < parcel_coords[0]:
        function_2()
    elif agent_coords[0] > parcel_coords[0]:
        function_1()
    elif agent_coords[1] < parcel_coords[1]:
        function_4()
    elif agent_coords[1] > parcel_coords[1]:
        function_3()
    if agent_coords == parcel_coords:
        function_5()

def function_14():
    global belief_set
    agent_coordinates = belief_set['agent']['coordinates']
    parcel_coordinates = belief_set['parcels'][1]['coordinates']
    while agent_coordinates != parcel_coordinates:
        if agent_coordinates[0] < parcel_coordinates[0]:
            function_2()
            agent_coordinates[0] += 1
        elif agent_coordinates[0] > parcel_coordinates[0]:
            function_1()
            agent_coordinates[0] -= 1
        elif agent_coordinates[1] < parcel_coordinates[1]:
            function_4()
            agent_coordinates[1] += 1
        elif agent_coordinates[1] > parcel_coordinates[1]:
            function_3()
            agent_coordinates[1] -= 1
    function_5()

def function_23():
    global belief_set
    if not belief_set['agent']['parcels_carried_ids']:
        parcel_coord = belief_set['parcels'][1]['coordinates']
        agent_coord = belief_set['agent']['coordinates']
        while agent_coord != parcel_coord:
            if parcel_coord[0] < agent_coord[0]:
                if agent_coord[0] > 0:
                    function_1()
            elif parcel_coord[0] > agent_coord[0]:
                if agent_coord[0] < belief_set['map']['height'] - 1:
                    function_2()
            if parcel_coord[1] < agent_coord[1]:
                if agent_coord[1] > 0:
                    function_3()
            elif parcel_coord[1] > agent_coord[1]:
                if agent_coord[1] < belief_set['map']['width'] - 1:
                    function_4()
            agent_coord = belief_set['agent']['coordinates']
        function_5()
    return

