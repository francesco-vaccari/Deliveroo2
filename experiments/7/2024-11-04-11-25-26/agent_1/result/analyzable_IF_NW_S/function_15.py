def function_15():
    global belief_set
    agent = belief_set['agent'][1]
    parcels = belief_set['parcels']
    map_grid = belief_set['map']['grid']
    max_iterations = belief_set['map']['width'] * belief_set['map']['height']
    iterations = 0
    while iterations < max_iterations:
        for parcel in parcels:
            if parcel['carried_by_id'] is None:
                parcel_coordinates = parcel['coordinates']
                for cell in map_grid:
                    if cell['cell_coordinates'] == parcel_coordinates and cell[
                        'cell_type'] == 'walkable':
                        if agent['coordinates'][0] < parcel_coordinates[0]:
                            function_2()
                        elif agent['coordinates'][0] > parcel_coordinates[0]:
                            function_1()
                        elif agent['coordinates'][1] < parcel_coordinates[1]:
                            function_4()
                        elif agent['coordinates'][1] > parcel_coordinates[1]:
                            function_3()
                        elif agent['coordinates'] == parcel_coordinates:
                            function_5()
                            return
        iterations += 1
