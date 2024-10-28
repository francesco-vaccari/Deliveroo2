def function_10():
    global belief_set
    while belief_set['agent'][1]['coordinates'] != belief_set['map']['grid'][7
        ]['cell_coordinates']:
        if belief_set['agent'][1]['coordinates'][0] < belief_set['map']['grid'
            ][7]['cell_coordinates'][0]:
            function_2()
        elif belief_set['agent'][1]['coordinates'][0] > belief_set['map'][
            'grid'][7]['cell_coordinates'][0]:
            function_1()
        elif belief_set['agent'][1]['coordinates'][1] < belief_set['map'][
            'grid'][7]['cell_coordinates'][1]:
            function_4()
        elif belief_set['agent'][1]['coordinates'][1] > belief_set['map'][
            'grid'][7]['cell_coordinates'][1]:
            function_3()
    function_6()
