def function_24():
    global belief_set
    agent = belief_set['agent'][1]
    parcels = belief_set['parcels']
    nearest_parcel = min(parcels.values(), key=lambda p: abs(p[
        'coordinates'][0] - agent['coordinates'][0]) + abs(p['coordinates']
        [1] - agent['coordinates'][1]))
    while agent['coordinates'] != nearest_parcel['coordinates']:
        if agent['coordinates'][0] < nearest_parcel['coordinates'][0]:
            function_2()
        elif agent['coordinates'][0] > nearest_parcel['coordinates'][0]:
            function_1()
        elif agent['coordinates'][1] < nearest_parcel['coordinates'][1]:
            function_4()
        else:
            function_3()
    function_5()
    delivery_cell = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'delivery_cell'][0]
    while agent['coordinates'] != delivery_cell['cell_coordinates']:
        if agent['coordinates'][0] < delivery_cell['cell_coordinates'][0]:
            function_2()
        elif agent['coordinates'][0] > delivery_cell['cell_coordinates'][0]:
            function_1()
        elif agent['coordinates'][1] < delivery_cell['cell_coordinates'][1]:
            function_4()
        else:
            function_3()
    function_6()
