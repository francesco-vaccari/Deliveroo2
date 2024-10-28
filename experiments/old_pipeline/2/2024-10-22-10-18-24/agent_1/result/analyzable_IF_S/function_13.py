def function_13():
    global belief_set
    agent_coordinates = belief_set['agent']['coordinates']
    delivery_coordinates = [cell['cell_coordinates'] for cell in belief_set
        ['map']['grid'] if cell['cell_type'] == 'delivery_cell'][0]
    if agent_coordinates[0] < delivery_coordinates[0]:
        function_2()
    elif agent_coordinates[0] > delivery_coordinates[0]:
        function_1()
    elif agent_coordinates[1] < delivery_coordinates[1]:
        function_4()
    elif agent_coordinates[1] > delivery_coordinates[1]:
        function_3()
    if agent_coordinates == delivery_coordinates and belief_set['agent'][
        'parcels_carried_ids']:
        function_6()
