def function_9():
    global belief_set
    agent_coordinates = belief_set['agent']['coordinates']
    parcels = belief_set['parcels']
    closest_parcel_id = min(parcels, key=lambda x: abs(parcels[x][
        'coordinates'][0] - agent_coordinates[0]) + abs(parcels[x][
        'coordinates'][1] - agent_coordinates[1]))
    closest_parcel = parcels[closest_parcel_id]
    while agent_coordinates != closest_parcel['coordinates']:
        if agent_coordinates[0] < closest_parcel['coordinates'][0]:
            function_2()
            agent_coordinates[0] += 1
        elif agent_coordinates[0] > closest_parcel['coordinates'][0]:
            function_1()
            agent_coordinates[0] -= 1
        if agent_coordinates[1] < closest_parcel['coordinates'][1]:
            function_4()
            agent_coordinates[1] += 1
        elif agent_coordinates[1] > closest_parcel['coordinates'][1]:
            function_3()
            agent_coordinates[1] -= 1
    function_5()
