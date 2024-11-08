def function_9():
    global belief_set
    agent = belief_set['agent'][1]
    parcels = belief_set['parcels']
    carried_parcels = [parcels[parcel_id] for parcel_id in agent[
        'parcels_carried_ids']]
    if not carried_parcels:
        return
    current_coordinates = agent['coordinates']
    target_coordinates = find_closest_walkable_cell(current_coordinates,
        belief_set['map']['grid'])
    while current_coordinates != target_coordinates:
        if current_coordinates[0] < target_coordinates[0]:
            function_2()
        elif current_coordinates[0] > target_coordinates[0]:
            function_1()
        if current_coordinates[1] < target_coordinates[1]:
            function_4()
        elif current_coordinates[1] > target_coordinates[1]:
            function_3()
        current_coordinates = agent['coordinates']
    function_6()
