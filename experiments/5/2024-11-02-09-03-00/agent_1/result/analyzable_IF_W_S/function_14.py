def function_14():
    global belief_set
    max_iterations = 100
    iteration_count = 0
    while iteration_count < max_iterations and belief_set['agent'][1][
        'coordinates'] != belief_set['parcels'][12]['coordinates']:
        if belief_set['agent'][1]['coordinates'][0] < belief_set['parcels'][12
            ]['coordinates'][0]:
            function_2()
        elif belief_set['agent'][1]['coordinates'][0] > belief_set['parcels'][
            12]['coordinates'][0]:
            function_1()
        elif belief_set['agent'][1]['coordinates'][1] < belief_set['parcels'][
            12]['coordinates'][1]:
            function_4()
        else:
            function_3()
        iteration_count += 1
    function_5()
    while iteration_count < max_iterations and belief_set['agent'][1][
        'coordinates'] != [1, 3]:
        if belief_set['agent'][1]['coordinates'][0] < 1:
            function_2()
        elif belief_set['agent'][1]['coordinates'][0] > 1:
            function_1()
        elif belief_set['agent'][1]['coordinates'][1] < 3:
            function_4()
        else:
            function_3()
        iteration_count += 1
    function_6()
