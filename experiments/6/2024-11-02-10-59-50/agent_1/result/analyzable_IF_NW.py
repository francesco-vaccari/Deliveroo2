def function_7():
    global belief_set
    agent_loc = belief_set['agent'][1]['coordinates']
    parcel_loc = belief_set['parcels'][1]['coordinates']
    delivery_loc = [cell['cell_coordinates'] for cell in belief_set['map'][
        'grid'] if cell['cell_type'] == 'delivery_cell'][0]
    while agent_loc != parcel_loc:
        if agent_loc[0] < parcel_loc[0]:
            function_2()
        elif agent_loc[0] > parcel_loc[0]:
            function_1()
        elif agent_loc[1] < parcel_loc[1]:
            function_4()
        else:
            function_3()
        agent_loc = belief_set['agent'][1]['coordinates']
    function_5()
    while agent_loc != delivery_loc:
        if agent_loc[0] < delivery_loc[0]:
            function_2()
        elif agent_loc[0] > delivery_loc[0]:
            function_1()
        elif agent_loc[1] < delivery_loc[1]:
            function_4()
        else:
            function_3()
        agent_loc = belief_set['agent'][1]['coordinates']
    function_6()

def function_8():
    global belief_set
    agent = belief_set['agent'][1]
    parcel_spawn_cell = [cell for cell in belief_set['map']['grid'] if cell
        ['cell_type'] == 'parcels_spawn'][0]
    parcel_spawn_coordinates = parcel_spawn_cell['cell_coordinates']
    while agent['coordinates'] != parcel_spawn_coordinates:
        if agent['coordinates'][0] > parcel_spawn_coordinates[0]:
            function_1()
        elif agent['coordinates'][0] < parcel_spawn_coordinates[0]:
            function_2()
        elif agent['coordinates'][1] > parcel_spawn_coordinates[1]:
            function_3()
        elif agent['coordinates'][1] < parcel_spawn_coordinates[1]:
            function_4()
    function_5()

def function_10():
    global belief_set
    agent = belief_set['agent'][1]
    battery_spawn = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'batteries_spawn'][0]['cell_coordinates']
    if agent['energy'] < 30:
        if agent['coordinates'] == battery_spawn:
            function_5()
        else:
            function_9()
    elif agent['coordinates'][0] < battery_spawn[0]:
        function_2()
    elif agent['coordinates'][0] > battery_spawn[0]:
        function_1()
    elif agent['coordinates'][1] < battery_spawn[1]:
        function_4()
    elif agent['coordinates'][1] > battery_spawn[1]:
        function_3()

def function_11():
    global belief_set
    agent_coordinates = belief_set['agent'][1]['coordinates']
    for cell in belief_set['map']['grid']:
        if cell['cell_type'] == 'parcels_spawn':
            spawn_coordinates = cell['cell_coordinates']
            break
    if agent_coordinates == spawn_coordinates:
        function_5()
    else:
        function_9()

