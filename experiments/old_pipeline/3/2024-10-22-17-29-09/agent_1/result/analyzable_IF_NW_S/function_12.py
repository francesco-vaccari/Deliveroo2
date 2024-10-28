def function_12():
    global belief_set
    coordinates = belief_set['agent']['coordinates']
    parcels = belief_set['parcel']
    if len(parcels) > 0:
        parcel = parcels[list(parcels.keys())[0]]
        if parcel['carried_by_id'] == 1:
            if coordinates[0] < 2:
                function_2()
            elif coordinates[0] > 2:
                function_1()
            elif coordinates[1] < 1:
                function_4()
            elif coordinates[1] > 1:
                function_3()
            else:
                function_6()
    elif coordinates[0] < 2:
        function_2()
    elif coordinates[0] > 2:
        function_1()
    elif coordinates[1] < 1:
        function_4()
    elif coordinates[1] > 1:
        function_3()
    else:
        function_5()
