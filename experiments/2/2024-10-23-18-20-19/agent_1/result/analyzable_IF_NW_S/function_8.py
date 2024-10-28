def function_8():
    global belief_set
    agent = belief_set['agent']
    key = belief_set['key']
    while agent['coordinates'] != key[1]['coordinates']:
        if agent['coordinates'][0] < key[1]['coordinates'][0]:
            function_2()
        elif agent['coordinates'][0] > key[1]['coordinates'][0]:
            function_1()
        elif agent['coordinates'][1] < key[1]['coordinates'][1]:
            function_4()
        elif agent['coordinates'][1] > key[1]['coordinates'][1]:
            function_3()
    function_5()
