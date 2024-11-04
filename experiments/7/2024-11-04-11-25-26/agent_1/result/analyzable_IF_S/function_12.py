def function_12():
    global belief_set
    agent_coordinates = belief_set['agent'][1]['coordinates']
    battery_coordinates = belief_set['batteries'][0]['coordinates']
    delivery_coordinates = [i['cell_coordinates'] for i in belief_set['map'
        ]['grid'] if i['cell_type'] == 'delivery_cell'][0]
    while agent_coordinates != battery_coordinates:
        if agent_coordinates[0] < battery_coordinates[0]:
            function_2()
        elif agent_coordinates[0] > battery_coordinates[0]:
            function_1()
        elif agent_coordinates[1] < battery_coordinates[1]:
            function_4()
        elif agent_coordinates[1] > battery_coordinates[1]:
            function_3()
        agent_coordinates = belief_set['agent'][1]['coordinates']
    function_5()
    while agent_coordinates != delivery_coordinates:
        if agent_coordinates[0] < delivery_coordinates[0]:
            function_2()
        elif agent_coordinates[0] > delivery_coordinates[0]:
            function_1()
        elif agent_coordinates[1] < delivery_coordinates[1]:
            function_4()
        elif agent_coordinates[1] > delivery_coordinates[1]:
            function_3()
        agent_coordinates = belief_set['agent'][1]['coordinates']
    function_6()
