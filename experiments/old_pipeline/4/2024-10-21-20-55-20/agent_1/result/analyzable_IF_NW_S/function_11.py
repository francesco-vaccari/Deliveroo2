def function_11():
    global belief_set
    agent_coordinates = belief_set['agent']['coordinates']
    parcel_coordinates = belief_set['parcels'][1]['coordinates']
    delivery_cell_coordinates = [cell['cell_coordinates'] for cell in
        belief_set['map']['grid'] if cell['cell_type'] in ['delivery_cell',
        'double_delivery_cell']][0]
    while agent_coordinates != parcel_coordinates:
        if parcel_coordinates[0] < agent_coordinates[0]:
            function_1()
        elif parcel_coordinates[0] > agent_coordinates[0]:
            function_2()
        elif parcel_coordinates[1] < agent_coordinates[1]:
            function_3()
        elif parcel_coordinates[1] > agent_coordinates[1]:
            function_4()
        agent_coordinates = belief_set['agent']['coordinates']
    function_5()
    while agent_coordinates != delivery_cell_coordinates:
        if delivery_cell_coordinates[0] < agent_coordinates[0]:
            function_1()
        elif delivery_cell_coordinates[0] > agent_coordinates[0]:
            function_2()
        elif delivery_cell_coordinates[1] < agent_coordinates[1]:
            function_3()
        elif delivery_cell_coordinates[1] > agent_coordinates[1]:
            function_4()
        agent_coordinates = belief_set['agent']['coordinates']
