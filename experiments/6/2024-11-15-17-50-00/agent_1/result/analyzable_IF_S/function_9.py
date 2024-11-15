def function_9():
    global belief_set
    agent = belief_set['agent'][1]
    parcels = belief_set['parcels']
    batteries = belief_set['batteries']
    delivery_cell = next(cell for cell in belief_set['map']['grid'] if cell
        ['cell_type'] == 'delivery_cell')['cell_coordinates']
    if agent['energy'] < 30:
        battery_coordinates = batteries[1]['coordinates']
        if battery_coordinates[0] < agent['coordinates'][0]:
            function_1()
        elif battery_coordinates[0] > agent['coordinates'][0]:
            function_2()
        elif battery_coordinates[1] < agent['coordinates'][1]:
            function_3()
        else:
            function_4()
        function_5()
    for parcel_id, parcel in parcels.items():
        if parcel['carried_by_id'] == None:
            parcel_coordinates = parcel['coordinates']
            if parcel_coordinates[0] < agent['coordinates'][0]:
                function_1()
            elif parcel_coordinates[0] > agent['coordinates'][0]:
                function_2()
            elif parcel_coordinates[1] < agent['coordinates'][1]:
                function_3()
            else:
                function_4()
            function_5()
            break
    if agent['parcels_carried_ids']:
        if delivery_cell[0] < agent['coordinates'][0]:
            function_1()
        elif delivery_cell[0] > agent['coordinates'][0]:
            function_2()
        elif delivery_cell[1] < agent['coordinates'][1]:
            function_3()
        else:
            function_4()
        function_6()
