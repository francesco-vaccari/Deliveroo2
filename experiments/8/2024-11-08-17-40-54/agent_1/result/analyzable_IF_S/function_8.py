def function_8():
    global belief_set
    current_cell = belief_set['agent']['coordinates']
    if {'cell_coordinates': [current_cell[0] - 1, current_cell[1]],
        'cell_type': 'walkable'} in belief_set['map']['grid']:
        function_1()
    elif {'cell_coordinates': [current_cell[0] + 1, current_cell[1]],
        'cell_type': 'walkable'} in belief_set['map']['grid']:
        function_2()
    elif {'cell_coordinates': [current_cell[0], current_cell[1] - 1],
        'cell_type': 'walkable'} in belief_set['map']['grid']:
        function_3()
    elif {'cell_coordinates': [current_cell[0], current_cell[1] + 1],
        'cell_type': 'walkable'} in belief_set['map']['grid']:
        function_4()
    for parcel in belief_set['parcels'].values():
        if parcel['coordinates'] == belief_set['agent']['coordinates']:
            function_5()
