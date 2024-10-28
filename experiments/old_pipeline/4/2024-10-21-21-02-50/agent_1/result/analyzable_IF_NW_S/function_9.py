def function_9():
    global belief_set
    while belief_set['agents'][1]['coordinates'] != belief_set['parcels'][1][
        'coordinates']:
        if belief_set['agents'][1]['coordinates'][0] < belief_set['parcels'][1
            ]['coordinates'][0]:
            function_2()
        elif belief_set['agents'][1]['coordinates'][0] > belief_set['parcels'][
            1]['coordinates'][0]:
            function_1()
        if belief_set['agents'][1]['coordinates'][1] < belief_set['parcels'][1
            ]['coordinates'][1]:
            function_4()
        elif belief_set['agents'][1]['coordinates'][1] > belief_set['parcels'][
            1]['coordinates'][1]:
            function_3()
    function_5()
