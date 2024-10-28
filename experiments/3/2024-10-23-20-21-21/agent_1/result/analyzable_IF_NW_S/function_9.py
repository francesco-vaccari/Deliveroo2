def function_9():
    global belief_set
    agent = belief_set['agent']
    parcels = belief_set['parcels']
    map = belief_set['map']['grid']
    parcel_coordinates = [parcel['coordinates'] for parcel in parcels.
        values() if parcel['carried_by_id'] is None]
    delivery_coordinates = [cell['cell_coordinates'] for cell in map if 
        cell['cell_type'] in ['delivery_cell', 'double_points_delivery_cell']]
    if not agent['parcels_carried_ids']:
        target_coordinates = parcel_coordinates[0]
    else:
        target_coordinates = delivery_coordinates[0]
    while agent['coordinates'] != target_coordinates:
        if agent['coordinates'][0] > target_coordinates[0]:
            function_1()
        elif agent['coordinates'][0] < target_coordinates[0]:
            function_2()
        elif agent['coordinates'][1] > target_coordinates[1]:
            function_3()
        elif agent['coordinates'][1] < target_coordinates[1]:
            function_4()
    if not agent['parcels_carried_ids']:
        function_5()
    else:
        function_6()
