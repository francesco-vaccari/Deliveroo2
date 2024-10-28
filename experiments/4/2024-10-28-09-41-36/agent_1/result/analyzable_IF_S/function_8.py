def function_8():
    global belief_set
    parcel_coordinates = belief_set['parcels'][1]['coordinates']
    agent_coordinates = belief_set['agent']['coordinates']
    if agent_coordinates[0] > parcel_coordinates[0]:
        function_1()
    elif agent_coordinates[0] < parcel_coordinates[0]:
        function_2()
    elif agent_coordinates[1] > parcel_coordinates[1]:
        function_3()
    elif agent_coordinates[1] < parcel_coordinates[1]:
        function_4()
    else:
        function_5()
