def function_33():
    global belief_set
    if belief_set['agent']['parcels_carried_ids'] and belief_set['agent'][
        'coordinates'] == [0, 0]:
        function_6()
    elif belief_set['agent']['coordinates'][0] > 0:
        function_1()
    elif belief_set['agent']['coordinates'][1] > 0:
        function_3()
    else:
        function_5()
