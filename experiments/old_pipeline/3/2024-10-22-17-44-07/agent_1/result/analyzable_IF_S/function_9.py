def function_9():
    global belief_set
    if belief_set['parcels'][1]['coordinates'][0] < belief_set['agent'][
        'coordinates'][0]:
        function_1()
    elif belief_set['parcels'][1]['coordinates'][0] > belief_set['agent'][
        'coordinates'][0]:
        function_2()
    elif belief_set['parcels'][1]['coordinates'][1] < belief_set['agent'][
        'coordinates'][1]:
        function_3()
    elif belief_set['parcels'][1]['coordinates'][1] > belief_set['agent'][
        'coordinates'][1]:
        function_4()
    else:
        function_5()
