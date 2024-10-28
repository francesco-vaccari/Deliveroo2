def function_8():
    global belief_set
    parcel_id = belief_set['agent'][1]['parcels_carried_ids']
    agent_coordinates = belief_set['agent'][1]['coordinates']
    if parcel_id and parcel_id[0] not in belief_set['parcels'].keys():
        function_5()
    delivery_cells = [cell['cell_coordinates'] for cell in belief_set['map'
        ]['grid'] if 'delivery' in cell['cell_type']]
    nearest_delivery_cell = min(delivery_cells, key=lambda x: abs(x[0] -
        agent_coordinates[0]) + abs(x[1] - agent_coordinates[1]))
    if nearest_delivery_cell[0] < agent_coordinates[0]:
        function_1()
    elif nearest_delivery_cell[0] > agent_coordinates[0]:
        function_2()
    elif nearest_delivery_cell[1] < agent_coordinates[1]:
        function_3()
    elif nearest_delivery_cell[1] > agent_coordinates[1]:
        function_4()
    if not parcel_id or parcel_id[0] not in belief_set['parcels'].keys():
        function_5()
