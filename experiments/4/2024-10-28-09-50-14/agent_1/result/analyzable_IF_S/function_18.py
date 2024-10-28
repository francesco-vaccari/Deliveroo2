def function_18():
    global belief_set
    agent = belief_set['agents'][1]
    key = belief_set['keys'][1]
    previous_coordinates = agent['coordinates'].copy()
    while agent['coordinates'] != key['coordinates'] or not agent['has_key']:
        if agent['coordinates'][0] < key['coordinates'][0]:
            function_2()
        elif agent['coordinates'][0] > key['coordinates'][0]:
            function_1()
        elif agent['coordinates'][1] < key['coordinates'][1]:
            function_4()
        elif agent['coordinates'][1] > key['coordinates'][1]:
            function_3()
        if agent['coordinates'] == key['coordinates'] and not agent['has_key']:
            function_5()
        if agent['coordinates'] == previous_coordinates:
            break
        previous_coordinates = agent['coordinates'].copy()
