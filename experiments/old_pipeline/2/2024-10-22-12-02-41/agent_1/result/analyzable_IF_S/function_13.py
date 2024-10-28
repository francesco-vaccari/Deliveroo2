def function_13():
    global belief_set
    for cell in belief_set['map']['grid']:
        if cell['cell_type'] == 'walkable':
            agent_coordinates = belief_set['agent']['coordinates']
            if cell['cell_coordinates'][0] > agent_coordinates[0]:
                function_2()
            elif cell['cell_coordinates'][0] < agent_coordinates[0]:
                function_1()
            if cell['cell_coordinates'][1] > agent_coordinates[1]:
                function_4()
            elif cell['cell_coordinates'][1] < agent_coordinates[1]:
                function_3()
            for key in belief_set['keys'].values():
                if key['coordinates'] == cell['cell_coordinates'] and key[
                    'carried_by_id'] is None:
                    function_5()
                    break
            for parcel in belief_set['parcels'].values():
                if parcel['coordinates'] == cell['cell_coordinates'
                    ] and parcel['carried_by_id'] is None:
                    function_5()
                    break
