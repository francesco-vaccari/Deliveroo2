def function_7():
    global belief_set
    agent_coordinates = belief_set['agent']['coordinates']
    nearest_parcel_coordinates = min(belief_set['parcels'], key=lambda p: 
        abs(p['coordinates'][0] - agent_coordinates[0]) + abs(p[
        'coordinates'][1] - agent_coordinates[1]))['coordinates']
    while agent_coordinates[0] != nearest_parcel_coordinates[0]:
        if agent_coordinates[0] < nearest_parcel_coordinates[0]:
            function_2()
        else:
            function_1()
    while agent_coordinates[1] != nearest_parcel_coordinates[1]:
        if agent_coordinates[1] < nearest_parcel_coordinates[1]:
            function_4()
        else:
            function_3()
    function_5()

def function_8():
    global belief_set
    parcels = belief_set['parcels']
    agent = belief_set['agent']
    map_width = belief_set['map']['width']
    map_height = belief_set['map']['height']
    parcel_distances = [(abs(parcel['coordinates'][0] - agent['coordinates'
        ][0]) + abs(parcel['coordinates'][1] - agent['coordinates'][1]),
        parcel) for parcel in parcels if parcel['carried_by_id'] is None]
    parcel_distances.sort(key=lambda x: x[0])
    for distance, parcel in parcel_distances:
        dx = parcel['coordinates'][0] - agent['coordinates'][0]
        dy = parcel['coordinates'][1] - agent['coordinates'][1]
        while dx != 0 and 0 <= agent['coordinates'][0] + dx < map_width:
            if dx > 0:
                function_2()
                dx -= 1
            else:
                function_1()
                dx += 1
        while dy != 0 and 0 <= agent['coordinates'][1] + dy < map_height:
            if dy > 0:
                function_4()
                dy -= 1
            else:
                function_3()
                dy += 1
        if dx == 0 and dy == 0:
            function_5()
            return

def function_9():
    global belief_set
    agent_coordinates = belief_set['agent']['coordinates']
    delivery_cell_coordinates = [cell['cell_coordinates'] for cell in
        belief_set['map']['grid'] if cell['cell_type'] == 'delivery_cell'][0]
    while agent_coordinates != delivery_cell_coordinates:
        if agent_coordinates[0] < delivery_cell_coordinates[0]:
            function_2()
        elif agent_coordinates[0] > delivery_cell_coordinates[0]:
            function_1()
        elif agent_coordinates[1] < delivery_cell_coordinates[1]:
            function_4()
        else:
            function_3()
        agent_coordinates = belief_set['agent']['coordinates']
    function_6()

def function_10():
    global belief_set
    agent = belief_set['agent']
    keys = belief_set['keys']
    batteries = belief_set['batteries']
    if agent['energy'] < 20:
        for battery in batteries:
            while agent['coordinates'] != battery['coordinates']:
                if agent['coordinates'][0] < battery['coordinates'][0]:
                    function_2()
                elif agent['coordinates'][0] > battery['coordinates'][0]:
                    function_1()
                if agent['coordinates'][1] < battery['coordinates'][1]:
                    function_4()
                elif agent['coordinates'][1] > battery['coordinates'][1]:
                    function_3()
        function_5()
    for key in keys:
        while agent['coordinates'] != key['coordinates']:
            if agent['coordinates'][0] < key['coordinates'][0]:
                function_2()
            elif agent['coordinates'][0] > key['coordinates'][0]:
                function_1()
            if agent['coordinates'][1] < key['coordinates'][1]:
                function_4()
            elif agent['coordinates'][1] > key['coordinates'][1]:
                function_3()
    function_5()

