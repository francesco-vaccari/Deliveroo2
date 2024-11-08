def function_8():
    global belief_set
    current_cell = belief_set['agent']['coordinates']
    if {'cell_coordinates': [current_cell[0] - 1, current_cell[1]],
        'cell_type': 'walkable'} in belief_set['map']['grid']:
        function_1()
    elif {'cell_coordinates': [current_cell[0] + 1, current_cell[1]],
        'cell_type': 'walkable'} in belief_set['map']['grid']:
        function_2()
    elif {'cell_coordinates': [current_cell[0], current_cell[1] - 1],
        'cell_type': 'walkable'} in belief_set['map']['grid']:
        function_3()
    elif {'cell_coordinates': [current_cell[0], current_cell[1] + 1],
        'cell_type': 'walkable'} in belief_set['map']['grid']:
        function_4()
    for parcel in belief_set['parcels'].values():
        if parcel['coordinates'] == belief_set['agent']['coordinates']:
            function_5()

def function_10():
    global belief_set
    agent = belief_set['agent']
    map_grid = belief_set['map']['grid']
    delivery_cell = next((cell for cell in map_grid if cell['cell_type'] ==
        'delivery_cell'), None)
    if not delivery_cell:
        return
    delivery_coordinates = delivery_cell['cell_coordinates']
    while agent['coordinates'] != delivery_coordinates and agent['energy'
        ] > 10:
        if agent['coordinates'][0] > delivery_coordinates[0]:
            function_1()
        elif agent['coordinates'][0] < delivery_coordinates[0]:
            function_2()
        elif agent['coordinates'][1] > delivery_coordinates[1]:
            function_3()
        elif agent['coordinates'][1] < delivery_coordinates[1]:
            function_4()
    if agent['coordinates'] == delivery_coordinates and agent[
        'parcels_carried_ids']:
        function_6()

def function_12():
    global belief_set
    agent_coords = belief_set['agent']['coordinates']
    battery_coords = list(belief_set['batteries'].values())[0]
    if agent_coords[0] < battery_coords[0]:
        function_2()
    elif agent_coords[0] > battery_coords[0]:
        function_1()
    elif agent_coords[1] < battery_coords[1]:
        function_4()
    elif agent_coords[1] > battery_coords[1]:
        function_3()
    else:
        function_5()

def function_13():
    global belief_set
    agent = belief_set['agent']
    batteries = belief_set['batteries']
    for battery in batteries.values():
        while agent['coordinates'] != battery:
            if agent['coordinates'][0] < battery[0]:
                function_2()
            elif agent['coordinates'][0] > battery[0]:
                function_1()
            if agent['coordinates'][1] < battery[1]:
                function_4()
            elif agent['coordinates'][1] > battery[1]:
                function_3()
        function_5()

def function_14():
    global belief_set
    safety_counter = 0
    while belief_set['agent']['coordinates'] != belief_set['batteries'][1
        ] and safety_counter < 100:
        if belief_set['agent']['coordinates'][0] > belief_set['batteries'][1][0
            ]:
            function_1()
        elif belief_set['agent']['coordinates'][0] < belief_set['batteries'][1
            ][0]:
            function_2()
        elif belief_set['agent']['coordinates'][1] > belief_set['batteries'][1
            ][1]:
            function_3()
        elif belief_set['agent']['coordinates'][1] < belief_set['batteries'][1
            ][1]:
            function_4()
        safety_counter += 1
    if belief_set['agent']['coordinates'] == belief_set['batteries'][1]:
        function_5()

def function_15():
    global belief_set
    key_position = belief_set['keys'][1]['coordinates']
    agent_position = belief_set['agent']['coordinates']
    while agent_position != key_position:
        if key_position[0] < agent_position[0]:
            function_1()
        elif key_position[0] > agent_position[0]:
            function_2()
        if key_position[1] < agent_position[1]:
            function_3()
        elif key_position[1] > agent_position[1]:
            function_4()
    function_5()

def function_16():
    global belief_set
    key_coord = belief_set['keys'][1]['coordinates']
    while belief_set['agent']['coordinates'] != key_coord and belief_set[
        'agent']['energy'] > 10:
        if belief_set['agent']['coordinates'][0] < key_coord[0]:
            function_2()
        elif belief_set['agent']['coordinates'][0] > key_coord[0]:
            function_1()
        elif belief_set['agent']['coordinates'][1] < key_coord[1]:
            function_4()
        elif belief_set['agent']['coordinates'][1] > key_coord[1]:
            function_3()
        belief_set['agent']['coordinates'] = key_coord
    if belief_set['agent']['coordinates'] == key_coord and belief_set['agent'][
        'energy'] > 10:
        function_5()

