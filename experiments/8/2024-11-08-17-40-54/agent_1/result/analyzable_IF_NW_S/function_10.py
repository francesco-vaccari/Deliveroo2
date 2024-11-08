def function_10():
    global belief_set
    agent = belief_set['agent']
    map_grid = belief_set['map']['grid']
    delivery_cell = next((cell for cell in map_grid if cell['cell_type'] ==
        'delivery_cell'), None)
    if not delivery_cell:
        return
    delivery_coordinates = delivery_cell['cell_coordinates']
    while agent['coordinates'] != delivery_coordinates and agent['energy'
        ] > 10:
        if agent['coordinates'][0] > delivery_coordinates[0]:
            function_1()
        elif agent['coordinates'][0] < delivery_coordinates[0]:
            function_2()
        elif agent['coordinates'][1] > delivery_coordinates[1]:
            function_3()
        elif agent['coordinates'][1] < delivery_coordinates[1]:
            function_4()
    if agent['coordinates'] == delivery_coordinates and agent[
        'parcels_carried_ids']:
        function_6()
