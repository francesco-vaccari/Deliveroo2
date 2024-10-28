def function_7():
    global belief_set
    agent = belief_set['agent']
    keys = belief_set['keys']
    doors = belief_set['doors']
    if not agent['has_key']:
        nearest_key = min(keys.values(), key=lambda k: abs(k['coordinates']
            [0] - agent['coordinates'][0]) + abs(k['coordinates'][1] -
            agent['coordinates'][1]))
        if agent['coordinates'][0] > nearest_key['coordinates'][0]:
            function_1()
        elif agent['coordinates'][0] < nearest_key['coordinates'][0]:
            function_2()
        elif agent['coordinates'][1] > nearest_key['coordinates'][1]:
            function_3()
        elif agent['coordinates'][1] < nearest_key['coordinates'][1]:
            function_4()
        function_5()
    nearest_door = min(doors.values(), key=lambda d: abs(d['coordinates'][0
        ] - agent['coordinates'][0]) + abs(d['coordinates'][1] - agent[
        'coordinates'][1]))
    if agent['coordinates'][0] > nearest_door['coordinates'][0]:
        function_1()
    elif agent['coordinates'][0] < nearest_door['coordinates'][0]:
        function_2()
    elif agent['coordinates'][1] > nearest_door['coordinates'][1]:
        function_3()
    elif agent['coordinates'][1] < nearest_door['coordinates'][1]:
        function_4()

def function_8():
    global belief_set
    parcel_coordinates = belief_set['parcels'][1]['coordinates']
    agent_coordinates = belief_set['agent']['coordinates']
    while parcel_coordinates != agent_coordinates:
        if parcel_coordinates[0] < agent_coordinates[0]:
            function_1()
        elif parcel_coordinates[0] > agent_coordinates[0]:
            function_2()
        if parcel_coordinates[1] < agent_coordinates[1]:
            function_3()
        elif parcel_coordinates[1] > agent_coordinates[1]:
            function_4()
    function_5()

def function_9():
    global belief_set
    agent_coordinates = belief_set['agent']['coordinates']
    parcels = belief_set['parcels']
    closest_parcel_id = min(parcels, key=lambda x: abs(parcels[x][
        'coordinates'][0] - agent_coordinates[0]) + abs(parcels[x][
        'coordinates'][1] - agent_coordinates[1]))
    closest_parcel = parcels[closest_parcel_id]
    while agent_coordinates != closest_parcel['coordinates']:
        if agent_coordinates[0] < closest_parcel['coordinates'][0]:
            function_2()
            agent_coordinates[0] += 1
        elif agent_coordinates[0] > closest_parcel['coordinates'][0]:
            function_1()
            agent_coordinates[0] -= 1
        if agent_coordinates[1] < closest_parcel['coordinates'][1]:
            function_4()
            agent_coordinates[1] += 1
        elif agent_coordinates[1] > closest_parcel['coordinates'][1]:
            function_3()
            agent_coordinates[1] -= 1
    function_5()

def function_10():
    global belief_set
    delivery_cell = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'delivery_cell'][0]['cell_coordinates']
    agent_coordinates = belief_set['agent']['coordinates']
    if agent_coordinates[0] > delivery_cell[0]:
        function_1()
    elif agent_coordinates[0] < delivery_cell[0]:
        function_2()
    elif agent_coordinates[1] > delivery_cell[1]:
        function_3()
    elif agent_coordinates[1] < delivery_cell[1]:
        function_4()
    else:
        function_6()

def function_11():
    global belief_set
    delivery_cell = next(cell for cell in belief_set['map']['grid'] if cell
        ['cell_type'] == 'delivery_cell')
    agent = belief_set['agent']
    if agent['coordinates'][0] < delivery_cell['cell_coordinates'][0]:
        function_2()
    elif agent['coordinates'][0] > delivery_cell['cell_coordinates'][0]:
        function_1()
    elif agent['coordinates'][1] < delivery_cell['cell_coordinates'][1]:
        function_4()
    else:
        function_3()