def function_17():
    global belief_set
    agent_coordinates = belief_set['agent']['coordinates']
    map_grid = belief_set['map']['grid']
    unexplored_cells = [cell for cell in map_grid if cell['cell_type'] ==
        'walkable' and cell['cell_coordinates'] not in belief_set['agent'][
        'visited_cells']]
    if belief_set['agent']['energy'] > 10:
        if unexplored_cells:
            next_cell = unexplored_cells[0]
            if next_cell['cell_coordinates'][0] < agent_coordinates[0]:
                function_1()
            elif next_cell['cell_coordinates'][0] > agent_coordinates[0]:
                function_2()
            elif next_cell['cell_coordinates'][1] < agent_coordinates[1]:
                function_3()
            else:
                function_4()
        else:
            function_5()
    else:
        function_14()

def function_18():
    global belief_set
    energy_threshold = 30
    energy = belief_set['agent']['energy']
    if energy < energy_threshold:
        function_14()
    else:
        function_1() if belief_set['agent']['coordinates'][0
            ] > 0 else function_2()
        function_3() if belief_set['agent']['coordinates'][1
            ] > 0 else function_4()

def function_19():
    global belief_set
    agent_coords = belief_set['agent']['coordinates']
    if belief_set['agent']['energy'] > 50:
        if agent_coords[0] > 0 and belief_set['map']['grid'][agent_coords[0
            ] - 1][agent_coords[1]]['cell_type'] == 'walkable':
            function_1()
        elif agent_coords[0] < belief_set['map']['width'] - 1 and belief_set[
            'map']['grid'][agent_coords[0] + 1][agent_coords[1]]['cell_type'
            ] == 'walkable':
            function_2()
        elif agent_coords[1] > 0 and belief_set['map']['grid'][agent_coords[0]
            ][agent_coords[1] - 1]['cell_type'] == 'walkable':
            function_3()
        elif agent_coords[1] < belief_set['map']['height'] - 1 and belief_set[
            'map']['grid'][agent_coords[0]][agent_coords[1] + 1]['cell_type'
            ] == 'walkable':
            function_4()
    else:
        pass

def function_20():
    global belief_set
    while belief_set['agent']['energy'] > 30:
        function_4()
    if belief_set['agent']['energy'] <= 30:
        function_14()

def function_21():
    global belief_set
    while belief_set['agent']['coordinates'][1] < belief_set['map']['height'
        ] - 1 and belief_set['agent']['energy'] > 30:
        function_4()
    if belief_set['agent']['energy'] <= 30:
        function_14()

def function_22():
    global belief_set
    while belief_set['agent']['coordinates'][1] < belief_set['map']['height'
        ] - 1 and belief_set['agent']['energy'] >= 30:
        function_4()
    if belief_set['agent']['energy'] < 30:
        function_14()

def function_23():
    global belief_set
    if belief_set['agent']['energy'] > 20:
        function_4()

def function_25():
    global belief_set
    agent = belief_set['agent']
    if agent['energy'] > 50:
        function_1()
        function_2()
        function_3()
        function_4()
        function_5()
    else:
        pass

def function_26():
    global belief_set
    agent_coordinates = belief_set['agent']['coordinates']
    agent_energy = belief_set['agent']['energy']
    map_grid = belief_set['map']['grid']
    if agent_energy > 50:
        for cell in map_grid:
            if cell['cell_coordinates'] == [agent_coordinates[0], 
                agent_coordinates[1] + 1] and cell['cell_type'] == 'walkable':
                function_4()
                function_5()
                break

def function_27():
    global belief_set
    x, y = belief_set['agent']['coordinates']
    if belief_set['agent']['energy'] > 50:
        if belief_set['map']['grid'][y][x - 1]['cell_type'] == 'walkable':
            function_1()
        if belief_set['map']['grid'][y - 1][x]['cell_type'] == 'walkable':
            function_3()
        if belief_set['map']['grid'][y][x + 1]['cell_type'] == 'walkable':
            function_2()
        if belief_set['map']['grid'][y + 1][x]['cell_type'] == 'walkable':
            function_4()

