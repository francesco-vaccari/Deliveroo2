def function_14():
    global belief_set
    delivery_coordinates = [cell['cell_coordinates'] for cell in belief_set
        ['map']['grid'] if cell['cell_type'] == 'delivery_cell'][0]
    agent_coordinates = belief_set['agent'][1]['coordinates']
    while agent_coordinates != delivery_coordinates:
        if agent_coordinates[0] > delivery_coordinates[0]:
            function_1()
        elif agent_coordinates[0] < delivery_coordinates[0]:
            function_2()
        if agent_coordinates[1] > delivery_coordinates[1]:
            function_3()
        elif agent_coordinates[1] < delivery_coordinates[1]:
            function_4()
        agent_coordinates = belief_set['agent'][1]['coordinates']
    function_6()
