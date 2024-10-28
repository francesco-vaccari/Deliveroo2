def function_12():
    global belief_set
    agent = belief_set['agent']
    parcels = belief_set['parcels']
    for parcel_id, parcel_info in parcels.items():
        if parcel_info['coordinates'] == agent['coordinates']:
            function_5()
        elif parcel_info['coordinates'][0] < agent['coordinates'][0]:
            function_1()
        elif parcel_info['coordinates'][0] > agent['coordinates'][0]:
            function_2()
        elif parcel_info['coordinates'][1] < agent['coordinates'][1]:
            function_3()
        elif parcel_info['coordinates'][1] > agent['coordinates'][1]:
            function_4()
    map_grid = belief_set['map']['grid']
    for cell in map_grid:
        if cell['cell_type'] == 'delivery_cell' or cell['cell_type'
            ] == 'double_delivery_cell':
            if cell['cell_coordinates'] == agent['coordinates']:
                function_6()
            elif cell['cell_coordinates'][0] < agent['coordinates'][0]:
                function_1()
            elif cell['cell_coordinates'][0] > agent['coordinates'][0]:
                function_2()
            elif cell['cell_coordinates'][1] < agent['coordinates'][1]:
                function_3()
            elif cell['cell_coordinates'][1] > agent['coordinates'][1]:
                function_4()
