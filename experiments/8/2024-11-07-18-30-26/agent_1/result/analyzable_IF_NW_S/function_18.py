def function_18():
    global belief_set
    agent = belief_set['agent'][1]
    door = belief_set['doors'][1]
    while agent['coordinates'] != door['coordinates']:
        if agent['coordinates'][0] < door['coordinates'][0]:
            function_2()
        elif agent['coordinates'][0] > door['coordinates'][0]:
            function_1()
        elif agent['coordinates'][1] < door['coordinates'][1]:
            function_4()
        else:
            function_3()
    door['is_locked'] = False
    return
