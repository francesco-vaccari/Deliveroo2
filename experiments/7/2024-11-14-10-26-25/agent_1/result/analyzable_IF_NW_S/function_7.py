def function_7():
    global belief_set
    agent_coordinates = belief_set['agent']['coordinates']
    nearest_parcel_coordinates = min(belief_set['parcels'], key=lambda p: 
        abs(p['coordinates'][0] - agent_coordinates[0]) + abs(p[
        'coordinates'][1] - agent_coordinates[1]))['coordinates']
    while agent_coordinates[0] != nearest_parcel_coordinates[0]:
        if agent_coordinates[0] < nearest_parcel_coordinates[0]:
            function_2()
        else:
            function_1()
    while agent_coordinates[1] != nearest_parcel_coordinates[1]:
        if agent_coordinates[1] < nearest_parcel_coordinates[1]:
            function_4()
        else:
            function_3()
    function_5()
