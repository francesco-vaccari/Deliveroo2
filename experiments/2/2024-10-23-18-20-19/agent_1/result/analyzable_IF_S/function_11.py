def function_11():
    global belief_set
    parcel_coord = belief_set['parcel'][1]['coordinates']
    agent_coord = belief_set['agent']['coordinates']
    while agent_coord != parcel_coord:
        if agent_coord[0] < parcel_coord[0]:
            function_2()
        elif agent_coord[0] > parcel_coord[0]:
            function_1()
        if agent_coord[1] < parcel_coord[1]:
            function_4()
        elif agent_coord[1] > parcel_coord[1]:
            function_3()
        agent_coord = belief_set['agent']['coordinates']
    function_5()
