def function_8():
    global belief_set
    agent_position = belief_set['agent']['coordinates']
    parcel_position = belief_set['parcels'][1]['coordinates']
    while agent_position != parcel_position:
        if agent_position[0] < parcel_position[0]:
            function_2()
            agent_position[0] += 1
        elif agent_position[0] > parcel_position[0]:
            function_1()
            agent_position[0] -= 1
        if agent_position[1] < parcel_position[1]:
            function_4()
            agent_position[1] += 1
        elif agent_position[1] > parcel_position[1]:
            function_3()
            agent_position[1] -= 1
    function_5()
