def function_15():
    global belief_set
    parcel_spawn = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'parcels_spawn'][0]['cell_coordinates']
    delivery_cell = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'delivery_cell'][0]['cell_coordinates']
    agent_coordinates = belief_set['agent'][1]['coordinates']
    while agent_coordinates != parcel_spawn:
        if agent_coordinates[0] < parcel_spawn[0]:
            function_2()
            agent_coordinates[0] += 1
        elif agent_coordinates[0] > parcel_spawn[0]:
            function_1()
            agent_coordinates[0] -= 1
        elif agent_coordinates[1] < parcel_spawn[1]:
            function_4()
            agent_coordinates[1] += 1
        elif agent_coordinates[1] > parcel_spawn[1]:
            function_3()
            agent_coordinates[1] -= 1
    function_5()
    while agent_coordinates != delivery_cell:
        if agent_coordinates[0] < delivery_cell[0]:
            function_2()
            agent_coordinates[0] += 1
        elif agent_coordinates[0] > delivery_cell[0]:
            function_1()
            agent_coordinates[0] -= 1
        elif agent_coordinates[1] < delivery_cell[1]:
            function_4()
            agent_coordinates[1] += 1
        elif agent_coordinates[1] > delivery_cell[1]:
            function_3()
            agent_coordinates[1] -= 1
    function_6()
