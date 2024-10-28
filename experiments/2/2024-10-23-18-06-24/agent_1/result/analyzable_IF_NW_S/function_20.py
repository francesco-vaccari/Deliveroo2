def function_20():
    global belief_set
    spawn_cell_coordinates = [cell['cell_coordinates'] for cell in
        belief_set['map']['grid'] if cell['cell_type'] == 'parcels_spawn'][0]
    delivery_cell_coordinates = [cell['cell_coordinates'] for cell in
        belief_set['map']['grid'] if cell['cell_type'] == 'delivery_cell'][0]
    while belief_set['agent']['coordinates'] != spawn_cell_coordinates:
        if belief_set['agent']['coordinates'][0] < spawn_cell_coordinates[0]:
            function_2()
        elif belief_set['agent']['coordinates'][0] > spawn_cell_coordinates[0]:
            function_1()
        elif belief_set['agent']['coordinates'][1] < spawn_cell_coordinates[1]:
            function_4()
        else:
            function_3()
    function_5()
    while belief_set['agent']['coordinates'] != delivery_cell_coordinates:
        if belief_set['agent']['coordinates'][0] < delivery_cell_coordinates[0
            ]:
            function_2()
        elif belief_set['agent']['coordinates'][0] > delivery_cell_coordinates[
            0]:
            function_1()
        elif belief_set['agent']['coordinates'][1] < delivery_cell_coordinates[
            1]:
            function_4()
        else:
            function_3()
    function_17()
