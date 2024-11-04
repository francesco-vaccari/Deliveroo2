def function_17():
    global belief_set
    for cell in belief_set['map']['grid']:
        if cell['cell_type'] == 'parcels_spawn':
            parcel_spawn_coordinates = cell['cell_coordinates']
    agent_coordinates = belief_set['agent'][1]['coordinates']
    while agent_coordinates != parcel_spawn_coordinates:
        if agent_coordinates[0] < parcel_spawn_coordinates[0]:
            function_2()
        elif agent_coordinates[0] > parcel_spawn_coordinates[0]:
            function_1()
        elif agent_coordinates[1] < parcel_spawn_coordinates[1]:
            function_4()
        elif agent_coordinates[1] > parcel_spawn_coordinates[1]:
            function_3()
        agent_coordinates = belief_set['agent'][1]['coordinates']
    function_5()
