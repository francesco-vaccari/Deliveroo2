def function_7():
    global belief_set
    agent_position = belief_set['agent'][1]['coordinates']
    parcel_position = belief_set['parcels'][1]['coordinates']
    delivery_position = [belief_set['map']['grid'][i]['cell_coordinates'] for
        i in range(len(belief_set['map']['grid'])) if belief_set['map'][
        'grid'][i]['cell_type'] == 'delivery_cell'][0]
    while agent_position[0] != parcel_position[0]:
        if agent_position[0] > parcel_position[0]:
            function_1()
            agent_position[0] -= 1
        else:
            function_2()
            agent_position[0] += 1
    while agent_position[1] != parcel_position[1]:
        if agent_position[1] > parcel_position[1]:
            function_3()
            agent_position[1] -= 1
        else:
            function_4()
            agent_position[1] += 1
    function_5()
    while agent_position[0] != delivery_position[0]:
        if agent_position[0] > delivery_position[0]:
            function_1()
            agent_position[0] -= 1
        else:
            function_2()
            agent_position[0] += 1
    while agent_position[1] != delivery_position[1]:
        if agent_position[1] > delivery_position[1]:
            function_3()
            agent_position[1] -= 1
        else:
            function_4()
            agent_position[1] += 1
    function_6()

def function_9():
    global belief_set
    agent = belief_set['agent'][1]
    parcels = belief_set['parcels']
    for parcel in parcels.values():
        if parcel['carried_by_id'] is None:
            parcel_x, parcel_y = parcel['coordinates']
            while agent['coordinates'][0] > parcel_x:
                function_1()
            while agent['coordinates'][0] < parcel_x:
                function_2()
            while agent['coordinates'][1] > parcel_y:
                function_3()
            while agent['coordinates'][1] < parcel_y:
                function_4()
            function_5()

def function_10():
    global belief_set
    agent = belief_set['agent'][1]
    parcels = belief_set['parcels']
    delivery_cells = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'delivery_cell']
    target_parcel = min(parcels.values(), key=lambda p: abs(p['coordinates'
        ][0] - agent['coordinates'][0]) + abs(p['coordinates'][1] - agent[
        'coordinates'][1]))
    target_delivery_cell = min(delivery_cells, key=lambda c: abs(c[
        'cell_coordinates'][0] - agent['coordinates'][0]) + abs(c[
        'cell_coordinates'][1] - agent['coordinates'][1]))
    while agent['coordinates'] != target_parcel['coordinates']:
        if agent['coordinates'][0] < target_parcel['coordinates'][0]:
            function_2()
            agent['coordinates'][0] += 1
        elif agent['coordinates'][0] > target_parcel['coordinates'][0]:
            function_1()
            agent['coordinates'][0] -= 1
        if agent['coordinates'][1] < target_parcel['coordinates'][1]:
            function_4()
            agent['coordinates'][1] += 1
        elif agent['coordinates'][1] > target_parcel['coordinates'][1]:
            function_3()
            agent['coordinates'][1] -= 1
    function_5()
    while agent['coordinates'] != target_delivery_cell['cell_coordinates']:
        if agent['coordinates'][0] < target_delivery_cell['cell_coordinates'][0
            ]:
            function_2()
            agent['coordinates'][0] += 1
        elif agent['coordinates'][0] > target_delivery_cell['cell_coordinates'
            ][0]:
            function_1()
            agent['coordinates'][0] -= 1
        if agent['coordinates'][1] < target_delivery_cell['cell_coordinates'][1
            ]:
            function_4()
            agent['coordinates'][1] += 1
        elif agent['coordinates'][1] > target_delivery_cell['cell_coordinates'
            ][1]:
            function_3()
            agent['coordinates'][1] -= 1
    function_6()

def function_11():
    global belief_set
    while len(belief_set['parcels']) > 0:
        function_10()
        if belief_set['agent'][1]['energy'] < 30:
            function_2()
            function_2()
            function_5()
            function_1()
            function_1()
        function_6()

def function_12():
    global belief_set
    coordinates = belief_set['agent'][1]['coordinates']
    battery_coordinates = belief_set['batteries'][1]['coordinates']
    while coordinates != battery_coordinates:
        if coordinates[0] < battery_coordinates[0]:
            function_2()
        elif coordinates[0] > battery_coordinates[0]:
            function_1()
        elif coordinates[1] < battery_coordinates[1]:
            function_4()
        elif coordinates[1] > battery_coordinates[1]:
            function_3()
        coordinates = belief_set['agent'][1]['coordinates']
    function_5()
    coordinates = belief_set['agent'][1]['coordinates']
    key_coordinates = belief_set['keys'][1]['coordinates']
    while coordinates != key_coordinates:
        if coordinates[0] < key_coordinates[0]:
            function_2()
        elif coordinates[0] > key_coordinates[0]:
            function_1()
        elif coordinates[1] < key_coordinates[1]:
            function_4()
        elif coordinates[1] > key_coordinates[1]:
            function_3()
        coordinates = belief_set['agent'][1]['coordinates']
    function_5()

def function_13():
    global belief_set
    if belief_set['agent'][1]['has_key']:
        function_10()
    else:
        function_8()
    function_11()
    if belief_set['map']['grid'][belief_set['agent'][1]['coordinates'][0]][
        belief_set['agent'][1]['coordinates'][1]]['cell_type'] == 'door':
        function_5()
    if belief_set['agent'][1]['energy'] < 30:
        function_1()
        function_2()
        function_3()
        function_4()

def function_14():
    global belief_set
    agent = belief_set['agent'][1]
    if agent['energy'] < 30:
        pass
    else:
        if agent['parcels_carried_ids']:
            function_10()
        else:
            function_11()
        pass

def function_15():
    global belief_set
    if belief_set['agent'][1]['energy'] > 10:
        function_10()
    else:
        function_14()

def function_16():
    global belief_set
    agent = belief_set['agent'][1]
    parcels = belief_set['parcels']
    delivery_cell = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'delivery_cell'][0]
    parcel_coords = sorted(parcels.values(), key=lambda x: abs(x[
        'coordinates'][0] - agent['coordinates'][0]) + abs(x['coordinates']
        [1] - agent['coordinates'][1]))[0]['coordinates']
    while agent['coordinates'] != parcel_coords:
        if agent['coordinates'][0] < parcel_coords[0]:
            function_2()
        elif agent['coordinates'][0] > parcel_coords[0]:
            function_1()
        if agent['coordinates'][1] < parcel_coords[1]:
            function_4()
        elif agent['coordinates'][1] > parcel_coords[1]:
            function_3()
    function_5()
    while agent['coordinates'] != delivery_cell['coordinates']:
        if agent['coordinates'][0] < delivery_cell['coordinates'][0]:
            function_2()
        elif agent['coordinates'][0] > delivery_cell['coordinates'][0]:
            function_1()
        if agent['coordinates'][1] < delivery_cell['coordinates'][1]:
            function_4()
        elif agent['coordinates'][1] > delivery_cell['coordinates'][1]:
            function_3()
    function_6()
