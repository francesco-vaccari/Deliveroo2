def function_11():
    global belief_set
    for parcel in belief_set['parcels']:
        if parcel['carried_by_id'] is None:
            target_coordinates = parcel['coordinates']
            break
    x_diff = belief_set['agent']['coordinates'][0] - target_coordinates[0]
    y_diff = belief_set['agent']['coordinates'][1] - target_coordinates[1]
    if x_diff > 0:
        for _ in range(x_diff):
            function_1()
    elif x_diff < 0:
        for _ in range(-x_diff):
            function_2()
    if y_diff > 0:
        for _ in range(y_diff):
            function_3()
    elif y_diff < 0:
        for _ in range(-y_diff):
            function_4()
    function_5()
