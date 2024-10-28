def function_11():
    global belief_set
    agent_coordinates = belief_set['agent']['coordinates']
    parcel_coordinates = None
    for parcel in belief_set['parcels'].values():
        if parcel['carried_by_id'] is None:
            parcel_coordinates = parcel['coordinates']
            break
    if parcel_coordinates is None:
        return
    dx = parcel_coordinates[0] - agent_coordinates[0]
    dy = parcel_coordinates[1] - agent_coordinates[1]
    if dx > 0:
        for i in range(dx):
            function_2()
    elif dx < 0:
        for i in range(abs(dx)):
            function_1()
    if dy > 0:
        for i in range(dy):
            function_4()
    elif dy < 0:
        for i in range(abs(dy)):
            function_3()
    function_5()
