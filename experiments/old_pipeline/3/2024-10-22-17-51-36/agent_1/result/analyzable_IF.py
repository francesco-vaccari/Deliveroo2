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
    agent_pos = belief_set['agent']['coordinates']
    key_pos = belief_set['keys'][1]['coordinates']
    door_pos = belief_set['doors'][1]['coordinates']
    if agent_pos[0] > key_pos[0]:
        function_1()
    elif agent_pos[0] < key_pos[0]:
        function_2()
    elif agent_pos[1] > key_pos[1]:
        function_3()
    elif agent_pos[1] < key_pos[1]:
        function_4()
    else:
        function_5()
    if belief_set['agent']['has_key'] is True:
        if agent_pos[0] > door_pos[0]:
            function_1()
        elif agent_pos[0] < door_pos[0]:
            function_2()
        elif agent_pos[1] > door_pos[1]:
            function_3()
        elif agent_pos[1] < door_pos[1]:
            function_4()

def function_8():
    global belief_set
    while belief_set['agent']['coordinates'] != belief_set['keys'][1][
        'coordinates']:
        if belief_set['agent']['coordinates'][0] < belief_set['keys'][1][
            'coordinates'][0]:
            function_2()
        elif belief_set['agent']['coordinates'][0] > belief_set['keys'][1][
            'coordinates'][0]:
            function_1()
        elif belief_set['agent']['coordinates'][1] < belief_set['keys'][1][
            'coordinates'][1]:
            function_4()
        elif belief_set['agent']['coordinates'][1] > belief_set['keys'][1][
            'coordinates'][1]:
            function_3()
    function_5()
    while belief_set['agent']['coordinates'] != belief_set['doors'][1][
        'coordinates']:
        if belief_set['agent']['coordinates'][0] < belief_set['doors'][1][
            'coordinates'][0]:
            function_2()
        elif belief_set['agent']['coordinates'][0] > belief_set['doors'][1][
            'coordinates'][0]:
            function_1()
        elif belief_set['agent']['coordinates'][1] < belief_set['doors'][1][
            'coordinates'][1]:
            function_4()
        elif belief_set['agent']['coordinates'][1] > belief_set['doors'][1][
            'coordinates'][1]:
            function_3()
    function_6()

def function_9():
    global belief_set
    agent = belief_set['agent']
    parcels = belief_set['parcels']
    map_info = belief_set['map']['grid']
    parcel_coordinate = None
    delivery_coordinate = None
    for parcel in parcels.values():
        if parcel['carried_by_id'] == None:
            parcel_coordinate = parcel['coordinates']
            break
    for cell in map_info:
        if 'delivery' in cell['cell_type']:
            delivery_coordinate = cell['cell_coordinates']
            break
    while agent['coordinates'] != parcel_coordinate:
        if agent['coordinates'][0] < parcel_coordinate[0]:
            function_2()
        elif agent['coordinates'][0] > parcel_coordinate[0]:
            function_1()
        elif agent['coordinates'][1] < parcel_coordinate[1]:
            function_4()
        elif agent['coordinates'][1] > parcel_coordinate[1]:
            function_3()
    function_5()
    while agent['coordinates'] != delivery_coordinate:
        if agent['coordinates'][0] < delivery_coordinate[0]:
            function_2()
        elif agent['coordinates'][0] > delivery_coordinate[0]:
            function_1()
        elif agent['coordinates'][1] < delivery_coordinate[1]:
            function_4()
        elif agent['coordinates'][1] > delivery_coordinate[1]:
            function_3()
    function_6()

def function_10():
    global belief_set
    closest_parcel = min(belief_set['parcels'].items(), key=lambda x: abs(x
        [1]['coordinates'][0] - belief_set['agent']['coordinates'][0]) +
        abs(x[1]['coordinates'][1] - belief_set['agent']['coordinates'][1]))
    while belief_set['agent']['coordinates'] != closest_parcel[1]['coordinates'
        ]:
        if belief_set['agent']['coordinates'][0] < closest_parcel[1][
            'coordinates'][0]:
            function_2()
        elif belief_set['agent']['coordinates'][0] > closest_parcel[1][
            'coordinates'][0]:
            function_1()
        if belief_set['agent']['coordinates'][1] < closest_parcel[1][
            'coordinates'][1]:
            function_4()
        elif belief_set['agent']['coordinates'][1] > closest_parcel[1][
            'coordinates'][1]:
            function_3()
    function_5()
    closest_delivery_cell = min(filter(lambda x: x['cell_type'] in [
        'delivery_cell', 'double_delivery_cell'], belief_set['map']['grid']
        ), key=lambda x: abs(x['cell_coordinates'][0] - belief_set['agent']
        ['coordinates'][0]) + abs(x['cell_coordinates'][1] - belief_set[
        'agent']['coordinates'][1]))
    while belief_set['agent']['coordinates'] != closest_delivery_cell[
        'cell_coordinates']:
        if belief_set['agent']['coordinates'][0] < closest_delivery_cell[
            'cell_coordinates'][0]:
            function_2()
        elif belief_set['agent']['coordinates'][0] > closest_delivery_cell[
            'cell_coordinates'][0]:
            function_1()
        if belief_set['agent']['coordinates'][1] < closest_delivery_cell[
            'cell_coordinates'][1]:
            function_4()
        elif belief_set['agent']['coordinates'][1] > closest_delivery_cell[
            'cell_coordinates'][1]:
            function_3()
    function_6()

