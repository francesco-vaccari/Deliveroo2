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
    agent_coords = belief_set['agent']['coordinates']
    parcel_coords = belief_set['parcel'][1]['coordinates']
    if agent_coords == parcel_coords:
        function_5()
    else:
        if agent_coords[0] < parcel_coords[0]:
            function_2()
        elif agent_coords[0] > parcel_coords[0]:
            function_1()
        if agent_coords[1] < parcel_coords[1]:
            function_4()
        elif agent_coords[1] > parcel_coords[1]:
            function_3()

def function_14():
    global belief_set
    agent = belief_set['agent']
    map_grid = belief_set['map']['grid']
    delivery_cells = [cell for cell in map_grid if cell['cell_type'] in [
        'delivery_cell', 'double_delivery_cell']]
    nearest_delivery_cell = min(delivery_cells, key=lambda cell: abs(cell[
        'cell_coordinates'][0] - agent['coordinates'][0]) + abs(cell[
        'cell_coordinates'][1] - agent['coordinates'][1]))
    while agent['coordinates'] != nearest_delivery_cell['cell_coordinates']:
        if agent['coordinates'][0] < nearest_delivery_cell['cell_coordinates'][
            0]:
            function_2()
        elif agent['coordinates'][0] > nearest_delivery_cell['cell_coordinates'
            ][0]:
            function_1()
        elif agent['coordinates'][1] < nearest_delivery_cell['cell_coordinates'
            ][1]:
            function_4()
        elif agent['coordinates'][1] > nearest_delivery_cell['cell_coordinates'
            ][1]:
            function_3()
    function_6()

