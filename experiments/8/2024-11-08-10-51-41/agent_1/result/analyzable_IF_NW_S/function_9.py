def function_9():
    global belief_set
    parcel_spawn_location = None
    for cell in belief_set['map']['grid']:
        if cell['cell_type'] == 'parcels_spawn':
            parcel_spawn_location = cell['cell_coordinates']
            break
    if parcel_spawn_location is not None:
        agent_location = belief_set['agent'][1]['coordinates']
        if agent_location[0] < parcel_spawn_location[0]:
            function_2()
        elif agent_location[0] > parcel_spawn_location[0]:
            function_1()
        elif agent_location[1] < parcel_spawn_location[1]:
            function_4()
        elif agent_location[1] > parcel_spawn_location[1]:
            function_3()
        if belief_set['agent'][1]['energy'] < 20:
            belief_set['agent'][1]['energy'] += 20
