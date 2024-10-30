def function_8():
    global belief_set
    agent = belief_set['agent'][1]
    parcels = belief_set['parcels']
    map_grid = belief_set['map']['grid']
    delivery_cell = [cell for cell in map_grid if cell['cell_type'] ==
        'delivery_cell'][0]['cell_coordinates']
    parcel_ids = [parcel['id'] for parcel in parcels.values() if parcel[
        'carried_by_id'] is None]
    if parcel_ids:
        parcel_location = parcels[parcel_ids[0]]['coordinates']
        while agent['coordinates'] != parcel_location:
            if agent['coordinates'][0] < parcel_location[0]:
                function_2()
            elif agent['coordinates'][0] > parcel_location[0]:
                function_1()
            elif agent['coordinates'][1] < parcel_location[1]:
                function_4()
            elif agent['coordinates'][1] > parcel_location[1]:
                function_3()
        function_5()
    while agent['coordinates'] != delivery_cell:
        if agent['coordinates'][0] < delivery_cell[0]:
            function_2()
        elif agent['coordinates'][0] > delivery_cell[0]:
            function_1()
        elif agent['coordinates'][1] < delivery_cell[1]:
            function_4()
        elif agent['coordinates'][1] > delivery_cell[1]:
            function_3()
    function_6()
