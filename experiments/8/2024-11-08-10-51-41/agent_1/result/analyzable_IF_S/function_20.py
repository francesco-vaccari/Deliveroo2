def function_20():
    global belief_set
    agent = belief_set['agent'][1]
    door = belief_set['doors'][1]
    if agent['has_key']:
        if agent['coordinates'][0] < door['coordinates'][0]:
            function_2()
        elif agent['coordinates'][0] > door['coordinates'][0]:
            function_1()
        if agent['coordinates'][1] < door['coordinates'][1]:
            function_4()
        elif agent['coordinates'][1] > door['coordinates'][1]:
            function_3()
