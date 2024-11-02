def function_9():
    global belief_set
    parcel_coordinates = [parcel['coordinates'] for parcel in belief_set[
        'parcels'].values() if parcel['carried_by_id'] is None]
    delivery_coordinates = [cell['cell_coordinates'] for cell in belief_set
        ['map']['grid'] if cell['cell_type'] == 'delivery_cell'][0]
    agent_coordinates = belief_set['agent'][1]['coordinates']
    while agent_coordinates != parcel_coordinates[0]:
        if agent_coordinates[0] < parcel_coordinates[0][0]:
            function_2()
        elif agent_coordinates[0] > parcel_coordinates[0][0]:
            function_1()
        if agent_coordinates[1] < parcel_coordinates[0][1]:
            function_4()
        elif agent_coordinates[1] > parcel_coordinates[0][1]:
            function_3()
        agent_coordinates = belief_set['agent'][1]['coordinates']
    function_5()
    while agent_coordinates != delivery_coordinates:
        if agent_coordinates[0] < delivery_coordinates[0]:
            function_2()
        elif agent_coordinates[0] > delivery_coordinates[0]:
            function_1()
        if agent_coordinates[1] < delivery_coordinates[1]:
            function_4()
        elif agent_coordinates[1] > delivery_coordinates[1]:
            function_3()
        agent_coordinates = belief_set['agent'][1]['coordinates']
    function_6()
