def function_11():
    global belief_set
    agent = belief_set['agent']
    parcels = belief_set['parcel']
    delivery_cell = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] in ['double_delivery_cell', 'delivery_cell']][0]
    nearest_parcel = min(parcels.values(), key=lambda parcel: abs(parcel[
        'coordinates'][0] - agent['coordinates'][0]) + abs(parcel[
        'coordinates'][1] - agent['coordinates'][1]))
    if agent['coordinates'][0] < nearest_parcel['coordinates'][0]:
        function_2()
    elif agent['coordinates'][0] > nearest_parcel['coordinates'][0]:
        function_1()
    elif agent['coordinates'][1] < nearest_parcel['coordinates'][1]:
        function_4()
    elif agent['coordinates'][1] > nearest_parcel['coordinates'][1]:
        function_3()
    else:
        function_5()
    if agent['coordinates'] == nearest_parcel['coordinates']:
        if agent['coordinates'][0] < delivery_cell['cell_coordinates'][0]:
            function_2()
        elif agent['coordinates'][0] > delivery_cell['cell_coordinates'][0]:
            function_1()
        elif agent['coordinates'][1] < delivery_cell['cell_coordinates'][1]:
            function_4()
        elif agent['coordinates'][1] > delivery_cell['cell_coordinates'][1]:
            function_3()
        else:
            function_6()
