def function_12():
    global belief_set
    while belief_set['agent'][1]['coordinates'] != [0, 0]:
        if belief_set['agent'][1]['coordinates'][0] > 0:
            function_1()
        elif belief_set['agent'][1]['coordinates'][1] > 0:
            function_3()
    function_5()
    if belief_set['agent'][1]['energy'] < 50:
        while belief_set['agent'][1]['coordinates'] != [2, 0]:
            if belief_set['agent'][1]['coordinates'][0] < 2:
                function_2()
            elif belief_set['agent'][1]['coordinates'][1] > 0:
                function_3()
        function_5()
    while belief_set['agent'][1]['coordinates'] != [2, 3]:
        if belief_set['agent'][1]['coordinates'][0] < 2:
            function_2()
        elif belief_set['agent'][1]['coordinates'][1] < 3:
            function_4()
    function_6()
