def function_9():
    global belief_set
    agent = belief_set['agent']
    parcels = belief_set['parcels']
    map_info = belief_set['map']['grid']
    parcel_coordinate = None
    delivery_coordinate = None
    for parcel in parcels.values():
        if parcel['carried_by_id'] == None:
            parcel_coordinate = parcel['coordinates']
            break
    for cell in map_info:
        if 'delivery' in cell['cell_type']:
            delivery_coordinate = cell['cell_coordinates']
            break
    while agent['coordinates'] != parcel_coordinate:
        if agent['coordinates'][0] < parcel_coordinate[0]:
            function_2()
        elif agent['coordinates'][0] > parcel_coordinate[0]:
            function_1()
        elif agent['coordinates'][1] < parcel_coordinate[1]:
            function_4()
        elif agent['coordinates'][1] > parcel_coordinate[1]:
            function_3()
    function_5()
    while agent['coordinates'] != delivery_coordinate:
        if agent['coordinates'][0] < delivery_coordinate[0]:
            function_2()
        elif agent['coordinates'][0] > delivery_coordinate[0]:
            function_1()
        elif agent['coordinates'][1] < delivery_coordinate[1]:
            function_4()
        elif agent['coordinates'][1] > delivery_coordinate[1]:
            function_3()
    function_6()
