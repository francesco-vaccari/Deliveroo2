def function_24():
    global belief_set
    agent_coords = belief_set['agent'][1]['coordinates']
    parcel_coords = [parcel['coordinates'] for parcel in belief_set[
        'parcels'].values() if parcel['carried_by_id'] is None]
    if agent_coords in parcel_coords:
        function_5()
    else:
        min_distance = float('inf')
        for coords in parcel_coords:
            distance = abs(agent_coords[0] - coords[0]) + abs(agent_coords[
                1] - coords[1])
            if distance < min_distance:
                min_distance = distance
                nearest_parcel = coords
        if agent_coords[0] > nearest_parcel[0]:
            function_1()
        elif agent_coords[0] < nearest_parcel[0]:
            function_2()
        elif agent_coords[1] > nearest_parcel[1]:
            function_3()
        elif agent_coords[1] < nearest_parcel[1]:
            function_4()
