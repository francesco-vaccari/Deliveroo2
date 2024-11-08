def function_22():
    global belief_set
    agent = belief_set['agent'][1]
    if agent['energy'] < 30:
        for cell in belief_set['map']['grid']:
            if cell['cell_type'] == 'batteries_spawn':
                agent['coordinates'] = cell['cell_coordinates']
                break
    else:
        parcel_picked = False
        for parcel in belief_set['parcels'].values():
            if parcel['coordinates'] == agent['coordinates']:
                function_5()
                parcel_picked = True
                break
        if not parcel_picked:
            function_7()
        for cell in belief_set['map']['grid']:
            if cell['cell_type'] == 'delivery_cell':
                while agent['coordinates'] != cell['cell_coordinates']:
                    if agent['coordinates'][0] < cell['cell_coordinates'][0]:
                        function_2()
                    elif agent['coordinates'][0] > cell['cell_coordinates'][0]:
                        function_1()
                    elif agent['coordinates'][1] < cell['cell_coordinates'][1]:
                        function_4()
                    elif agent['coordinates'][1] > cell['cell_coordinates'][1]:
                        function_3()
                function_6()
                break
