def function_18():
    global belief_set
    agent = belief_set['agent'][1]
    key = belief_set['keys'][1]
    if agent['coordinates'] == key['coordinates']:
        function_5()
    elif agent['coordinates'][0] > key['coordinates'][0]:
        function_1()
    elif agent['coordinates'][0] < key['coordinates'][0]:
        function_2()
    elif agent['coordinates'][1] > key['coordinates'][1]:
        function_3()
    else:
        function_4()
