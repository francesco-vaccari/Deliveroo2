def function_25():
    global belief_set
    agent = belief_set['agent'][1]
    batteries_spawn = [cell['cell_coordinates'] for cell in belief_set[
        'map']['grid'] if cell['cell_type'] == 'batteries_spawn'][0]
    parcels_spawn = [cell['cell_coordinates'] for cell in belief_set['map']
        ['grid'] if cell['cell_type'] == 'parcels_spawn'][0]
    delivery_cell = [cell['cell_coordinates'] for cell in belief_set['map']
        ['grid'] if cell['cell_type'] == 'delivery_cell'][0]
    max_moves = belief_set['map']['width'] * belief_set['map']['height']
    for _ in range(max_moves):
        if agent['coordinates'][0] > batteries_spawn[0]:
            function_1()
        elif agent['coordinates'][0] < batteries_spawn[0]:
            function_2()
        elif agent['coordinates'][1] > batteries_spawn[1]:
            function_3()
        elif agent['coordinates'][1] < batteries_spawn[1]:
            function_4()
        else:
            break
    function_5()
    for _ in range(max_moves):
        if agent['coordinates'][0] > parcels_spawn[0]:
            function_1()
        elif agent['coordinates'][0] < parcels_spawn[0]:
            function_2()
        elif agent['coordinates'][1] > parcels_spawn[1]:
            function_3()
        elif agent['coordinates'][1] < parcels_spawn[1]:
            function_4()
        else:
            break
    function_5()
    for _ in range(max_moves):
        if agent['coordinates'][0] > delivery_cell[0]:
            function_1()
        elif agent['coordinates'][0] < delivery_cell[0]:
            function_2()
        elif agent['coordinates'][1] > delivery_cell[1]:
            function_3()
        elif agent['coordinates'][1] < delivery_cell[1]:
            function_4()
        else:
            break
    function_6()
