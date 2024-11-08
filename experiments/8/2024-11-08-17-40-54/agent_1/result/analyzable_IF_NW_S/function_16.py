def function_16():
    global belief_set
    key_coord = belief_set['keys'][1]['coordinates']
    while belief_set['agent']['coordinates'] != key_coord and belief_set[
        'agent']['energy'] > 10:
        if belief_set['agent']['coordinates'][0] < key_coord[0]:
            function_2()
        elif belief_set['agent']['coordinates'][0] > key_coord[0]:
            function_1()
        elif belief_set['agent']['coordinates'][1] < key_coord[1]:
            function_4()
        elif belief_set['agent']['coordinates'][1] > key_coord[1]:
            function_3()
        belief_set['agent']['coordinates'] = key_coord
    if belief_set['agent']['coordinates'] == key_coord and belief_set['agent'][
        'energy'] > 10:
        function_5()
