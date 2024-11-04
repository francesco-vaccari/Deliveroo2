def function_8():
    global belief_set
    while belief_set['agent']['coordinates'] != [2, 3]:
        if belief_set['agent']['coordinates'][0] < 2:
            function_2()
        elif belief_set['agent']['coordinates'][1] < 3:
            function_4()
        if belief_set['agent']['energy'] <= 40 and belief_set['agent'][
            'coordinates'] == [2, 0]:
            function_5()
    function_6()

def function_9():
    global belief_set
    agent = belief_set['agent']
    parcel_location = belief_set['parcels'][3]['coordinates']
    delivery_location = [cell for cell in belief_set['map']['grid'] if cell
        ['cell_type'] == 'delivery_cell'][0]['cell_coordinates']
    battery_location = belief_set['battery'][1]
    if agent['energy'] < 50:
        if agent['coordinates'][0] > battery_location[0]:
            function_1()
        elif agent['coordinates'][0] < battery_location[0]:
            function_2()
        elif agent['coordinates'][1] > battery_location[1]:
            function_3()
        else:
            function_4()
    elif len(agent['parcels_carried_ids']) == 0:
        if agent['coordinates'][0] > parcel_location[0]:
            function_1()
        elif agent['coordinates'][0] < parcel_location[0]:
            function_2()
        elif agent['coordinates'][1] > parcel_location[1]:
            function_3()
        else:
            function_4()
        function_5()
    else:
        if agent['coordinates'][0] > delivery_location[0]:
            function_1()
        elif agent['coordinates'][0] < delivery_location[0]:
            function_2()
        elif agent['coordinates'][1] > delivery_location[1]:
            function_3()
        else:
            function_4()
        function_6()

def function_10():
    global belief_set
    current_position = belief_set['agent']['coordinates']
    parcels_position = belief_set['map']['grid'][0]['cell_coordinates']
    batteries_position = belief_set['map']['grid'][8]['cell_coordinates']
    energy = belief_set['agent']['energy']
    if energy < 30:
        if current_position[0] > batteries_position[0]:
            function_1()
        elif current_position[0] < batteries_position[0]:
            function_2()
        elif current_position[1] > batteries_position[1]:
            function_3()
        elif current_position[1] < batteries_position[1]:
            function_4()
    else:
        if current_position[0] > parcels_position[0]:
            function_1()
        elif current_position[0] < parcels_position[0]:
            function_2()
        elif current_position[1] > parcels_position[1]:
            function_3()
        elif current_position[1] < parcels_position[1]:
            function_4()
        if current_position == parcels_position:
            function_5()

def function_11():
    global belief_set
    parcels = belief_set['parcels']
    agent_location = belief_set['agent']['coordinates']
    delivery_location = [cell for cell in belief_set['map']['grid'] if cell
        ['cell_type'] == 'delivery_cell'][0]['cell_coordinates']
    closest_parcel = min(parcels.values(), key=lambda x: abs(x[
        'coordinates'][0] - agent_location[0]) + abs(x['coordinates'][1] -
        agent_location[1]))
    parcel_location = closest_parcel['coordinates']
    while agent_location != parcel_location:
        if agent_location[0] < parcel_location[0]:
            function_2()
        elif agent_location[0] > parcel_location[0]:
            function_1()
        if agent_location[1] < parcel_location[1]:
            function_4()
        elif agent_location[1] > parcel_location[1]:
            function_3()
    function_5()
    while agent_location != delivery_location:
        if agent_location[0] < delivery_location[0]:
            function_2()
        elif agent_location[0] > delivery_location[0]:
            function_1()
        if agent_location[1] < delivery_location[1]:
            function_4()
        elif agent_location[1] > delivery_location[1]:
            function_3()
    function_6()

def function_12():
    global belief_set
    parcels = belief_set['parcels']
    agent = belief_set['agent']
    delivery_cell_coords = [cell['cell_coordinates'] for cell in belief_set
        ['map']['grid'] if cell['cell_type'] == 'delivery_cell'][0]
    while True:
        if len(parcels) == 0 or agent['energy'] <= 0:
            break
        else:
            closest_parcel_coords = min(parcels.values(), key=lambda x: abs
                (x['coordinates'][0] - agent['coordinates'][0]) + abs(x[
                'coordinates'][1] - agent['coordinates'][1]))['coordinates']
            while agent['coordinates'] != closest_parcel_coords:
                if agent['coordinates'][0] < closest_parcel_coords[0]:
                    function_2()
                elif agent['coordinates'][0] > closest_parcel_coords[0]:
                    function_1()
                elif agent['coordinates'][1] < closest_parcel_coords[1]:
                    function_4()
                else:
                    function_3()
                agent['coordinates'] = closest_parcel_coords
            function_5()
            while agent['coordinates'] != delivery_cell_coords:
                if agent['coordinates'][0] < delivery_cell_coords[0]:
                    function_2()
                elif agent['coordinates'][0] > delivery_cell_coords[0]:
                    function_1()
                elif agent['coordinates'][1] < delivery_cell_coords[1]:
                    function_4()
                else:
                    function_3()
                agent['coordinates'] = delivery_cell_coords
            function_6()
            parcels = {k: v for k, v in parcels.items() if v[
                'carried_by_id'] is None}
    return

def function_13():
    global belief_set
    agent = belief_set['agent']
    parcels = belief_set['parcels']
    battery_position = belief_set['battery'][1]
    delivery_position = [2, 3]
    while agent['coordinates'] != battery_position and agent['energy'] < 20:
        if agent['coordinates'][0] < battery_position[0]:
            function_2()
        elif agent['coordinates'][0] > battery_position[0]:
            function_1()
        elif agent['coordinates'][1] < battery_position[1]:
            function_4()
        elif agent['coordinates'][1] > battery_position[1]:
            function_3()
    function_5()
    for parcel in parcels.values():
        if parcel['carried_by_id'] is None:
            target_position = parcel['coordinates']
            while agent['coordinates'] != target_position:
                if agent['coordinates'][0] < target_position[0]:
                    function_2()
                elif agent['coordinates'][0] > target_position[0]:
                    function_1()
                elif agent['coordinates'][1] < target_position[1]:
                    function_4()
                elif agent['coordinates'][1] > target_position[1]:
                    function_3()
            function_5()
            break
    while agent['coordinates'] != delivery_position:
        if agent['coordinates'][0] < delivery_position[0]:
            function_2()
        elif agent['coordinates'][0] > delivery_position[0]:
            function_1()
        elif agent['coordinates'][1] < delivery_position[1]:
            function_4()
        elif agent['coordinates'][1] > delivery_position[1]:
            function_3()
    function_6()

def function_15():
    global belief_set
    function_14()
    function_7()
    function_5()
    function_14()
    function_6()
