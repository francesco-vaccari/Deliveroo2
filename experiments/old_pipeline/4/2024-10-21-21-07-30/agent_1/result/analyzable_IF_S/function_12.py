def function_12():
    global belief_set
    agent = belief_set['agent']
    map = belief_set['map']
    parcel = belief_set['parcel'][1]
    key = belief_set['key'][1]
    door_1 = belief_set['door'][1]
    door_2 = belief_set['door'][2]
    if agent['coordinates'] == parcel['coordinates']:
        function_5()
    elif agent['coordinates'] == key['coordinates']:
        function_5()
    elif (agent['coordinates'] == door_1['coordinates'] or agent[
        'coordinates'] == door_2['coordinates']) and agent['has_key']:
        function_5()
    else:
        for cell in map['grid']:
            if cell['cell_type'] == 'delivery_cell' and cell['cell_coordinates'
                ][0] > agent['coordinates'][0]:
                function_2()
            elif cell['cell_type'] == 'delivery_cell' and cell[
                'cell_coordinates'][0] < agent['coordinates'][0]:
                function_1()
            elif cell['cell_type'] == 'delivery_cell' and cell[
                'cell_coordinates'][1] > agent['coordinates'][1]:
                function_4()
            elif cell['cell_type'] == 'delivery_cell' and cell[
                'cell_coordinates'][1] < agent['coordinates'][1]:
                function_3()
