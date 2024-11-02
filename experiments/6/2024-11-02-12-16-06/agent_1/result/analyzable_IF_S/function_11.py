def function_11():
    global belief_set
    delivery_cell = [item['cell_coordinates'] for item in belief_set['map']
        ['grid'] if item['cell_type'] == 'delivery_cell'][0]
    agent = belief_set['agent'][1]
    while agent['coordinates'] != delivery_cell:
        if agent['coordinates'][0] > delivery_cell[0]:
            function_1()
        elif agent['coordinates'][0] < delivery_cell[0]:
            function_2()
        elif agent['coordinates'][1] > delivery_cell[1]:
            function_3()
        elif agent['coordinates'][1] < delivery_cell[1]:
            function_4()
        agent = belief_set['agent'][1]
        if agent['coordinates'] == [item['cell_coordinates'] for item in
            belief_set['map']['grid'] if item['cell_type'] == 'batteries_spawn'
            ][0] and agent['energy'] < 50:
            function_5()
    function_6()
