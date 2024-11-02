def function_13():
    global belief_set
    agent = belief_set['agent']
    parcels = belief_set['parcels']
    battery_position = belief_set['battery'][1]
    delivery_position = [2, 3]
    while agent['coordinates'] != battery_position and agent['energy'] < 20:
        if agent['coordinates'][0] < battery_position[0]:
            function_2()
        elif agent['coordinates'][0] > battery_position[0]:
            function_1()
        elif agent['coordinates'][1] < battery_position[1]:
            function_4()
        elif agent['coordinates'][1] > battery_position[1]:
            function_3()
    function_5()
    for parcel in parcels.values():
        if parcel['carried_by_id'] is None:
            target_position = parcel['coordinates']
            while agent['coordinates'] != target_position:
                if agent['coordinates'][0] < target_position[0]:
                    function_2()
                elif agent['coordinates'][0] > target_position[0]:
                    function_1()
                elif agent['coordinates'][1] < target_position[1]:
                    function_4()
                elif agent['coordinates'][1] > target_position[1]:
                    function_3()
            function_5()
            break
    while agent['coordinates'] != delivery_position:
        if agent['coordinates'][0] < delivery_position[0]:
            function_2()
        elif agent['coordinates'][0] > delivery_position[0]:
            function_1()
        elif agent['coordinates'][1] < delivery_position[1]:
            function_4()
        elif agent['coordinates'][1] > delivery_position[1]:
            function_3()
    function_6()
