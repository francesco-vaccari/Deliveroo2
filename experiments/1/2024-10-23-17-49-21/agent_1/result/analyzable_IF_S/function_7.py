def function_7():
    global belief_set
    agent_coords = belief_set['agent']['coordinates']
    parcel_coords = belief_set['parcel'][1]['coordinates']
    if agent_coords[0] > parcel_coords[0]:
        function_1()
    elif agent_coords[0] < parcel_coords[0]:
        function_2()
    if agent_coords[1] > parcel_coords[1]:
        function_3()
    elif agent_coords[1] < parcel_coords[1]:
        function_4()
    else:
        function_5()
