def function_7():
    global belief_set
    spawn_location = [cell['cell_coordinates'] for cell in belief_set['map'
        ]['grid'] if cell['cell_type'] == 'parcels_spawn'][0]
    while belief_set['agent'][1]['coordinates'] != spawn_location:
        if belief_set['agent'][1]['coordinates'][0] > spawn_location[0]:
            function_1()
        elif belief_set['agent'][1]['coordinates'][0] < spawn_location[0]:
            function_2()
        if belief_set['agent'][1]['coordinates'][1] > spawn_location[1]:
            function_3()
        elif belief_set['agent'][1]['coordinates'][1] < spawn_location[1]:
            function_4()
    function_5()
