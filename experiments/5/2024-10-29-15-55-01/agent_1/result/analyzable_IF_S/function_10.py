def function_10():
    global belief_set
    agent = belief_set['agent'][1]
    parcels = belief_set['parcels']
    map_info = belief_set['map']
    width = map_info['width']
    height = map_info['height']
    delivery_cell = [cell for cell in map_info['grid'] if cell['cell_type'] ==
        'delivery_cell'][0]['cell_coordinates']
    for parcel_id, parcel_info in parcels.items():
        if parcel_info['carried_by_id'] is None:
            parcel_coordinates = parcel_info['coordinates']
            while agent['coordinates'] != parcel_coordinates:
                if agent['coordinates'][0] > parcel_coordinates[0] and agent[
                    'coordinates'][0] > 0:
                    function_1()
                elif agent['coordinates'][0] < parcel_coordinates[0] and agent[
                    'coordinates'][0] < width - 1:
                    function_2()
                if agent['coordinates'][1] > parcel_coordinates[1] and agent[
                    'coordinates'][1] > 0:
                    function_3()
                elif agent['coordinates'][1] < parcel_coordinates[1] and agent[
                    'coordinates'][1] < height - 1:
                    function_4()
            function_5()
            break
    while agent['coordinates'] != delivery_cell:
        if agent['coordinates'][0] > delivery_cell[0] and agent['coordinates'][
            0] > 0:
            function_1()
        elif agent['coordinates'][0] < delivery_cell[0] and agent['coordinates'
            ][0] < width - 1:
            function_2()
        if agent['coordinates'][1] > delivery_cell[1] and agent['coordinates'][
            1] > 0:
            function_3()
        elif agent['coordinates'][1] < delivery_cell[1] and agent['coordinates'
            ][1] < height - 1:
            function_4()
    function_6()
