def function_11():
    global belief_set
    agent = belief_set['agent'][1]
    parcels = belief_set['parcels']
    map_grid = belief_set['map']['grid']
    delivery_cell = [cell for cell in map_grid if cell['cell_type'] ==
        'delivery_cell'][0]
    while True:
        if not agent['parcels_carried_ids']:
            function_5()
            if agent['parcels_carried_ids']:
                continue
        if agent['coordinates'][0] > delivery_cell['cell_coordinates'][0]:
            function_1()
        elif agent['coordinates'][0] < delivery_cell['cell_coordinates'][0]:
            function_2()
        if agent['coordinates'][1] > delivery_cell['cell_coordinates'][1]:
            function_3()
        elif agent['coordinates'][1] < delivery_cell['cell_coordinates'][1]:
            function_4()
        if agent['coordinates'] == delivery_cell['cell_coordinates'] and agent[
            'parcels_carried_ids']:
            function_6()
            break
