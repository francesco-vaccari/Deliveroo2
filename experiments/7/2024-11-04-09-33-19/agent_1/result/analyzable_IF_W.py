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


def function_11():
    global belief_set
    for parcel in belief_set['parcels']:
        if parcel['carried_by_id'] is None:
            target_coordinates = parcel['coordinates']
            break
    x_diff = belief_set['agent']['coordinates'][0] - target_coordinates[0]
    y_diff = belief_set['agent']['coordinates'][1] - target_coordinates[1]
    if x_diff > 0:
        for _ in range(x_diff):
            function_1()
    elif x_diff < 0:
        for _ in range(-x_diff):
            function_2()
    if y_diff > 0:
        for _ in range(y_diff):
            function_3()
    elif y_diff < 0:
        for _ in range(-y_diff):
            function_4()
    function_5()

def function_12():
    global belief_set
    delivery_cell = [cell['cell_coordinates'] for cell in belief_set['map']
        ['grid'] if cell['cell_type'] == 'delivery_cell'][0]
    agent_coords = belief_set['agent']['coordinates']
    while agent_coords != delivery_cell:
        if agent_coords[0] < delivery_cell[0]:
            function_2()
        elif agent_coords[0] > delivery_cell[0]:
            function_1()
        elif agent_coords[1] < delivery_cell[1]:
            function_4()
        elif agent_coords[1] > delivery_cell[1]:
            function_3()
        agent_coords = belief_set['agent']['coordinates']
    function_6()

def function_14():
    global belief_set
    battery_coords = belief_set['batteries'][0]['coordinates']
    while belief_set['agent']['coordinates'] != battery_coords:
        if belief_set['agent']['coordinates'][0] < battery_coords[0]:
            function_2()
        elif belief_set['agent']['coordinates'][0] > battery_coords[0]:
            function_1()
        elif belief_set['agent']['coordinates'][1] < battery_coords[1]:
            function_4()
        elif belief_set['agent']['coordinates'][1] > battery_coords[1]:
            function_3()
    function_5()

def function_15():
    global belief_set
    while belief_set['agent']['coordinates'] != [0, 0]:
        if belief_set['agent']['coordinates'][0] > 0:
            function_1()
        else:
            function_3()
    function_5()
    while belief_set['agent']['coordinates'] != [1, 3]:
        if belief_set['agent']['coordinates'][0] < 1:
            function_2()
        else:
            function_4()
    function_6()

