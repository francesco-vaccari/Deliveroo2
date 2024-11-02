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
    agent_coords = belief_set['agent']['coordinates']
    parcel_coords = belief_set['parcels'][1]['coordinates']
    while agent_coords != parcel_coords:
        if agent_coords[0] > parcel_coords[0]:
            function_1()
            agent_coords[0] -= 1
        elif agent_coords[0] < parcel_coords[0]:
            function_2()
            agent_coords[0] += 1
        if agent_coords[1] > parcel_coords[1]:
            function_3()
            agent_coords[1] -= 1
        elif agent_coords[1] < parcel_coords[1]:
            function_4()
            agent_coords[1] += 1
    function_5()

def function_14():
    global belief_set
    agent_coordinates = belief_set['agent']['coordinates']
    delivery_cell = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'delivery_cell'][0]['cell_coordinates']
    while agent_coordinates != delivery_cell:
        if agent_coordinates[0] < delivery_cell[0]:
            function_2()
        elif agent_coordinates[0] > delivery_cell[0]:
            function_1()
        elif agent_coordinates[1] < delivery_cell[1]:
            function_4()
        else:
            function_3()
        agent_coordinates = belief_set['agent']['coordinates']
    function_6()
    battery_spawn = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'batteries_spawn'][0]['cell_coordinates']
    while agent_coordinates != battery_spawn:
        if agent_coordinates[0] < battery_spawn[0]:
            function_2()
        elif agent_coordinates[0] > battery_spawn[0]:
            function_1()
        elif agent_coordinates[1] < battery_spawn[1]:
            function_4()
        else:
            function_3()
        agent_coordinates = belief_set['agent']['coordinates']

def function_15():
    global belief_set
    function_14()
    function_7()
    function_5()
    function_14()
    function_6()

