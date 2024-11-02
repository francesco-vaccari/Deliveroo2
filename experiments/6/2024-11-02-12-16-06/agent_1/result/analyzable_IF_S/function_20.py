def function_20():
    global belief_set
    agent = belief_set['agent'][1]
    parcels_spawn = next(cell['cell_coordinates'] for cell in belief_set[
        'map']['grid'] if cell['cell_type'] == 'parcels_spawn')
    batteries_spawn = next(cell['cell_coordinates'] for cell in belief_set[
        'map']['grid'] if cell['cell_type'] == 'batteries_spawn')
    delivery_cell = next(cell['cell_coordinates'] for cell in belief_set[
        'map']['grid'] if cell['cell_type'] == 'delivery_cell')
    while agent['coordinates'] != parcels_spawn:
        if agent['coordinates'][0] < parcels_spawn[0]:
            function_2()
        elif agent['coordinates'][0] > parcels_spawn[0]:
            function_1()
        elif agent['coordinates'][1] < parcels_spawn[1]:
            function_4()
        elif agent['coordinates'][1] > parcels_spawn[1]:
            function_3()
        agent = belief_set['agent'][1]
    function_5()
    while agent['coordinates'] != batteries_spawn:
        if agent['coordinates'][0] < batteries_spawn[0]:
            function_2()
        elif agent['coordinates'][0] > batteries_spawn[0]:
            function_1()
        elif agent['coordinates'][1] < batteries_spawn[1]:
            function_4()
        elif agent['coordinates'][1] > batteries_spawn[1]:
            function_3()
        agent = belief_set['agent'][1]
    if agent['energy'] < 50:
        function_5()
    while agent['coordinates'] != delivery_cell:
        if agent['coordinates'][0] < delivery_cell[0]:
            function_2()
        elif agent['coordinates'][0] > delivery_cell[0]:
            function_1()
        elif agent['coordinates'][1] < delivery_cell[1]:
            function_4()
        elif agent['coordinates'][1] > delivery_cell[1]:
            function_3()
        agent = belief_set['agent'][1]
    function_6()
