def function_7():
    global belief_set
    spawn_location = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'parcels_spawn'][0]['cell_coordinates']
    delivery_location = [cell for cell in belief_set['map']['grid'] if cell
        ['cell_type'] == 'delivery_cell'][0]['cell_coordinates']
    while belief_set['agent']['coordinates'] != spawn_location:
        if belief_set['agent']['coordinates'][0] < spawn_location[0]:
            function_2()
        elif belief_set['agent']['coordinates'][0] > spawn_location[0]:
            function_1()
        elif belief_set['agent']['coordinates'][1] < spawn_location[1]:
            function_4()
        elif belief_set['agent']['coordinates'][1] > spawn_location[1]:
            function_3()
    function_5()
    while belief_set['agent']['coordinates'] != delivery_location:
        if belief_set['agent']['coordinates'][0] < delivery_location[0]:
            function_2()
        elif belief_set['agent']['coordinates'][0] > delivery_location[0]:
            function_1()
        elif belief_set['agent']['coordinates'][1] < delivery_location[1]:
            function_4()
        elif belief_set['agent']['coordinates'][1] > delivery_location[1]:
            function_3()
    function_6()
