def function_8():
    global belief_set
    agent = belief_set['agent'][1]
    parcels = belief_set['parcels']
    batteries = belief_set['batteries']
    map = belief_set['map']['grid']
    delivery_cell = next((cell for cell in map if cell['cell_type'] ==
        'delivery_cell'), None)
    battery_cell = next((cell for cell in map if cell['cell_type'] ==
        'batteries_spawn'), None)
    parcel_cell = next((cell for cell in map if cell['cell_type'] ==
        'parcels_spawn'), None)
    if agent['energy'] < 30 and battery_cell:
        if agent['coordinates'][0] < battery_cell['cell_coordinates'][0]:
            function_2()
        elif agent['coordinates'][0] > battery_cell['cell_coordinates'][0]:
            function_1()
        elif agent['coordinates'][1] < battery_cell['cell_coordinates'][1]:
            function_4()
        elif agent['coordinates'][1] > battery_cell['cell_coordinates'][1]:
            function_3()
        function_5()
    elif agent['parcels_carried_ids'] and delivery_cell:
        if agent['coordinates'][0] < delivery_cell['cell_coordinates'][0]:
            function_2()
        elif agent['coordinates'][0] > delivery_cell['cell_coordinates'][0]:
            function_1()
        elif agent['coordinates'][1] < delivery_cell['cell_coordinates'][1]:
            function_4()
        elif agent['coordinates'][1] > delivery_cell['cell_coordinates'][1]:
            function_3()
        function_6()
    elif parcels and parcel_cell:
        if agent['coordinates'][0] < parcel_cell['cell_coordinates'][0]:
            function_2()
        elif agent['coordinates'][0] > parcel_cell['cell_coordinates'][0]:
            function_1()
        elif agent['coordinates'][1] < parcel_cell['cell_coordinates'][1]:
            function_4()
        elif agent['coordinates'][1] > parcel_cell['cell_coordinates'][1]:
            function_3()
        function_5()
