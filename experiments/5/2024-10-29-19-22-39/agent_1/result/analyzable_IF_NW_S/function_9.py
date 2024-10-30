def function_9():
    global belief_set
    max_attempts = 10
    attempts = 0
    while attempts < max_attempts and belief_set['agent'][1][
        'parcels_carried_ids']:
        coordinates = belief_set['agent'][1]['coordinates']
        if [coordinates[0] + 1, coordinates[1]] in [item['cell_coordinates'
            ] for item in belief_set['map']['grid'] if item['cell_type'] ==
            'walkable']:
            function_2()
        elif [coordinates[0], coordinates[1] + 1] in [item[
            'cell_coordinates'] for item in belief_set['map']['grid'] if 
            item['cell_type'] == 'walkable']:
            function_4()
        elif [coordinates[0] - 1, coordinates[1]] in [item[
            'cell_coordinates'] for item in belief_set['map']['grid'] if 
            item['cell_type'] == 'walkable']:
            function_1()
        elif [coordinates[0], coordinates[1] - 1] in [item[
            'cell_coordinates'] for item in belief_set['map']['grid'] if 
            item['cell_type'] == 'walkable']:
            function_3()
        attempts += 1
    if belief_set['agent'][1]['coordinates'] in [item['cell_coordinates'] for
        item in belief_set['map']['grid'] if item['cell_type'] ==
        'delivery_cell'] and belief_set['agent'][1]['parcels_carried_ids']:
        function_6()
