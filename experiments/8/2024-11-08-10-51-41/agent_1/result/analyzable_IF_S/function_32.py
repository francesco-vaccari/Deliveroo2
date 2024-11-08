def function_32():
    global belief_set
    agent = belief_set['agent'][1]
    delivery_cell = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'delivery_cell'][0]
    if agent['coordinates'] == delivery_cell['cell_coordinates']:
        function_6()
    elif agent['energy'] < 20:
        battery = [cell for cell in belief_set['map']['grid'] if cell[
            'cell_type'] == 'batteries_spawn'][0]
        if agent['coordinates'][0] < battery['cell_coordinates'][0]:
            function_2()
        elif agent['coordinates'][0] > battery['cell_coordinates'][0]:
            function_1()
        elif agent['coordinates'][1] < battery['cell_coordinates'][1]:
            function_4()
        else:
            function_3()
    elif agent['coordinates'][0] < delivery_cell['cell_coordinates'][0]:
        function_2()
    elif agent['coordinates'][0] > delivery_cell['cell_coordinates'][0]:
        function_1()
    elif agent['coordinates'][1] < delivery_cell['cell_coordinates'][1]:
        function_4()
    else:
        function_3()
