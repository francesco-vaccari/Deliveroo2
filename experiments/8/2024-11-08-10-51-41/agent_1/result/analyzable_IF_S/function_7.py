def function_7():
    global belief_set
    agent_coords = belief_set['agent'][1]['coordinates']
    parcel_coords = belief_set['parcels'][1]['coordinates']
    while agent_coords[0] < parcel_coords[0]:
        function_2()
        agent_coords[0] += 1
    while agent_coords[1] < parcel_coords[1]:
        function_4()
        agent_coords[1] += 1
    function_5()
    while agent_coords[0] > 0:
        function_1()
        agent_coords[0] -= 1
    while agent_coords[1] > 0:
        function_3()
        agent_coords[1] -= 1
    function_6()
