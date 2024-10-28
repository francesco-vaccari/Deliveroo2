def function_7():
    global belief_set
    agent_pos = belief_set['agent']['coordinates']
    parcel_pos = belief_set['parcels'][1]['coordinates']
    if agent_pos[0] < parcel_pos[0]:
        function_2()
    elif agent_pos[0] > parcel_pos[0]:
        function_1()
    elif agent_pos[1] < parcel_pos[1]:
        function_4()
    elif agent_pos[1] > parcel_pos[1]:
        function_3()
    else:
        function_5()
