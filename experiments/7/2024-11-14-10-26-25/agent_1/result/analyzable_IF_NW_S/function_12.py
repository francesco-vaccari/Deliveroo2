def function_12():
    global belief_set
    agent = belief_set['agent']
    batteries = belief_set['batteries']
    keys = belief_set['keys']
    if agent['energy'] < 50:
        if batteries[0]['coordinates'][0] > agent['coordinates'][0]:
            function_2()
        elif batteries[0]['coordinates'][0] < agent['coordinates'][0]:
            function_1()
        elif batteries[0]['coordinates'][1] > agent['coordinates'][1]:
            function_4()
        elif batteries[0]['coordinates'][1] < agent['coordinates'][1]:
            function_3()
        function_5()
    else:
        if keys[0]['coordinates'][0] > agent['coordinates'][0]:
            function_2()
        elif keys[0]['coordinates'][0] < agent['coordinates'][0]:
            function_1()
        elif keys[0]['coordinates'][1] > agent['coordinates'][1]:
            function_4()
        elif keys[0]['coordinates'][1] < agent['coordinates'][1]:
            function_3()
        function_5()
