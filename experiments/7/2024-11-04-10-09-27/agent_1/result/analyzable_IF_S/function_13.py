def function_13():
    global belief_set
    if belief_set['agent'][1]['has_key']:
        function_10()
    else:
        function_8()
    function_11()
    if belief_set['map']['grid'][belief_set['agent'][1]['coordinates'][0]][
        belief_set['agent'][1]['coordinates'][1]]['cell_type'] == 'door':
        function_5()
    if belief_set['agent'][1]['energy'] < 30:
        function_1()
        function_2()
        function_3()
        function_4()
