def function_11():
    global belief_set
    agent = belief_set['agent'][1]
    parcel = belief_set['parcel'][1]
    while agent['coordinates'] != [1, 3]:
        if agent['coordinates'][0] < 1:
            function_2()
        elif agent['coordinates'][0] > 1:
            function_1()
        elif agent['coordinates'][1] < 3:
            function_4()
        elif agent['coordinates'][1] > 3:
            function_3()
    function_6()
