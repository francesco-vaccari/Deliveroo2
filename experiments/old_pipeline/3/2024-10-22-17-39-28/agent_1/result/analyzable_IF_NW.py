def function_7():
    global belief_set
    agent_coords = belief_set['agent'][1]['coordinates']
    parcel_coords = belief_set['parcels'][1]['coordinates']
    while agent_coords[0] != parcel_coords[0]:
        if agent_coords[0] > parcel_coords[0]:
            function_1()
            agent_coords[0] -= 1
        else:
            function_2()
            agent_coords[0] += 1
    while agent_coords[1] != parcel_coords[1]:
        if agent_coords[1] > parcel_coords[1]:
            function_3()
            agent_coords[1] -= 1
        else:
            function_4()
            agent_coords[1] += 1
    function_5()
    for cell in belief_set['map']['grid']:
        if 'delivery' in cell['cell_type']:
            delivery_coords = cell['cell_coordinates']
            break
    while agent_coords[0] != delivery_coords[0]:
        if agent_coords[0] > delivery_coords[0]:
            function_1()
            agent_coords[0] -= 1
        else:
            function_2()
            agent_coords[0] += 1
    while agent_coords[1] != delivery_coords[1]:
        if agent_coords[1] > delivery_coords[1]:
            function_3()
            agent_coords[1] -= 1
        else:
            function_4()
            agent_coords[1] += 1
    function_6()

def function_9():
    global belief_set
    agent_coords = belief_set['agent'][1]['coordinates']
    parcel_coords = belief_set['parcels'][1]['coordinates']
    if agent_coords == parcel_coords:
        function_5()
    delivery_cell_coords = [cell['cell_coordinates'] for cell in belief_set
        ['map']['grid'] if 'delivery_cell' in cell['cell_type']]
    nearest_delivery_cell_coords = min(delivery_cell_coords, key=lambda x: 
        abs(x[0] - agent_coords[0]) + abs(x[1] - agent_coords[1]))
    if nearest_delivery_cell_coords[0] < agent_coords[0]:
        function_1()
    elif nearest_delivery_cell_coords[0] > agent_coords[0]:
        function_2()
    elif nearest_delivery_cell_coords[1] < agent_coords[1]:
        function_3()
    elif nearest_delivery_cell_coords[1] > agent_coords[1]:
        function_4()
    door_coords = [door['coordinates'] for door in belief_set['doors'].values()
        ]
    if agent_coords in door_coords and belief_set['agent'][1]['has_key']:
        function_7()
    if belief_set['parcels'][1]['carried_by_id'] != 1:
        function_5()

def function_10():
    global belief_set
    if belief_set['agent'][1]['parcels_carried_ids']:
        function_2()
        if not belief_set['agent'][1]['parcels_carried_ids']:
            function_5()
    else:
        function_5()
        function_2()
    if belief_set['doors'][1]['coordinates'] == belief_set['agent'][1][
        'coordinates'] and belief_set['agent'][1]['has_key']:
        function_8()
    else:
        function_2()

def function_11():
    global belief_set
    agent = belief_set['agent'][1]
    parcels = belief_set['parcels']
    for parcel in parcels.values():
        if parcel['carried_by_id'] == agent['id']:
            function_6()
            function_5()
            break
    if not agent['parcels_carried_ids']:
        function_5()
    if belief_set['map']['grid'][agent['coordinates'][0]][agent[
        'coordinates'][1]]['cell_type'] == 'delivery_cell':
        function_6()
    else:
        if agent['coordinates'][0] > 0:
            function_1()
        elif agent['coordinates'][0] < belief_set['map']['height'] - 1:
            function_2()
        if agent['coordinates'][1] > 0:
            function_3()
        elif agent['coordinates'][1] < belief_set['map']['width'] - 1:
            function_4()

