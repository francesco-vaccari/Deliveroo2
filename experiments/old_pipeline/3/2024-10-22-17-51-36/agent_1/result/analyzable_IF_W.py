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

