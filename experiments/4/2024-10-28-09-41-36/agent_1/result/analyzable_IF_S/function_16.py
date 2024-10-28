def function_16():
    global belief_set
    agent_coordinates = belief_set['agent']['coordinates']
    if belief_set['agent']['parcels_carried_ids']:
        delivery_cells = [cell for cell in belief_set['map']['grid'] if 
            'delivery' in cell['cell_type']]
        delivery_cells.sort(key=lambda cell: abs(cell['cell_coordinates'][0
            ] - agent_coordinates[0]) + abs(cell['cell_coordinates'][1] -
            agent_coordinates[1]))
        target_coordinates = delivery_cells[0]['cell_coordinates']
        function_6(
            ) if agent_coordinates == target_coordinates else function_1(
            ) if agent_coordinates[0] > target_coordinates[0] else function_2(
            ) if agent_coordinates[0] < target_coordinates[0] else function_3(
            ) if agent_coordinates[1] > target_coordinates[1] else function_4()
    else:
        parcels = [parcel for parcel in belief_set['parcels'].values()]
        parcels.sort(key=lambda parcel: abs(parcel['coordinates'][0] -
            agent_coordinates[0]) + abs(parcel['coordinates'][1] -
            agent_coordinates[1]))
        target_coordinates = parcels[0]['coordinates']
        function_5(
            ) if agent_coordinates == target_coordinates else function_1(
            ) if agent_coordinates[0] > target_coordinates[0] else function_2(
            ) if agent_coordinates[0] < target_coordinates[0] else function_3(
            ) if agent_coordinates[1] > target_coordinates[1] else function_4()
