def function_16():
    global belief_set
    agent = belief_set['agent'][1]
    parcels = belief_set['parcels']
    delivery_cell = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'delivery_cell'][0]
    parcel_coords = sorted(parcels.values(), key=lambda x: abs(x[
        'coordinates'][0] - agent['coordinates'][0]) + abs(x['coordinates']
        [1] - agent['coordinates'][1]))[0]['coordinates']
    while agent['coordinates'] != parcel_coords:
        if agent['coordinates'][0] < parcel_coords[0]:
            function_2()
        elif agent['coordinates'][0] > parcel_coords[0]:
            function_1()
        if agent['coordinates'][1] < parcel_coords[1]:
            function_4()
        elif agent['coordinates'][1] > parcel_coords[1]:
            function_3()
    function_5()
    while agent['coordinates'] != delivery_cell['coordinates']:
        if agent['coordinates'][0] < delivery_cell['coordinates'][0]:
            function_2()
        elif agent['coordinates'][0] > delivery_cell['coordinates'][0]:
            function_1()
        if agent['coordinates'][1] < delivery_cell['coordinates'][1]:
            function_4()
        elif agent['coordinates'][1] > delivery_cell['coordinates'][1]:
            function_3()
    function_6()
