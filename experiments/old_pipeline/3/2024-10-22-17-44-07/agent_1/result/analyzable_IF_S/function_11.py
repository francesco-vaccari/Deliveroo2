def function_11():
    global belief_set
    function_3()
    if belief_set['map']['grid'][belief_set['agent']['coordinates'][0]][
        belief_set['agent']['coordinates'][1]]['cell_type'
        ] == 'delivery_cell' or belief_set['map']['grid'][belief_set[
        'agent']['coordinates'][0]][belief_set['agent']['coordinates'][1]][
        'cell_type'] == 'double_delivery_cell':
        function_6()
