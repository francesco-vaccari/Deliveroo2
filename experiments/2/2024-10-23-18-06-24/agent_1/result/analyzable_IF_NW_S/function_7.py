def function_7():
    global belief_set
    agent_coordinates = belief_set['agent']['coordinates']
    parcel_coordinates = belief_set['parcel'][1]['coordinates']
    if agent_coordinates[0] > parcel_coordinates[0]:
        function_1()
    elif agent_coordinates[0] < parcel_coordinates[0]:
        function_2()
    elif agent_coordinates[1] > parcel_coordinates[1]:
        function_3()
    elif agent_coordinates[1] < parcel_coordinates[1]:
        function_4()
