def function_16():
    global belief_set
    agent_coordinates = belief_set['agent'][1]['coordinates']
    parcels_coordinates = [p['coordinates'] for p in belief_set['parcels'].
        values() if p['carried_by_id'] == None]
    parcel_coordinates = min(parcels_coordinates, key=lambda c: abs(c[0] -
        agent_coordinates[0]) + abs(c[1] - agent_coordinates[1]))
    while agent_coordinates != parcel_coordinates:
        if agent_coordinates[0] > parcel_coordinates[0]:
            function_1()
            agent_coordinates[0] -= 1
        elif agent_coordinates[0] < parcel_coordinates[0]:
            function_2()
            agent_coordinates[0] += 1
        elif agent_coordinates[1] > parcel_coordinates[1]:
            function_3()
            agent_coordinates[1] -= 1
        elif agent_coordinates[1] < parcel_coordinates[1]:
            function_4()
            agent_coordinates[1] += 1
    function_5()
    delivery_coordinates = [cell['cell_coordinates'] for cell in belief_set
        ['map']['grid'] if cell['cell_type'] == 'delivery_cell'][0]
    while agent_coordinates != delivery_coordinates:
        if agent_coordinates[0] > delivery_coordinates[0]:
            function_1()
            agent_coordinates[0] -= 1
        elif agent_coordinates[0] < delivery_coordinates[0]:
            function_2()
            agent_coordinates[0] += 1
        elif agent_coordinates[1] > delivery_coordinates[1]:
            function_3()
            agent_coordinates[1] -= 1
        elif agent_coordinates[1] < delivery_coordinates[1]:
            function_4()
            agent_coordinates[1] += 1
    function_6()
