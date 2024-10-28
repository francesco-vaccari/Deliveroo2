def function_8():
    global belief_set
    agent = belief_set['agent'][1]
    parcels = belief_set['parcels']
    map = belief_set['map']['grid']
    for parcel in parcels.values():
        if parcel['carried_by_id'] == agent['id']:
            for cell in map:
                if cell['cell_type'] == 'delivery_cell':
                    while agent['coordinates'][0] < cell['cell_coordinates'][0
                        ]:
                        function_2()
                    while agent['coordinates'][0] > cell['cell_coordinates'][0
                        ]:
                        function_1()
                    while agent['coordinates'][1] < cell['cell_coordinates'][1
                        ]:
                        function_4()
                    while agent['coordinates'][1] > cell['cell_coordinates'][1
                        ]:
                        function_3()
                    function_6()
                    break
            break
        else:
            if agent['coordinates'][0] < parcel['coordinates'][0]:
                function_2()
            elif agent['coordinates'][0] > parcel['coordinates'][0]:
                function_1()
            elif agent['coordinates'][1] < parcel['coordinates'][1]:
                function_4()
            elif agent['coordinates'][1] > parcel['coordinates'][1]:
                function_3()
            function_5()
            break
