def function_9():
    global belief_set
    agent_coordinates = belief_set['agent']['coordinates']
    nearest_parcel_coordinates = belief_set['parcels'][1]['coordinates']
    while agent_coordinates != nearest_parcel_coordinates:
        if agent_coordinates[0] < nearest_parcel_coordinates[0]:
            function_2()
            if belief_set['agent']['coordinates'] == agent_coordinates:
                break
        elif agent_coordinates[0] > nearest_parcel_coordinates[0]:
            function_1()
            if belief_set['agent']['coordinates'] == agent_coordinates:
                break
        elif agent_coordinates[1] < nearest_parcel_coordinates[1]:
            function_4()
            if belief_set['agent']['coordinates'] == agent_coordinates:
                break
        elif agent_coordinates[1] > nearest_parcel_coordinates[1]:
            function_3()
            if belief_set['agent']['coordinates'] == agent_coordinates:
                break
        agent_coordinates = belief_set['agent']['coordinates']
    function_5()
