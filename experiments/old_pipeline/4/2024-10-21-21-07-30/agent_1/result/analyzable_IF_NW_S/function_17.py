def function_17():
    global belief_set
    while belief_set['agent']['coordinates'] != [3, 0]:
        if belief_set['agent']['coordinates'][0] < 3:
            function_2()
        elif belief_set['agent']['coordinates'][1] > 0:
            function_3()
    if belief_set['agent']['parcels_carried_ids']:
        function_6()
