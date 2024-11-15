def function_13():
    global belief_set
    delivery_cell_coordinates = None
    for cell in belief_set['map']['grid']:
        if cell['cell_type'] == 'delivery_cell':
            delivery_cell_coordinates = cell['cell_coordinates']
    while belief_set['agent'][1]['coordinates'] != delivery_cell_coordinates:
        if belief_set['agent'][1]['coordinates'][0
            ] > delivery_cell_coordinates[0]:
            function_1()
        elif belief_set['agent'][1]['coordinates'][0
            ] < delivery_cell_coordinates[0]:
            function_2()
        elif belief_set['agent'][1]['coordinates'][1
            ] > delivery_cell_coordinates[1]:
            function_3()
        else:
            function_4()
    function_6()
