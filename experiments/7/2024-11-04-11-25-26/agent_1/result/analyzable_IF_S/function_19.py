def function_19():
    global belief_set
    MAX_ITERATIONS = 1000
    iteration = 0
    delivery_cell = [c['cell_coordinates'] for c in belief_set['map'][
        'grid'] if c['cell_type'] == 'delivery_cell'][0]
    while belief_set['agent'][1]['coordinates'
        ] != delivery_cell and iteration < MAX_ITERATIONS:
        x_diff = belief_set['agent'][1]['coordinates'][0] - delivery_cell[0]
        y_diff = belief_set['agent'][1]['coordinates'][1] - delivery_cell[1]
        if x_diff > 0:
            function_1()
        elif x_diff < 0:
            function_2()
        if y_diff > 0:
            function_3()
        elif y_diff < 0:
            function_4()
        iteration += 1
    function_6()
