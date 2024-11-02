def function_9():
    global belief_set
    agent = belief_set['agent']
    parcel_location = belief_set['parcels'][3]['coordinates']
    delivery_location = [cell for cell in belief_set['map']['grid'] if cell
        ['cell_type'] == 'delivery_cell'][0]['cell_coordinates']
    battery_location = belief_set['battery'][1]
    if agent['energy'] < 50:
        if agent['coordinates'][0] > battery_location[0]:
            function_1()
        elif agent['coordinates'][0] < battery_location[0]:
            function_2()
        elif agent['coordinates'][1] > battery_location[1]:
            function_3()
        else:
            function_4()
    elif len(agent['parcels_carried_ids']) == 0:
        if agent['coordinates'][0] > parcel_location[0]:
            function_1()
        elif agent['coordinates'][0] < parcel_location[0]:
            function_2()
        elif agent['coordinates'][1] > parcel_location[1]:
            function_3()
        else:
            function_4()
        function_5()
    else:
        if agent['coordinates'][0] > delivery_location[0]:
            function_1()
        elif agent['coordinates'][0] < delivery_location[0]:
            function_2()
        elif agent['coordinates'][1] > delivery_location[1]:
            function_3()
        else:
            function_4()
        function_6()