def function_11():
    global belief_set
    key_coord = belief_set['keys'][0]['coordinates']
    bat_coord = belief_set['batteries'][0]['coordinates']
    agent_coord = belief_set['agent']['coordinates']
    while belief_set['agent']['energy'] > 30:
        if agent_coord[0] < key_coord[0]:
            function_2()
        elif agent_coord[0] > key_coord[0]:
            function_1()
        elif agent_coord[1] < key_coord[1]:
            function_4()
        elif agent_coord[1] > key_coord[1]:
            function_3()
        if agent_coord == key_coord:
            function_5()
            break
    while belief_set['agent']['energy'] <= 30:
        if agent_coord[0] < bat_coord[0]:
            function_2()
        elif agent_coord[0] > bat_coord[0]:
            function_1()
        elif agent_coord[1] < bat_coord[1]:
            function_4()
        elif agent_coord[1] > bat_coord[1]:
            function_3()
        if agent_coord == bat_coord:
            function_5()
            break

def function_12():
    global belief_set
    agent = belief_set['agent']
    batteries = belief_set['batteries']
    keys = belief_set['keys']
    if agent['energy'] < 50:
        if batteries[0]['coordinates'][0] > agent['coordinates'][0]:
            function_2()
        elif batteries[0]['coordinates'][0] < agent['coordinates'][0]:
            function_1()
        elif batteries[0]['coordinates'][1] > agent['coordinates'][1]:
            function_4()
        elif batteries[0]['coordinates'][1] < agent['coordinates'][1]:
            function_3()
        function_5()
    else:
        if keys[0]['coordinates'][0] > agent['coordinates'][0]:
            function_2()
        elif keys[0]['coordinates'][0] < agent['coordinates'][0]:
            function_1()
        elif keys[0]['coordinates'][1] > agent['coordinates'][1]:
            function_4()
        elif keys[0]['coordinates'][1] < agent['coordinates'][1]:
            function_3()
        function_5()

def function_13():
    global belief_set
    parcel_spawn_location = [cell['cell_coordinates'] for cell in
        belief_set['map']['grid'] if cell['cell_type'] == 'parcels_spawn'][0]
    agent_location = belief_set['agent']['coordinates']
    while agent_location != parcel_spawn_location:
        if agent_location[0] < parcel_spawn_location[0]:
            function_2()
        elif agent_location[0] > parcel_spawn_location[0]:
            function_1()
        elif agent_location[1] < parcel_spawn_location[1]:
            function_4()
        else:
            function_3()
        agent_location = belief_set['agent']['coordinates']
    function_5()
    if belief_set['agent']['energy'] < 30:
        battery_spawn_location = [cell['cell_coordinates'] for cell in
            belief_set['map']['grid'] if cell['cell_type'] == 'batteries_spawn'
            ][0]
        while agent_location != battery_spawn_location:
            if agent_location[0] < battery_spawn_location[0]:
                function_2()
            elif agent_location[0] > battery_spawn_location[0]:
                function_1()
            elif agent_location[1] < battery_spawn_location[1]:
                function_4()
            else:
                function_3()
            agent_location = belief_set['agent']['coordinates']
        function_5()

def function_14():
    global belief_set
    agent_coordinates = belief_set['agent']['coordinates']
    next_cell_coordinates = [agent_coordinates[0] - 1, agent_coordinates[1]]
    next_cell = next((cell for cell in belief_set['map']['grid'] if cell[
        'cell_coordinates'] == next_cell_coordinates), None)
    if next_cell and next_cell['cell_type'] == 'walkable':
        function_1()

def function_15():
    global belief_set
    delivery_cell = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'delivery_cell'][0]['cell_coordinates']
    agent_coordinates = belief_set['agent']['coordinates']
    if agent_coordinates[0] < delivery_cell[0]:
        function_2()
    elif agent_coordinates[0] > delivery_cell[0]:
        function_1()
    elif agent_coordinates[1] < delivery_cell[1]:
        function_4()
    elif agent_coordinates[1] > delivery_cell[1]:
        function_3()
    else:
        function_6()

def function_16():
    global belief_set
    agent = belief_set['agent']
    delivery_cell = next(cell for cell in belief_set['map']['grid'] if cell
        ['cell_type'] == 'delivery_cell')
    while agent['coordinates'] != delivery_cell['cell_coordinates']:
        if agent['coordinates'][0] < delivery_cell['cell_coordinates'][0]:
            function_2()
        elif agent['coordinates'][0] > delivery_cell['cell_coordinates'][0]:
            function_1()
        elif agent['coordinates'][1] < delivery_cell['cell_coordinates'][1]:
            function_4()
        elif agent['coordinates'][1] > delivery_cell['cell_coordinates'][1]:
            function_3()
    function_6()

