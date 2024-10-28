def function_12():
    global belief_set
    for cell in belief_set['map']['grid']:
        if cell['cell_type'] == 'walkable' and 'id' in [parcel for parcel in
            belief_set['parcels'].values() if parcel['coordinates'] == cell
            ['cell_coordinates']]:
            while belief_set['agent']['coordinates'] != cell['cell_coordinates'
                ]:
                if belief_set['agent']['coordinates'][0] < cell[
                    'cell_coordinates'][0]:
                    function_2()
                elif belief_set['agent']['coordinates'][0] > cell[
                    'cell_coordinates'][0]:
                    function_1()
                elif belief_set['agent']['coordinates'][1] < cell[
                    'cell_coordinates'][1]:
                    function_4()
                else:
                    function_3()
            function_5()
            break
