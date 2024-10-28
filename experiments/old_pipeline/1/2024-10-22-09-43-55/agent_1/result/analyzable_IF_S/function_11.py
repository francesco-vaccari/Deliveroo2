def function_11():
    global belief_set
    while belief_set['agent']['coordinates'] != [1, 3]:
        if belief_set['agent']['coordinates'][1] < 3:
            function_4()
        elif belief_set['agent']['coordinates'][0] > 1:
            function_1()
    function_6()
