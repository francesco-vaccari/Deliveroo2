def function_9():
    global belief_set
    width = belief_set['map']['width']
    height = belief_set['map']['height']
    grid = belief_set['map']['grid']
    agent = belief_set['agent'][1]
    parcels = belief_set['parcels']
    non_walkable_cells = [cell for cell in grid if cell['cell_type'] ==
        'non_walkable']
    for i in range(width * height):
        for parcel in parcels.values():
            if parcel['carried_by_id'] is None and parcel['coordinates'
                ] not in [cell['cell_coordinates'] for cell in
                non_walkable_cells]:
                while agent['coordinates'][0] > parcel['coordinates'][0]:
                    function_1()
                while agent['coordinates'][0] < parcel['coordinates'][0]:
                    function_2()
                while agent['coordinates'][1] > parcel['coordinates'][1]:
                    function_3()
                while agent['coordinates'][1] < parcel['coordinates'][1]:
                    function_4()
                function_5()
                break
        else:
            continue
        break
    delivery_cell_coordinates = [cell['cell_coordinates'] for cell in grid if
        cell['cell_type'] == 'delivery_cell'][0]
    for i in range(width * height):
        while agent['coordinates'][0] > delivery_cell_coordinates[0]:
            function_1()
        while agent['coordinates'][0] < delivery_cell_coordinates[0]:
            function_2()
        while agent['coordinates'][1] > delivery_cell_coordinates[1]:
            function_3()
        while agent['coordinates'][1] < delivery_cell_coordinates[1]:
            function_4()
        function_6()
        break
