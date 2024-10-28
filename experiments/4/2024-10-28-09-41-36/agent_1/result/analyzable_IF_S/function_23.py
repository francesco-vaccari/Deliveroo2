def function_23():
    global belief_set
    if not belief_set['agent']['parcels_carried_ids']:
        parcel_coord = belief_set['parcels'][1]['coordinates']
        agent_coord = belief_set['agent']['coordinates']
        while agent_coord != parcel_coord:
            if parcel_coord[0] < agent_coord[0]:
                if agent_coord[0] > 0:
                    function_1()
            elif parcel_coord[0] > agent_coord[0]:
                if agent_coord[0] < belief_set['map']['height'] - 1:
                    function_2()
            if parcel_coord[1] < agent_coord[1]:
                if agent_coord[1] > 0:
                    function_3()
            elif parcel_coord[1] > agent_coord[1]:
                if agent_coord[1] < belief_set['map']['width'] - 1:
                    function_4()
            agent_coord = belief_set['agent']['coordinates']
        function_5()
    return
