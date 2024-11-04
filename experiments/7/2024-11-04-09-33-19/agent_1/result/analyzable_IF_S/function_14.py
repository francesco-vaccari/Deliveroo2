def function_14():
    global belief_set
    battery_coords = belief_set['batteries'][0]['coordinates']
    while belief_set['agent']['coordinates'] != battery_coords:
        if belief_set['agent']['coordinates'][0] < battery_coords[0]:
            function_2()
        elif belief_set['agent']['coordinates'][0] > battery_coords[0]:
            function_1()
        elif belief_set['agent']['coordinates'][1] < battery_coords[1]:
            function_4()
        elif belief_set['agent']['coordinates'][1] > battery_coords[1]:
            function_3()
    function_5()
