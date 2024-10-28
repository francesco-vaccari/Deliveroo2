def function_25():
    global belief_set
    agent = belief_set['agent']
    parcels = belief_set['parcels']
    map = belief_set['map']['grid']
    keys = belief_set['keys']
    doors = belief_set['doors']
    for cell in map:
        if cell['cell_type'] == 'double_points_delivery_cell':
            target = cell['cell_coordinates']
    if 'carried_by_id' in parcels[1] and parcels[1]['carried_by_id'] == agent[
        'id']:
        if agent['coordinates'][0] < target[0]:
            function_2()
        elif agent['coordinates'][0] > target[0]:
            function_1()
        elif agent['coordinates'][1] < target[1]:
            function_4()
        else:
            function_3()
    else:
        if not agent['has_key']:
            for key in keys.values():
                if key['carried_by_id'] is None:
                    if agent['coordinates'][0] < key['coordinates'][0]:
                        function_2()
                    elif agent['coordinates'][0] > key['coordinates'][0]:
                        function_1()
                    elif agent['coordinates'][1] < key['coordinates'][1]:
                        function_4()
                    else:
                        function_3()
        else:
            for door in doors.values():
                if agent['coordinates'][0] < door['coordinates'][0]:
                    function_2()
                elif agent['coordinates'][0] > door['coordinates'][0]:
                    function_1()
                elif agent['coordinates'][1] < door['coordinates'][1]:
                    function_4()
                else:
                    function_3()
        function_5()
    function_6()
