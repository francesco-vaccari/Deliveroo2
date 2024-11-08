def function_20():
    global belief_set
    agent = belief_set['agent'][1]
    delivery_cell = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'delivery_cell'][0]['cell_coordinates']
    if agent['coordinates'] == delivery_cell and len(agent[
        'parcels_carried_ids']) > 0:
        function_6()
    elif agent['coordinates'][0] < delivery_cell[0]:
        function_2()
    elif agent['coordinates'][0] > delivery_cell[0]:
        function_1()
    elif agent['coordinates'][1] < delivery_cell[1]:
        function_4()
    elif agent['coordinates'][1] > delivery_cell[1]:
        function_3()
    elif agent['energy'] < 30:
        battery_cell = [cell for cell in belief_set['map']['grid'] if cell[
            'cell_type'] == 'batteries_spawn'][0]['cell_coordinates']
        if agent['coordinates'] == battery_cell:
            function_5()
        elif agent['coordinates'][0] < battery_cell[0]:
            function_2()
        elif agent['coordinates'][0] > battery_cell[0]:
            function_1()
        elif agent['coordinates'][1] < battery_cell[1]:
            function_4()
        elif agent['coordinates'][1] > battery_cell[1]:
            function_3()
    else:
        function_7()
