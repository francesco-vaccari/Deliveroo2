def function_11():
    global belief_set
    while len(belief_set['parcels']) > 0:
        function_10()
        if belief_set['agent'][1]['energy'] < 30:
            function_2()
            function_2()
            function_5()
            function_1()
            function_1()
        function_6()
