def function_10():
    global belief_set
    agent = belief_set['agent']
    keys = belief_set['keys']
    batteries = belief_set['batteries']
    if agent['energy'] < 20:
        for battery in batteries:
            while agent['coordinates'] != battery['coordinates']:
                if agent['coordinates'][0] < battery['coordinates'][0]:
                    function_2()
                elif agent['coordinates'][0] > battery['coordinates'][0]:
                    function_1()
                if agent['coordinates'][1] < battery['coordinates'][1]:
                    function_4()
                elif agent['coordinates'][1] > battery['coordinates'][1]:
                    function_3()
        function_5()
    for key in keys:
        while agent['coordinates'] != key['coordinates']:
            if agent['coordinates'][0] < key['coordinates'][0]:
                function_2()
            elif agent['coordinates'][0] > key['coordinates'][0]:
                function_1()
            if agent['coordinates'][1] < key['coordinates'][1]:
                function_4()
            elif agent['coordinates'][1] > key['coordinates'][1]:
                function_3()
    function_5()
