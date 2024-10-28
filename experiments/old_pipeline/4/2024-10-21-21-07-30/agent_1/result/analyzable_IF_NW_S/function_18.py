def function_18():
    global belief_set
    if belief_set['agent']['parcels_carried_ids']:
        if belief_set['agent']['coordinates'] == [3, 0]:
            function_6()
        elif belief_set['agent']['coordinates'][0] < 3:
            function_2()
        elif belief_set['agent']['coordinates'][1] > 0:
            function_3()
