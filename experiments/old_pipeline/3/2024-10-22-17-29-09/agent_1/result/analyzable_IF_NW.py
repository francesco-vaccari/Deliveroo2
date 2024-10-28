def function_8():
    global belief_set
    agent_coordinates = belief_set['agent']['coordinates']
    delivery_cell_coordinates = [cell['cell_coordinates'] for cell in
        belief_set['map']['grid'] if cell['cell_type'] in ['delivery_cell',
        'double_delivery_cell']][0]
    while agent_coordinates[0] < delivery_cell_coordinates[0]:
        function_2()
        agent_coordinates[0] += 1
    while agent_coordinates[0] > delivery_cell_coordinates[0]:
        function_1()
        agent_coordinates[0] -= 1
    while agent_coordinates[1] < delivery_cell_coordinates[1]:
        function_4()
        agent_coordinates[1] += 1
    while agent_coordinates[1] > delivery_cell_coordinates[1]:
        function_3()
        agent_coordinates[1] -= 1
    function_6()

def function_9():
    global belief_set
    agent_location = belief_set['agent']['coordinates']
    parcel_location = belief_set['parcel'][1]['coordinates']
    delivery_location = [cell['cell_coordinates'] for cell in belief_set[
        'map']['grid'] if 'delivery' in cell['cell_type']][0]
    if agent_location[0] < delivery_location[0]:
        function_2()
    elif agent_location[0] > delivery_location[0]:
        function_1()
    elif agent_location[1] < delivery_location[1]:
        function_4()
    elif agent_location[1] > delivery_location[1]:
        function_3()
    else:
        function_6()

def function_10():
    global belief_set
    agent = belief_set['agent']
    parcels = belief_set['parcel']
    map = belief_set['map']['grid']
    for parcel in parcels.values():
        if parcel['carried_by_id'] == agent['id']:
            for cell in map:
                if cell['cell_type'] in ['delivery_cell',
                    'double_delivery_cell'] and agent['coordinates'] != cell[
                    'cell_coordinates']:
                    if cell['cell_coordinates'][0] < agent['coordinates'][0]:
                        function_1()
                    elif cell['cell_coordinates'][0] > agent['coordinates'][0]:
                        function_2()
                    elif cell['cell_coordinates'][1] < agent['coordinates'][1]:
                        function_3()
                    elif cell['cell_coordinates'][1] > agent['coordinates'][1]:
                        function_4()
            if agent['coordinates'] == cell['cell_coordinates']:
                function_6()
                break

def function_11():
    global belief_set
    agent = belief_set['agent']
    parcels = belief_set['parcel']
    delivery_cell = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] in ['double_delivery_cell', 'delivery_cell']][0]
    nearest_parcel = min(parcels.values(), key=lambda parcel: abs(parcel[
        'coordinates'][0] - agent['coordinates'][0]) + abs(parcel[
        'coordinates'][1] - agent['coordinates'][1]))
    if agent['coordinates'][0] < nearest_parcel['coordinates'][0]:
        function_2()
    elif agent['coordinates'][0] > nearest_parcel['coordinates'][0]:
        function_1()
    elif agent['coordinates'][1] < nearest_parcel['coordinates'][1]:
        function_4()
    elif agent['coordinates'][1] > nearest_parcel['coordinates'][1]:
        function_3()
    else:
        function_5()
    if agent['coordinates'] == nearest_parcel['coordinates']:
        if agent['coordinates'][0] < delivery_cell['cell_coordinates'][0]:
            function_2()
        elif agent['coordinates'][0] > delivery_cell['cell_coordinates'][0]:
            function_1()
        elif agent['coordinates'][1] < delivery_cell['cell_coordinates'][1]:
            function_4()
        elif agent['coordinates'][1] > delivery_cell['cell_coordinates'][1]:
            function_3()
        else:
            function_6()

def function_12():
    global belief_set
    coordinates = belief_set['agent']['coordinates']
    parcels = belief_set['parcel']
    if len(parcels) > 0:
        parcel = parcels[list(parcels.keys())[0]]
        if parcel['carried_by_id'] == 1:
            if coordinates[0] < 2:
                function_2()
            elif coordinates[0] > 2:
                function_1()
            elif coordinates[1] < 1:
                function_4()
            elif coordinates[1] > 1:
                function_3()
            else:
                function_6()
    elif coordinates[0] < 2:
        function_2()
    elif coordinates[0] > 2:
        function_1()
    elif coordinates[1] < 1:
        function_4()
    elif coordinates[1] > 1:
        function_3()
    else:
        function_5()

def function_13():
    global belief_set
    agent_coords = belief_set['agent']['coordinates']
    delivery_cells = [cell['cell_coordinates'] for cell in belief_set['map'
        ]['grid'] if 'delivery' in cell['cell_type']]
    destination = min(delivery_cells, key=lambda cell: abs(cell[0] -
        agent_coords[0]) + abs(cell[1] - agent_coords[1]))
    while agent_coords != destination:
        if agent_coords[0] > destination[0]:
            function_1()
        elif agent_coords[0] < destination[0]:
            function_2()
        if agent_coords[1] > destination[1]:
            function_3()
        elif agent_coords[1] < destination[1]:
            function_4()
    function_6()

