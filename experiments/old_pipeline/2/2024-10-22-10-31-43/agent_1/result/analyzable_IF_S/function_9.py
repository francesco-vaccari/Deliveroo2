def function_9():
    global belief_set
    parcel_location = belief_set['parcel'][1]['coordinates']
    agent_location = belief_set['agent'][1]['coordinates']
    while agent_location != parcel_location:
        if agent_location[0] < parcel_location[0]:
            function_2()
        elif agent_location[0] > parcel_location[0]:
            function_1()
        elif agent_location[1] < parcel_location[1]:
            function_4()
        elif agent_location[1] > parcel_location[1]:
            function_3()
        agent_location = belief_set['agent'][1]['coordinates']
    function_5()
