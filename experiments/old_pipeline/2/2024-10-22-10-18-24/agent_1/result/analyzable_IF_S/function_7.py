def function_7():
    global belief_set
    while belief_set['agent']['coordinates'][0] > belief_set['parcel'][1][
        'coordinates'][0]:
        function_1()
    while belief_set['agent']['coordinates'][0] < belief_set['parcel'][1][
        'coordinates'][0]:
        function_2()
    while belief_set['agent']['coordinates'][1] > belief_set['parcel'][1][
        'coordinates'][1]:
        function_3()
    while belief_set['agent']['coordinates'][1] < belief_set['parcel'][1][
        'coordinates'][1]:
        function_4()
    function_5()
    delivery_cell_coordinates = None
    for cell in belief_set['map']['grid']:
        if cell['cell_type'] == 'delivery_cell':
            delivery_cell_coordinates = cell['cell_coordinates']
            break
    while belief_set['agent']['coordinates'][0] > delivery_cell_coordinates[0]:
        function_1()
    while belief_set['agent']['coordinates'][0] < delivery_cell_coordinates[0]:
        function_2()
    while belief_set['agent']['coordinates'][1] > delivery_cell_coordinates[1]:
        function_3()
    while belief_set['agent']['coordinates'][1] < delivery_cell_coordinates[1]:
        function_4()
    function_6()
