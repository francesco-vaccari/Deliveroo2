def function_10():
    global belief_set
    agent = belief_set['agent'][1]
    battery_spawn = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'batteries_spawn'][0]['cell_coordinates']
    if agent['energy'] < 30:
        if agent['coordinates'] == battery_spawn:
            function_5()
        else:
            function_9()
    elif agent['coordinates'][0] < battery_spawn[0]:
        function_2()
    elif agent['coordinates'][0] > battery_spawn[0]:
        function_1()
    elif agent['coordinates'][1] < battery_spawn[1]:
        function_4()
    elif agent['coordinates'][1] > battery_spawn[1]:
        function_3()
