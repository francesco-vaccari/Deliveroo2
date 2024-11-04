def function_11():
    global belief_set
    agent = belief_set['agent'][1]
    key = belief_set['keys'][0]
    door = belief_set['doors'][0]
    while agent['coordinates'] != key['coordinates']:
        if agent['coordinates'][0] < key['coordinates'][0]:
            function_2()
        elif agent['coordinates'][0] > key['coordinates'][0]:
            function_1()
        elif agent['coordinates'][1] < key['coordinates'][1]:
            function_4()
        elif agent['coordinates'][1] > key['coordinates'][1]:
            function_3()
    function_5()
    while agent['coordinates'] != door['coordinates']:
        if agent['coordinates'][0] < door['coordinates'][0]:
            function_2()
        elif agent['coordinates'][0] > door['coordinates'][0]:
            function_1()
        elif agent['coordinates'][1] < door['coordinates'][1]:
            function_4()
        elif agent['coordinates'][1] > door['coordinates'][1]:
            function_3()
    function_5()
