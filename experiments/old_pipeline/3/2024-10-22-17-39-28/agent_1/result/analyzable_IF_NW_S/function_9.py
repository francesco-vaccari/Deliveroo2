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
