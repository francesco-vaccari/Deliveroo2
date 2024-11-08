def function_7():
    global belief_set
    spawn_point = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'parcels_spawn'][0]['cell_coordinates']
    while belief_set['agent']['coordinates'] != spawn_point:
        if belief_set['agent']['coordinates'][0] < spawn_point[0]:
            function_2()
        elif belief_set['agent']['coordinates'][0] > spawn_point[0]:
            function_1()
        elif belief_set['agent']['coordinates'][1] < spawn_point[1]:
            function_4()
        elif belief_set['agent']['coordinates'][1] > spawn_point[1]:
            function_3()
    function_5()
