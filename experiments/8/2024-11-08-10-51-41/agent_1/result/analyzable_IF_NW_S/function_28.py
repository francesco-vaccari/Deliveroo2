def function_28():
    global belief_set
    agent = belief_set['agent'][1]
    parcel_coords = [parcel['coordinates'] for parcel in belief_set[
        'parcels'].values() if parcel['carried_by_id'] is None]
    delivery_coords = [cell['cell_coordinates'] for cell in belief_set[
        'map']['grid'] if cell['cell_type'] == 'delivery_cell'][0]
    while agent['coordinates'] != parcel_coords[0]:
        if agent['coordinates'][0] < parcel_coords[0][0]:
            function_2()
        elif agent['coordinates'][0] > parcel_coords[0][0]:
            function_1()
        elif agent['coordinates'][1] < parcel_coords[0][1]:
            function_4()
        elif agent['coordinates'][1] > parcel_coords[0][1]:
            function_3()
    function_5()
    while agent['coordinates'] != delivery_coords:
        if agent['coordinates'][0] < delivery_coords[0]:
            function_2()
        elif agent['coordinates'][0] > delivery_coords[0]:
            function_1()
        elif agent['coordinates'][1] < delivery_coords[1]:
            function_4()
        elif agent['coordinates'][1] > delivery_coords[1]:
            function_3()
    function_6()
    if agent['energy'] < 30:
        function_16()
