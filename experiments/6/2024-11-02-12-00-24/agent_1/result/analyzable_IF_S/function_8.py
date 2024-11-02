def function_8():
    global belief_set
    while belief_set['agent']['coordinates'] != [2, 3]:
        if belief_set['agent']['coordinates'][0] < 2:
            function_2()
        elif belief_set['agent']['coordinates'][1] < 3:
            function_4()
        if belief_set['agent']['energy'] <= 40 and belief_set['agent'][
            'coordinates'] == [2, 0]:
            function_5()
    function_6()
