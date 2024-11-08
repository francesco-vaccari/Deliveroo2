def function_16():
    global belief_set
    agent = belief_set['agent'][1]
    key = belief_set['keys'][1]
    while agent['coordinates'] != key['coordinates']:
        if agent['coordinates'][0] < key['coordinates'][0] and agent[
            'coordinates'][0] < belief_set['map']['width'] - 1:
            function_2()
            agent['coordinates'][0] += 1
        elif agent['coordinates'][0] > key['coordinates'][0] and agent[
            'coordinates'][0] > 0:
            function_1()
            agent['coordinates'][0] -= 1
        if agent['coordinates'][1] < key['coordinates'][1] and agent[
            'coordinates'][1] < belief_set['map']['height'] - 1:
            function_4()
            agent['coordinates'][1] += 1
        elif agent['coordinates'][1] > key['coordinates'][1] and agent[
            'coordinates'][1] > 0:
            function_3()
            agent['coordinates'][1] -= 1
    function_5()
