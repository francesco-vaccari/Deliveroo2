def function_7():
    global belief_set
    agent = belief_set['agents'][1]
    key = belief_set['keys'][1]
    if agent['coordinates'] == key['coordinates']:
        function_5()
    elif agent['coordinates'][0] > key['coordinates'][0]:
        function_1()
    elif agent['coordinates'][0] < key['coordinates'][0]:
        function_2()
    elif agent['coordinates'][1] > key['coordinates'][1]:
        function_3()
    elif agent['coordinates'][1] < key['coordinates'][1]:
        function_4()
    else:
        pass
