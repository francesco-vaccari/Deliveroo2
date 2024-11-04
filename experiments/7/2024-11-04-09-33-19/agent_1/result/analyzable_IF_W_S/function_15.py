def function_15():
    global belief_set
    while belief_set['agent']['coordinates'] != [0, 0]:
        if belief_set['agent']['coordinates'][0] > 0:
            function_1()
        else:
            function_3()
    function_5()
    while belief_set['agent']['coordinates'] != [1, 3]:
        if belief_set['agent']['coordinates'][0] < 1:
            function_2()
        else:
            function_4()
    function_6()
