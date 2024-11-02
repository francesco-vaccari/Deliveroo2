def function_8():
    global belief_set
    agent = belief_set['agent'][1]
    parcel_spawn_cell = [cell for cell in belief_set['map']['grid'] if cell
        ['cell_type'] == 'parcels_spawn'][0]
    parcel_spawn_coordinates = parcel_spawn_cell['cell_coordinates']
    while agent['coordinates'] != parcel_spawn_coordinates:
        if agent['coordinates'][0] > parcel_spawn_coordinates[0]:
            function_1()
        elif agent['coordinates'][0] < parcel_spawn_coordinates[0]:
            function_2()
        elif agent['coordinates'][1] > parcel_spawn_coordinates[1]:
            function_3()
        elif agent['coordinates'][1] < parcel_spawn_coordinates[1]:
            function_4()
    function_5()
