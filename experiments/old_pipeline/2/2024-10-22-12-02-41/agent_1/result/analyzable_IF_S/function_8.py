def function_8():
    global belief_set
    agent = belief_set['agent']
    keys = belief_set['keys']
    for key in keys.values():
        if key['coordinates'][0] > agent['coordinates'][0]:
            function_2()
        elif key['coordinates'][0] < agent['coordinates'][0]:
            function_1()
        elif key['coordinates'][1] > agent['coordinates'][1]:
            function_4()
        elif key['coordinates'][1] < agent['coordinates'][1]:
            function_3()
    function_5()
