def function_32():
    global belief_set
    if belief_set['agent']['energy'] > 50:
        if belief_set['agent']['has_key']:
            for door in belief_set['doors'].values():
                if not door.get('unlocked', False):
                    if door['coordinates'][0] > belief_set['agent'][
                        'coordinates'][0]:
                        function_2()
                        break
                    elif door['coordinates'][0] < belief_set['agent'][
                        'coordinates'][0]:
                        function_1()
                        break
                    elif door['coordinates'][1] > belief_set['agent'][
                        'coordinates'][1]:
                        function_4()
                        break
                    elif door['coordinates'][1] < belief_set['agent'][
                        'coordinates'][1]:
                        function_3()
                        break
    else:
        function_29()
        function_5()
