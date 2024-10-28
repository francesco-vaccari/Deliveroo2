def function_8():
    global belief_set
    parcel = next(iter(belief_set['parcel'].values()))
    agent = belief_set['agent']
    if agent['coordinates'] == parcel['coordinates']:
        function_5()
    elif agent['coordinates'][0] < parcel['coordinates'][0]:
        function_2()
    elif agent['coordinates'][0] > parcel['coordinates'][0]:
        function_1()
    elif agent['coordinates'][1] < parcel['coordinates'][1]:
        function_4()
    elif agent['coordinates'][1] > parcel['coordinates'][1]:
        function_3()

def function_10():
    global belief_set
    agent = belief_set['agent']
    parcel = belief_set['parcel'][1]
    if agent['coordinates'] == parcel['coordinates'] and 1 in agent[
        'parcels_carried_ids']:
        function_4()
    elif agent['has_key'] and belief_set['door'][1]['coordinates'] in [[
        agent['coordinates'][0] + 1, agent['coordinates'][1]], [agent[
        'coordinates'][0] - 1, agent['coordinates'][1]], [agent[
        'coordinates'][0], agent['coordinates'][1] - 1], [agent[
        'coordinates'][0], agent['coordinates'][1] + 1]]:
        function_5()
    elif agent['coordinates'] == belief_set['map']['grid'][3][
        'cell_coordinates'] and 1 in agent['parcels_carried_ids']:
        function_6()
    else:
        function_2()
        function_4()

def function_11():
    global belief_set
    agent_coordinates = belief_set['agent']['coordinates']
    parcel_coordinates = belief_set['parcel'][1]['coordinates']
    delivery_cell_coordinates = [cell['cell_coordinates'] for cell in
        belief_set['map']['grid'] if cell['cell_type'] ==
        'double_delivery_cell' or cell['cell_type'] == 'delivery_cell'][0]
    if belief_set['agent']['has_key']:
        for door in belief_set['door'].values():
            if door['coordinates'] == agent_coordinates:
                function_7()
    if parcel_coordinates == agent_coordinates and 1 not in belief_set['agent'
        ]['parcels_carried_ids']:
        function_9()
    if delivery_cell_coordinates[0] < agent_coordinates[0]:
        function_1()
    elif delivery_cell_coordinates[0] > agent_coordinates[0]:
        function_2()
    elif delivery_cell_coordinates[1] < agent_coordinates[1]:
        function_3()
    elif delivery_cell_coordinates[1] > agent_coordinates[1]:
        function_4()
    if delivery_cell_coordinates == agent_coordinates:
        function_6()

def function_12():
    global belief_set
    agent = belief_set['agent']
    map = belief_set['map']
    parcel = belief_set['parcel'][1]
    key = belief_set['key'][1]
    door_1 = belief_set['door'][1]
    door_2 = belief_set['door'][2]
    if agent['coordinates'] == parcel['coordinates']:
        function_5()
    elif agent['coordinates'] == key['coordinates']:
        function_5()
    elif (agent['coordinates'] == door_1['coordinates'] or agent[
        'coordinates'] == door_2['coordinates']) and agent['has_key']:
        function_5()
    else:
        for cell in map['grid']:
            if cell['cell_type'] == 'delivery_cell' and cell['cell_coordinates'
                ][0] > agent['coordinates'][0]:
                function_2()
            elif cell['cell_type'] == 'delivery_cell' and cell[
                'cell_coordinates'][0] < agent['coordinates'][0]:
                function_1()
            elif cell['cell_type'] == 'delivery_cell' and cell[
                'cell_coordinates'][1] > agent['coordinates'][1]:
                function_4()
            elif cell['cell_type'] == 'delivery_cell' and cell[
                'cell_coordinates'][1] < agent['coordinates'][1]:
                function_3()

