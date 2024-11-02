def function_18():
    global belief_set
    agent = belief_set['agent'][1]
    if agent['energy'] > 50:
        if not agent['parcels_carried_ids']:
            if belief_set['parcels'] and agent['coordinates'][0] > belief_set[
                'parcels'][list(belief_set['parcels'].keys())[0]]['coordinates'
                ][0]:
                function_1()
            elif belief_set['parcels'] and agent['coordinates'][0
                ] < belief_set['parcels'][list(belief_set['parcels'].keys())[0]
                ]['coordinates'][0]:
                function_2()
            elif belief_set['parcels'] and agent['coordinates'][1
                ] > belief_set['parcels'][list(belief_set['parcels'].keys())[0]
                ]['coordinates'][1]:
                function_3()
            elif belief_set['parcels'] and agent['coordinates'][1
                ] < belief_set['parcels'][list(belief_set['parcels'].keys())[0]
                ]['coordinates'][1]:
                function_4()
            else:
                function_5()
        elif agent['coordinates'][0] > belief_set['map']['grid'][11][
            'cell_coordinates'][0]:
            function_1()
        elif agent['coordinates'][0] < belief_set['map']['grid'][11][
            'cell_coordinates'][0]:
            function_2()
        elif agent['coordinates'][1] > belief_set['map']['grid'][11][
            'cell_coordinates'][1]:
            function_3()
        elif agent['coordinates'][1] < belief_set['map']['grid'][11][
            'cell_coordinates'][1]:
            function_4()
        else:
            function_6()
    elif belief_set['batteries'] and agent['coordinates'][0] > belief_set[
        'batteries'][list(belief_set['batteries'].keys())[0]]['coordinates'][0
        ]:
        function_1()
    elif belief_set['batteries'] and agent['coordinates'][0] < belief_set[
        'batteries'][list(belief_set['batteries'].keys())[0]]['coordinates'][0
        ]:
        function_2()
    elif belief_set['batteries'] and agent['coordinates'][1] > belief_set[
        'batteries'][list(belief_set['batteries'].keys())[0]]['coordinates'][1
        ]:
        function_3()
    elif belief_set['batteries'] and agent['coordinates'][1] < belief_set[
        'batteries'][list(belief_set['batteries'].keys())[0]]['coordinates'][1
        ]:
        function_4()
    else:
        function_5()
