def function_10():
    global belief_set
    parcel_coordinates = belief_set['parcel'][1]['coordinates']
    agent_coordinates = belief_set['agent']['coordinates']
    while agent_coordinates != parcel_coordinates:
        if agent_coordinates[0] < parcel_coordinates[0]:
            function_2()
        elif agent_coordinates[0] > parcel_coordinates[0]:
            function_1()
        elif agent_coordinates[1] < parcel_coordinates[1]:
            function_4()
        elif agent_coordinates[1] > parcel_coordinates[1]:
            function_3()
        agent_coordinates = belief_set['agent']['coordinates']
    function_5()
