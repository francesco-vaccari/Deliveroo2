def function_8():
    global belief_set
    agent = belief_set['agent']
    parcels = belief_set['parcels']
    for parcel_id, parcel in parcels.items():
        if not parcel['carried_by_id']:
            parcel_coords = parcel['coordinates']
            while agent['coordinates'] != parcel_coords:
                if agent['coordinates'][0] < parcel_coords[0]:
                    function_2()
                elif agent['coordinates'][0] > parcel_coords[0]:
                    function_1()
                elif agent['coordinates'][1] < parcel_coords[1]:
                    function_4()
                elif agent['coordinates'][1] > parcel_coords[1]:
                    function_3()
            function_5()
            break
    delivery_cell_coords = [cell['cell_coordinates'] for cell in belief_set
        ['map']['grid'] if cell['cell_type'] in ['delivery_cell',
        'double_points_delivery_cell']][0]
    while agent['coordinates'] != delivery_cell_coords:
        if agent['coordinates'][0] < delivery_cell_coords[0]:
            function_2()
        elif agent['coordinates'][0] > delivery_cell_coords[0]:
            function_1()
        elif agent['coordinates'][1] < delivery_cell_coords[1]:
            function_4()
        elif agent['coordinates'][1] > delivery_cell_coords[1]:
            function_3()
    function_6()
