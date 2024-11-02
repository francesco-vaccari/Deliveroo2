def function_8():
    global belief_set
    parcel_carrying = False
    while not parcel_carrying:
        if belief_set['agent'][1]['coordinates'] == belief_set['map']['grid'][0
            ]['cell_coordinates']:
            function_5()
            parcel_carrying = True
        elif belief_set['agent'][1]['coordinates'][0] > belief_set['map'][
            'grid'][0]['cell_coordinates'][0]:
            function_1()
        elif belief_set['agent'][1]['coordinates'][0] < belief_set['map'][
            'grid'][0]['cell_coordinates'][0]:
            function_2()
        elif belief_set['agent'][1]['coordinates'][1] > belief_set['map'][
            'grid'][0]['cell_coordinates'][1]:
            function_3()
        else:
            function_4()
    while belief_set['agent'][1]['coordinates'] != belief_set['map']['grid'][7
        ]['cell_coordinates']:
        if belief_set['agent'][1]['coordinates'][0] > belief_set['map']['grid'
            ][7]['cell_coordinates'][0]:
            function_1()
        elif belief_set['agent'][1]['coordinates'][0] < belief_set['map'][
            'grid'][7]['cell_coordinates'][0]:
            function_2()
        elif belief_set['agent'][1]['coordinates'][1] > belief_set['map'][
            'grid'][7]['cell_coordinates'][1]:
            function_3()
        else:
            function_4()
    function_6()
    return
