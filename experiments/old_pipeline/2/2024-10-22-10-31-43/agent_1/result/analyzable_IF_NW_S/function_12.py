def function_12():
    global belief_set
    agent_coordinates = belief_set['agent'][1]['coordinates']
    delivery_coordinates = [item['cell_coordinates'] for item in belief_set
        ['map']['grid'] if item['cell_type'] == 'delivery_cell'][0]
    if agent_coordinates[0] > delivery_coordinates[0]:
        function_1()
    elif agent_coordinates[0] < delivery_coordinates[0]:
        function_2()
    elif agent_coordinates[1] > delivery_coordinates[1]:
        function_3()
    elif agent_coordinates[1] < delivery_coordinates[1]:
        function_4()
    if agent_coordinates == delivery_coordinates:
        function_6()
