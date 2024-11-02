def function_14():
    global belief_set
    agent_coordinates = belief_set['agent']['coordinates']
    delivery_cell = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'delivery_cell'][0]['cell_coordinates']
    while agent_coordinates != delivery_cell:
        if agent_coordinates[0] < delivery_cell[0]:
            function_2()
        elif agent_coordinates[0] > delivery_cell[0]:
            function_1()
        elif agent_coordinates[1] < delivery_cell[1]:
            function_4()
        else:
            function_3()
        agent_coordinates = belief_set['agent']['coordinates']
    function_6()
    battery_spawn = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'batteries_spawn'][0]['cell_coordinates']
    while agent_coordinates != battery_spawn:
        if agent_coordinates[0] < battery_spawn[0]:
            function_2()
        elif agent_coordinates[0] > battery_spawn[0]:
            function_1()
        elif agent_coordinates[1] < battery_spawn[1]:
            function_4()
        else:
            function_3()
        agent_coordinates = belief_set['agent']['coordinates']
