def function_31():
    global belief_set
    if belief_set['agent'][1]['energy'] < 50:
        function_16()
    elif belief_set['agent'][1]['coordinates'] in [i['cell_coordinates'] for
        i in belief_set['map']['grid'] if i['cell_type'] == 'delivery_cell']:
        function_6()
    else:
        function_13()
