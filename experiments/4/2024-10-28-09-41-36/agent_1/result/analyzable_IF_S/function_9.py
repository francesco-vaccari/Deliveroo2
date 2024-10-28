def function_9():
    global belief_set
    parcel_coordinates = belief_set['parcels'][1]['coordinates']
    agent_coordinates = belief_set['agent']['coordinates']
    while agent_coordinates != parcel_coordinates:
        if parcel_coordinates[0] < agent_coordinates[0]:
            function_1()
        elif parcel_coordinates[0] > agent_coordinates[0]:
            function_2()
        elif parcel_coordinates[1] < agent_coordinates[1]:
            function_3()
        elif parcel_coordinates[1] > agent_coordinates[1]:
            function_4()
        agent_coordinates = belief_set['agent']['coordinates']
    function_5()
