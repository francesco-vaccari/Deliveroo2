def function_8():
    global belief_set
    parcel_coordinates = belief_set['parcels'][1]['coordinates']
    agent_coordinates = belief_set['agent']['coordinates']
    while parcel_coordinates != agent_coordinates:
        if parcel_coordinates[0] < agent_coordinates[0]:
            function_1()
        elif parcel_coordinates[0] > agent_coordinates[0]:
            function_2()
        if parcel_coordinates[1] < agent_coordinates[1]:
            function_3()
        elif parcel_coordinates[1] > agent_coordinates[1]:
            function_4()
    function_5()