def function_13():
    global belief_set
    agent_coords = belief_set['agent']['coordinates']
    for cell in belief_set['map']['grid']:
        if cell['cell_type'] == 'double_delivery_cell':
            delivery_coords = cell['cell_coordinates']
            break
    if agent_coords[0] < delivery_coords[0] and belief_set['map']['grid'][
        agent_coords[0] + 1][agent_coords[1]]['cell_type'] != 'non_walkable':
        function_2()
    elif agent_coords[0] > delivery_coords[0] and belief_set['map']['grid'][
        agent_coords[0] - 1][agent_coords[1]]['cell_type'] != 'non_walkable':
        function_1()
    elif agent_coords[1] < delivery_coords[1] and belief_set['map']['grid'][
        agent_coords[0]][agent_coords[1] + 1]['cell_type'] != 'non_walkable':
        function_4()
    elif agent_coords[1] > delivery_coords[1] and belief_set['map']['grid'][
        agent_coords[0]][agent_coords[1] - 1]['cell_type'] != 'non_walkable':
        function_3()
    if agent_coords == delivery_coords:
        function_6()

def function_14():
    global belief_set
    agent_coords = belief_set['agent']['coordinates']
    delivery_cells = [cell['cell_coordinates'] for cell in belief_set['map'
        ]['grid'] if 'delivery' in cell['cell_type']]
    for cell in delivery_cells:
        if cell[0] < agent_coords[0]:
            function_1()
        elif cell[0] > agent_coords[0]:
            function_2()
        if cell[1] < agent_coords[1]:
            function_3()
        elif cell[1] > agent_coords[1]:
            function_4()
    if belief_set['agent']['parcels_carried_ids']:
        function_6()

def function_15():
    global belief_set
    agt_crd = belief_set['agent']['coordinates']
    map_grid = belief_set['map']['grid']
    walkable_cells = [c['cell_coordinates'] for c in map_grid if c[
        'cell_type'] == 'walkable']
    target_crd = min(walkable_cells, key=lambda c: abs(c[0] - agt_crd[0]) +
        abs(c[1] - agt_crd[1]))
    while agt_crd != target_crd:
        if agt_crd[0] < target_crd[0]:
            function_2()
        elif agt_crd[0] > target_crd[0]:
            function_1()
        elif agt_crd[1] < target_crd[1]:
            function_4()
        elif agt_crd[1] > target_crd[1]:
            function_3()
        function_5()
        function_7()
        function_9()
        agt_crd = belief_set['agent']['coordinates']

def function_16():
    global belief_set
    agent_position = belief_set['agent']['coordinates']
    parcel_position = belief_set['parcel'][1]['coordinates']
    delivery_cell_position = [cell['cell_coordinates'] for cell in
        belief_set['map']['grid'] if cell['cell_type'] in [
        'double_delivery_cell', 'delivery_cell']][0]
    while agent_position != parcel_position:
        if agent_position[0] < parcel_position[0]:
            function_2()
        elif agent_position[0] > parcel_position[0]:
            function_1()
        elif agent_position[1] < parcel_position[1]:
            function_4()
        elif agent_position[1] > parcel_position[1]:
            function_3()
    function_5()
    while agent_position != delivery_cell_position:
        if agent_position[0] < delivery_cell_position[0]:
            function_2()
        elif agent_position[0] > delivery_cell_position[0]:
            function_1()
        elif agent_position[1] < delivery_cell_position[1]:
            function_4()
        elif agent_position[1] > delivery_cell_position[1]:
            function_3()
    function_6()

def function_17():
    global belief_set
    while belief_set['agent']['coordinates'] != [3, 0]:
        if belief_set['agent']['coordinates'][0] < 3:
            function_2()
        elif belief_set['agent']['coordinates'][1] > 0:
            function_3()
    if belief_set['agent']['parcels_carried_ids']:
        function_6()

def function_18():
    global belief_set
    if belief_set['agent']['parcels_carried_ids']:
        if belief_set['agent']['coordinates'] == [3, 0]:
            function_6()
        elif belief_set['agent']['coordinates'][0] < 3:
            function_2()
        elif belief_set['agent']['coordinates'][1] > 0:
            function_3()