def function_18():
    global belief_set
    agent_coords = belief_set['agent']['coordinates']
    parcels = belief_set['parcels']
    for parcel in parcels:
        parcel_coords = parcel['coordinates']
        if parcel_coords[0] < agent_coords[0]:
            function_1()
        elif parcel_coords[0] > agent_coords[0]:
            function_2()
        elif parcel_coords[1] < agent_coords[1]:
            function_3()
        elif parcel_coords[1] > agent_coords[1]:
            function_4()
    function_5()
    delivery_cell_coords = [coord['cell_coordinates'] for coord in
        belief_set['map']['grid'] if coord['cell_type'] == 'delivery_cell'][0]
    if delivery_cell_coords[0] < agent_coords[0]:
        function_1()
    elif delivery_cell_coords[0] > agent_coords[0]:
        function_2()
    elif delivery_cell_coords[1] < agent_coords[1]:
        function_3()
    elif delivery_cell_coords[1] > agent_coords[1]:
        function_4()
    function_6()

def function_19():
    global belief_set
    parcel_spawn_cell = [cell['cell_coordinates'] for cell in belief_set[
        'map']['grid'] if cell['cell_type'] == 'parcels_spawn'][0]
    delivery_cell = [cell['cell_coordinates'] for cell in belief_set['map']
        ['grid'] if cell['cell_type'] == 'delivery_cell'][0]
    agent_coordinates = belief_set['agent']['coordinates']
    while agent_coordinates != parcel_spawn_cell:
        if agent_coordinates[0] < parcel_spawn_cell[0]:
            function_2()
        elif agent_coordinates[0] > parcel_spawn_cell[0]:
            function_1()
        elif agent_coordinates[1] < parcel_spawn_cell[1]:
            function_4()
        elif agent_coordinates[1] > parcel_spawn_cell[1]:
            function_3()
        agent_coordinates = belief_set['agent']['coordinates']
    function_5()
    while agent_coordinates != delivery_cell:
        if agent_coordinates[0] < delivery_cell[0]:
            function_2()
        elif agent_coordinates[0] > delivery_cell[0]:
            function_1()
        elif agent_coordinates[1] < delivery_cell[1]:
            function_4()
        elif agent_coordinates[1] > delivery_cell[1]:
            function_3()
        agent_coordinates = belief_set['agent']['coordinates']
    function_6()

def function_20():
    global belief_set
    parcel_spawn_cell = next(cell for cell in belief_set['map']['grid'] if 
        cell['cell_type'] == 'parcels_spawn')['cell_coordinates']
    delivery_cell = next(cell for cell in belief_set['map']['grid'] if cell
        ['cell_type'] == 'delivery_cell')['cell_coordinates']
    agent_coords = belief_set['agent']['coordinates']
    for i in range(30):
        if agent_coords[0] < parcel_spawn_cell[0]:
            function_2()
            agent_coords = belief_set['agent']['coordinates']
        elif agent_coords[0] > parcel_spawn_cell[0]:
            function_1()
            agent_coords = belief_set['agent']['coordinates']
        elif agent_coords[1] < parcel_spawn_cell[1]:
            function_4()
            agent_coords = belief_set['agent']['coordinates']
        elif agent_coords[1] > parcel_spawn_cell[1]:
            function_3()
            agent_coords = belief_set['agent']['coordinates']
        function_5()
        if agent_coords[0] < delivery_cell[0]:
            function_2()
            agent_coords = belief_set['agent']['coordinates']
        elif agent_coords[0] > delivery_cell[0]:
            function_1()
            agent_coords = belief_set['agent']['coordinates']
        elif agent_coords[1] < delivery_cell[1]:
            function_4()
            agent_coords = belief_set['agent']['coordinates']
        elif agent_coords[1] > delivery_cell[1]:
            function_3()
            agent_coords = belief_set['agent']['coordinates']
        function_6()

