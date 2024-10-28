def function_10():
    global belief_set
    delivery_cell = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'delivery_cell'][0]['cell_coordinates']
    while belief_set['agent']['coordinates'] != delivery_cell:
        if belief_set['agent']['coordinates'][0] > delivery_cell[0]:
            function_1()
        elif belief_set['agent']['coordinates'][0] < delivery_cell[0]:
            function_2()
        elif belief_set['agent']['coordinates'][1] > delivery_cell[1]:
            function_3()
        elif belief_set['agent']['coordinates'][1] < delivery_cell[1]:
            function_4()
    function_6()
