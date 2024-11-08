def function_22():
    global belief_set
    agent = belief_set['agent'][1]
    if agent['has_key'] and agent['energy'] > 10:
        door = belief_set['doors'][1]
        if agent['coordinates'][0] > door['coordinates'][0]:
            function_1()
        elif agent['coordinates'][0] < door['coordinates'][0]:
            function_2()
        elif agent['coordinates'][1] > door['coordinates'][1]:
            function_3()
        elif agent['coordinates'][1] < door['coordinates'][1]:
            function_4()
    elif agent['energy'] <= 10:
        function_16()
