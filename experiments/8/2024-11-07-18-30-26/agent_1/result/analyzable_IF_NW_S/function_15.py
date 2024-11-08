def function_15():
    global belief_set
    agent = belief_set['agent'][1]
    keys = belief_set['keys']
    for key_id, key in keys.items():
        if key['carried_by_id'] is None:
            while agent['coordinates'] != key['coordinates']:
                if agent['coordinates'][0] > key['coordinates'][0] and agent[
                    'coordinates'][0] > 0:
                    function_1()
                elif agent['coordinates'][0] < key['coordinates'][0] and agent[
                    'coordinates'][0] < belief_set['map']['width'] - 1:
                    function_2()
                elif agent['coordinates'][1] > key['coordinates'][1] and agent[
                    'coordinates'][1] > 0:
                    function_3()
                elif agent['coordinates'][1] < key['coordinates'][1] and agent[
                    'coordinates'][1] < belief_set['map']['height'] - 1:
                    function_4()
                else:
                    break
            function_5()
            break
