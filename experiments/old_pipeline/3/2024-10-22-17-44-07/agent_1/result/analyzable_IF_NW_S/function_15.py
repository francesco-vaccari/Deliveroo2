def function_15():
    global belief_set
    agent_coordinates = belief_set['agent']['coordinates']
    parcel_coordinates = [parcel['coordinates'] for parcel in belief_set[
        'parcels'].values() if parcel['carried_by_id'] is None]
    key_coordinates = [key['coordinates'] for key in belief_set['keys'].
        values() if key['carried_by_id'] is None]
    nearest_coordinates = min(parcel_coordinates + key_coordinates, key=lambda
        c: abs(c[0] - agent_coordinates[0]) + abs(c[1] - agent_coordinates[1]))
    if agent_coordinates != nearest_coordinates:
        if nearest_coordinates[0] > agent_coordinates[0]:
            function_2()
        elif nearest_coordinates[0] < agent_coordinates[0]:
            function_1()
        elif nearest_coordinates[1] > agent_coordinates[1]:
            function_4()
        else:
            function_3()
    else:
        function_5()
        delivery_cell_coordinates = [cell['cell_coordinates'] for cell in
            belief_set['map']['grid'] if 'delivery' in cell['cell_type']]
        nearest_delivery_cell_coordinates = min(delivery_cell_coordinates,
            key=lambda c: abs(c[0] - agent_coordinates[0]) + abs(c[1] -
            agent_coordinates[1]))
        if nearest_delivery_cell_coordinates[0] > agent_coordinates[0]:
            function_2()
        elif nearest_delivery_cell_coordinates[0] < agent_coordinates[0]:
            function_1()
        elif nearest_delivery_cell_coordinates[1] > agent_coordinates[1]:
            function_4()
        else:
            function_3()
