def function_7():
    global belief_set
    agent_coordinates = belief_set['agent']['coordinates']
    while belief_set['parcels'][1]['coordinates'] != agent_coordinates:
        if belief_set['parcels'][1]['coordinates'][0] < agent_coordinates[0]:
            function_1()
        elif belief_set['parcels'][1]['coordinates'][0] > agent_coordinates[0]:
            function_2()
        elif belief_set['parcels'][1]['coordinates'][1] < agent_coordinates[1]:
            function_3()
        elif belief_set['parcels'][1]['coordinates'][1] > agent_coordinates[1]:
            function_4()
        agent_coordinates = belief_set['agent']['coordinates']
    function_5()
    while belief_set['map']['grid'][7]['cell_coordinates'
        ] != agent_coordinates:
        if belief_set['map']['grid'][7]['cell_coordinates'][0
            ] < agent_coordinates[0]:
            function_1()
        elif belief_set['map']['grid'][7]['cell_coordinates'][0
            ] > agent_coordinates[0]:
            function_2()
        elif belief_set['map']['grid'][7]['cell_coordinates'][1
            ] < agent_coordinates[1]:
            function_3()
        elif belief_set['map']['grid'][7]['cell_coordinates'][1
            ] > agent_coordinates[1]:
            function_4()
        agent_coordinates = belief_set['agent']['coordinates']
    function_6()

def function_9():
    global belief_set
    key_coordinates = belief_set['keys'][1]['coordinates']
    agent_coordinates = belief_set['agent']['coordinates']
    while agent_coordinates != key_coordinates:
        if key_coordinates[0] < agent_coordinates[0]:
            function_1()
        elif key_coordinates[0] > agent_coordinates[0]:
            function_2()
        elif key_coordinates[1] < agent_coordinates[1]:
            function_3()
        elif key_coordinates[1] > agent_coordinates[1]:
            function_4()
    function_5()
    door_coordinates = belief_set['doors'][1]['coordinates']
    while agent_coordinates != door_coordinates:
        if door_coordinates[0] < agent_coordinates[0]:
            function_1()
        elif door_coordinates[0] > agent_coordinates[0]:
            function_2()
        elif door_coordinates[1] < agent_coordinates[1]:
            function_3()
        elif door_coordinates[1] > agent_coordinates[1]:
            function_4()
    function_6()

def function_10():
    global belief_set
    keys = belief_set['keys']
    parcels = belief_set['parcels']
    agent = belief_set['agent']
    map_grid = belief_set['map']['grid']
    walkable_cells = [cell for cell in map_grid if cell['cell_type'] ==
        'walkable']
    key_cells = [cell for cell in walkable_cells if cell['cell_coordinates'
        ] in [keys[key]['coordinates'] for key in keys]]
    parcel_cells = [cell for cell in walkable_cells if cell[
        'cell_coordinates'] in [parcels[parcel]['coordinates'] for parcel in
        parcels]]
    if key_cells and not agent['has_key']:
        target_key_cell = min(key_cells, key=lambda cell: abs(cell[
            'cell_coordinates'][0] - agent['coordinates'][0]) + abs(cell[
            'cell_coordinates'][1] - agent['coordinates'][1]))
        while agent['coordinates'] != target_key_cell['cell_coordinates']:
            if agent['coordinates'][1] < target_key_cell['cell_coordinates'][1
                ]:
                function_4()
            elif agent['coordinates'][1] > target_key_cell['cell_coordinates'][
                1]:
                function_3()
            elif agent['coordinates'][0] < target_key_cell['cell_coordinates'][
                0]:
                function_2()
            elif agent['coordinates'][0] > target_key_cell['cell_coordinates'][
                0]:
                function_1()
        function_5()
    if parcel_cells and agent['parcels_carried_ids']:
        target_parcel_cell = min(parcel_cells, key=lambda cell: abs(cell[
            'cell_coordinates'][0] - agent['coordinates'][0]) + abs(cell[
            'cell_coordinates'][1] - agent['coordinates'][1]))
        while agent['coordinates'] != target_parcel_cell['cell_coordinates']:
            if agent['coordinates'][1] < target_parcel_cell['cell_coordinates'
                ][1]:
                function_4()
            elif agent['coordinates'][1] > target_parcel_cell[
                'cell_coordinates'][1]:
                function_3()
            elif agent['coordinates'][0] < target_parcel_cell[
                'cell_coordinates'][0]:
                function_2()
            elif agent['coordinates'][0] > target_parcel_cell[
                'cell_coordinates'][0]:
                function_1()
        function_5()

