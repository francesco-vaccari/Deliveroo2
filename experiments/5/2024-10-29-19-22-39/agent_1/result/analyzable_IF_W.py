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
    spawn_location = [cell['cell_coordinates'] for cell in belief_set['map'
        ]['grid'] if cell['cell_type'] == 'parcels_spawn'][0]
    while belief_set['agent'][1]['coordinates'] != spawn_location:
        if belief_set['agent'][1]['coordinates'][0] > spawn_location[0]:
            function_1()
        elif belief_set['agent'][1]['coordinates'][0] < spawn_location[0]:
            function_2()
        if belief_set['agent'][1]['coordinates'][1] > spawn_location[1]:
            function_3()
        elif belief_set['agent'][1]['coordinates'][1] < spawn_location[1]:
            function_4()
    function_5()

def function_12():
    global belief_set
    spawn_location = [cell['cell_coordinates'] for cell in belief_set['map'
        ]['grid'] if cell['cell_type'] == 'parcels_spawn'][0]
    delivery_location = [cell['cell_coordinates'] for cell in belief_set[
        'map']['grid'] if cell['cell_type'] == 'delivery_cell'][0]
    agent_location = belief_set['agent'][1]['coordinates']
    while agent_location != spawn_location:
        if agent_location[0] > spawn_location[0]:
            function_1()
        elif agent_location[0] < spawn_location[0]:
            function_2()
        if agent_location[1] > spawn_location[1]:
            function_3()
        elif agent_location[1] < spawn_location[1]:
            function_4()
        agent_location = belief_set['agent'][1]['coordinates']
    function_5()
    while agent_location != delivery_location:
        if agent_location[0] > delivery_location[0]:
            function_1()
        elif agent_location[0] < delivery_location[0]:
            function_2()
        if agent_location[1] > delivery_location[1]:
            function_3()
        elif agent_location[1] < delivery_location[1]:
            function_4()
        agent_location = belief_set['agent'][1]['coordinates']
    function_6()

def function_13():
    global belief_set
    function_7()
    function_5()
    function_12()

def function_15():
    global belief_set
    parcel_spawn = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'parcels_spawn'][0]['cell_coordinates']
    delivery_cell = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'delivery_cell'][0]['cell_coordinates']
    agent_coordinates = belief_set['agent'][1]['coordinates']
    while agent_coordinates != parcel_spawn:
        if agent_coordinates[0] < parcel_spawn[0]:
            function_2()
            agent_coordinates[0] += 1
        elif agent_coordinates[0] > parcel_spawn[0]:
            function_1()
            agent_coordinates[0] -= 1
        elif agent_coordinates[1] < parcel_spawn[1]:
            function_4()
            agent_coordinates[1] += 1
        elif agent_coordinates[1] > parcel_spawn[1]:
            function_3()
            agent_coordinates[1] -= 1
    function_5()
    while agent_coordinates != delivery_cell:
        if agent_coordinates[0] < delivery_cell[0]:
            function_2()
            agent_coordinates[0] += 1
        elif agent_coordinates[0] > delivery_cell[0]:
            function_1()
            agent_coordinates[0] -= 1
        elif agent_coordinates[1] < delivery_cell[1]:
            function_4()
            agent_coordinates[1] += 1
        elif agent_coordinates[1] > delivery_cell[1]:
            function_3()
            agent_coordinates[1] -= 1
    function_6()

