def function_7():
    global belief_set
    agent = belief_set['agent'][1]
    parcels = belief_set['parcels']
    map_grid = belief_set['map']['grid']
    spawn_points = [cell for cell in map_grid if cell['cell_type'] ==
        'parcels_spawn']
    nearest_spawn_point = min(spawn_points, key=lambda cell: abs(cell[
        'cell_coordinates'][0] - agent['coordinates'][0]) + abs(cell[
        'cell_coordinates'][1] - agent['coordinates'][1]))
    while agent['coordinates'] != nearest_spawn_point['cell_coordinates']:
        if agent['coordinates'][0] < nearest_spawn_point['cell_coordinates'][0
            ]:
            function_2()
        elif agent['coordinates'][0] > nearest_spawn_point['cell_coordinates'][
            0]:
            function_1()
        if agent['coordinates'][1] < nearest_spawn_point['cell_coordinates'][1
            ]:
            function_4()
        elif agent['coordinates'][1] > nearest_spawn_point['cell_coordinates'][
            1]:
            function_3()
    for parcel in parcels.values():
        if parcel['coordinates'] == agent['coordinates'] and parcel[
            'carried_by_id'] is None:
            function_5()

def function_8():
    global belief_set
    agent = belief_set['agent'][1]
    parcels = belief_set['parcels']
    map = belief_set['map']['grid']
    for parcel in parcels.values():
        if parcel['carried_by_id'] == agent['id']:
            for cell in map:
                if cell['cell_type'] == 'delivery_cell':
                    while agent['coordinates'][0] < cell['cell_coordinates'][0
                        ]:
                        function_2()
                    while agent['coordinates'][0] > cell['cell_coordinates'][0
                        ]:
                        function_1()
                    while agent['coordinates'][1] < cell['cell_coordinates'][1
                        ]:
                        function_4()
                    while agent['coordinates'][1] > cell['cell_coordinates'][1
                        ]:
                        function_3()
                    function_6()
                    break
            break
        else:
            if agent['coordinates'][0] < parcel['coordinates'][0]:
                function_2()
            elif agent['coordinates'][0] > parcel['coordinates'][0]:
                function_1()
            elif agent['coordinates'][1] < parcel['coordinates'][1]:
                function_4()
            elif agent['coordinates'][1] > parcel['coordinates'][1]:
                function_3()
            function_5()
            break

def function_9():
    global belief_set
    delivery_cell = next(cell for cell in belief_set['map']['grid'] if cell
        ['cell_type'] == 'delivery_cell')
    agent = belief_set['agent'][1]
    while agent['coordinates'] != delivery_cell['cell_coordinates']:
        if agent['coordinates'][0] > delivery_cell['cell_coordinates'][0]:
            function_1()
        elif agent['coordinates'][0] < delivery_cell['cell_coordinates'][0]:
            function_2()
        elif agent['coordinates'][1] > delivery_cell['cell_coordinates'][1]:
            function_3()
        else:
            function_4()
    function_6()

def function_10():
    global belief_set
    delivery_cell = [cell['cell_coordinates'] for cell in belief_set['map']
        ['grid'] if cell['cell_type'] == 'delivery_cell'][0]
    agent_position = belief_set['agent'][1]['coordinates']
    if agent_position[0] < delivery_cell[0]:
        function_2()
    elif agent_position[0] > delivery_cell[0]:
        function_1()
    elif agent_position[1] < delivery_cell[1]:
        function_4()
    elif agent_position[1] > delivery_cell[1]:
        function_3()
    else:
        function_6()

