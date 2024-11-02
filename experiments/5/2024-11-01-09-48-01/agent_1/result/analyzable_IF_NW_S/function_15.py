def function_15():
    global belief_set
    agent = belief_set['agent'][1]
    parcels = belief_set['parcels']
    map_grid = belief_set['map']['grid']
    delivery_cell = [cell for cell in map_grid if cell['cell_type'] ==
        'delivery_cell'][0]
    agent_cell = [cell for cell in map_grid if cell['cell_coordinates'] ==
        agent['coordinates']][0]
    if not agent['parcels_carried_ids']:
        parcel_spawn = [cell for cell in map_grid if cell['cell_type'] ==
            'parcels_spawn'][0]
        if agent_cell['cell_coordinates'][0] < parcel_spawn['cell_coordinates'
            ][0]:
            function_2()
        elif agent_cell['cell_coordinates'][0] > parcel_spawn[
            'cell_coordinates'][0]:
            function_1()
        elif agent_cell['cell_coordinates'][1] < parcel_spawn[
            'cell_coordinates'][1]:
            function_4()
        elif agent_cell['cell_coordinates'][1] > parcel_spawn[
            'cell_coordinates'][1]:
            function_3()
        function_5()
    else:
        if agent_cell['cell_coordinates'][0] < delivery_cell['cell_coordinates'
            ][0]:
            function_2()
        elif agent_cell['cell_coordinates'][0] > delivery_cell[
            'cell_coordinates'][0]:
            function_1()
        elif agent_cell['cell_coordinates'][1] < delivery_cell[
            'cell_coordinates'][1]:
            function_4()
        elif agent_cell['cell_coordinates'][1] > delivery_cell[
            'cell_coordinates'][1]:
            function_3()
        function_6()
