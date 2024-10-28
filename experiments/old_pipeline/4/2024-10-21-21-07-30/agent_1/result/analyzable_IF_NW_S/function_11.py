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