def function_28():
    global belief_set
    agent_coordinates = belief_set['agent']['coordinates']
    key_coordinates = [item['coordinates'] for item in belief_set['keys'].
        values()]
    door_coordinates = [item['coordinates'] for item in belief_set['doors']
        .values()]
    if belief_set['agent']['has_key'] == False:
        if key_coordinates:
            target_key_coordinates = key_coordinates[0]
            if target_key_coordinates[0] < agent_coordinates[0]:
                function_1()
            elif target_key_coordinates[0] > agent_coordinates[0]:
                function_2()
            elif target_key_coordinates[1] < agent_coordinates[1]:
                function_3()
            elif target_key_coordinates[1] > agent_coordinates[1]:
                function_4()
            else:
                function_5()
    elif door_coordinates:
        target_door_coordinates = door_coordinates[0]
        if target_door_coordinates[0] < agent_coordinates[0]:
            function_1()
        elif target_door_coordinates[0] > agent_coordinates[0]:
            function_2()
        elif target_door_coordinates[1] < agent_coordinates[1]:
            function_3()
        elif target_door_coordinates[1] > agent_coordinates[1]:
            function_4()

def function_29():
    global belief_set
    agent_coordinates = belief_set['agent']['coordinates']
    key_coordinates = belief_set['keys'][2]['coordinates']
    battery_coordinates = belief_set['batteries'][2]
    if belief_set['agent']['energy'] < 30:
        if battery_coordinates[0] > agent_coordinates[0]:
            function_2()
        elif battery_coordinates[0] < agent_coordinates[0]:
            function_1()
        elif battery_coordinates[1] > agent_coordinates[1]:
            function_4()
        elif battery_coordinates[1] < agent_coordinates[1]:
            function_3()
        function_5()
    else:
        if key_coordinates[0] > agent_coordinates[0]:
            function_2()
        elif key_coordinates[0] < agent_coordinates[0]:
            function_1()
        elif key_coordinates[1] > agent_coordinates[1]:
            function_4()
        elif key_coordinates[1] < agent_coordinates[1]:
            function_3()
        function_5()

def function_30():
    global belief_set
    if belief_set['agent']['has_key']:
        for door in belief_set['doors'].values():
            if door['coordinates'] == belief_set['agent']['coordinates']:
                function_5()
    elif belief_set['agent']['energy'] < 50:
        function_29()
    else:
        function_24()

def function_31():
    global belief_set
    agent = belief_set['agent']
    keys = belief_set['keys']
    doors = belief_set['doors']
    batteries = belief_set['batteries']
    if agent['energy'] < 30:
        function_29()
    elif not agent['has_key'] and keys:
        function_29()
    else:
        nearest_door = min(doors, key=lambda x: abs(doors[x]['coordinates']
            [0] - agent['coordinates'][0]) + abs(doors[x]['coordinates'][1] -
            agent['coordinates'][1]))
        door_x, door_y = doors[nearest_door]['coordinates']
        agent_x, agent_y = agent['coordinates']
        if door_x > agent_x:
            function_2()
        elif door_x < agent_x:
            function_1()
        elif door_y > agent_y:
            function_4()
        else:
            function_3()

def function_32():
    global belief_set
    if belief_set['agent']['energy'] > 50:
        if belief_set['agent']['has_key']:
            for door in belief_set['doors'].values():
                if not door.get('unlocked', False):
                    if door['coordinates'][0] > belief_set['agent'][
                        'coordinates'][0]:
                        function_2()
                        break
                    elif door['coordinates'][0] < belief_set['agent'][
                        'coordinates'][0]:
                        function_1()
                        break
                    elif door['coordinates'][1] > belief_set['agent'][
                        'coordinates'][1]:
                        function_4()
                        break
                    elif door['coordinates'][1] < belief_set['agent'][
                        'coordinates'][1]:
                        function_3()
                        break
    else:
        function_29()
        function_5()

def function_33():
    global belief_set
    if belief_set['agent']['parcels_carried_ids'] and belief_set['agent'][
        'coordinates'] == [0, 0]:
        function_6()
    elif belief_set['agent']['coordinates'][0] > 0:
        function_1()
    elif belief_set['agent']['coordinates'][1] > 0:
        function_3()
    else:
        function_5()

def function_34():
    global belief_set
    if belief_set['agent']['coordinates'] == [0, 0] and len(belief_set[
        'agent']['parcels_carried_ids']) > 0:
        function_6()
    else:
        function_11()
    if belief_set['agent']['energy'] < 50 and belief_set['agent']['coordinates'
        ] != [3, 2]:
        function_2() if belief_set['agent']['coordinates'][0] < [3, 2][0
            ] else function_1()
        function_4() if belief_set['agent']['coordinates'][1] < [3, 2][1
            ] else function_3()
        function_5()

def function_35():
    global belief_set
    if belief_set['agent']['energy'] > 50:
        function_7()
        function_11()

