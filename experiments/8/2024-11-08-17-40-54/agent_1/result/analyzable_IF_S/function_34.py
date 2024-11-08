def function_34():
    global belief_set
    if belief_set['agent']['coordinates'] == [0, 0] and len(belief_set[
        'agent']['parcels_carried_ids']) > 0:
        function_6()
    else:
        function_11()
    if belief_set['agent']['energy'] < 50 and belief_set['agent']['coordinates'
        ] != [3, 2]:
        function_2() if belief_set['agent']['coordinates'][0] < [3, 2][0
            ] else function_1()
        function_4() if belief_set['agent']['coordinates'][1] < [3, 2][1
            ] else function_3()
        function_5()
