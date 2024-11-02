def function_13():
    global belief_set
    agent = belief_set['agent'][1]
    if agent['energy'] < 50:
        function_2()
        function_5()
    elif agent['coordinates'][0] < belief_set['map']['width'] - 1:
        function_2()
    elif agent['coordinates'][1] < belief_set['map']['height'] - 1:
        function_4()
    else:
        function_1()
        function_3()
