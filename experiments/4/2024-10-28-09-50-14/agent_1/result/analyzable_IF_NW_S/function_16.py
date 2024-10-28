def function_16():
    global belief_set
    agent = belief_set['agents'][1]
    key_locations = [key['coordinates'] for key in belief_set['keys'].
        values() if key['carried_by_id'] is None]
    if not agent['has_key'] and key_locations:
        nearest_key_location = min(key_locations, key=lambda c: abs(c[0] -
            agent['coordinates'][0]) + abs(c[1] - agent['coordinates'][1]))
        while agent['coordinates'] != nearest_key_location:
            if agent['coordinates'][0] < nearest_key_location[0]:
                function_2()
            elif agent['coordinates'][0] > nearest_key_location[0]:
                function_1()
            if agent['coordinates'][1] < nearest_key_location[1]:
                function_4()
            elif agent['coordinates'][1] > nearest_key_location[1]:
                function_3()
        function_5()
