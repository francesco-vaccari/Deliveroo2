def function_18():
    global belief_set
    agent_coords = belief_set['agent']['coordinates']
    parcels = belief_set['parcels']
    for parcel in parcels:
        parcel_coords = parcel['coordinates']
        if parcel_coords[0] < agent_coords[0]:
            function_1()
        elif parcel_coords[0] > agent_coords[0]:
            function_2()
        elif parcel_coords[1] < agent_coords[1]:
            function_3()
        elif parcel_coords[1] > agent_coords[1]:
            function_4()
    function_5()
    delivery_cell_coords = [coord['cell_coordinates'] for coord in
        belief_set['map']['grid'] if coord['cell_type'] == 'delivery_cell'][0]
    if delivery_cell_coords[0] < agent_coords[0]:
        function_1()
    elif delivery_cell_coords[0] > agent_coords[0]:
        function_2()
    elif delivery_cell_coords[1] < agent_coords[1]:
        function_3()
    elif delivery_cell_coords[1] > agent_coords[1]:
        function_4()
    function_6()
