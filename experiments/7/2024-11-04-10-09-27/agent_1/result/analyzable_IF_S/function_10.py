def function_10():
    global belief_set
    agent = belief_set['agent'][1]
    parcels = belief_set['parcels']
    delivery_cells = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'delivery_cell']
    target_parcel = min(parcels.values(), key=lambda p: abs(p['coordinates'
        ][0] - agent['coordinates'][0]) + abs(p['coordinates'][1] - agent[
        'coordinates'][1]))
    target_delivery_cell = min(delivery_cells, key=lambda c: abs(c[
        'cell_coordinates'][0] - agent['coordinates'][0]) + abs(c[
        'cell_coordinates'][1] - agent['coordinates'][1]))
    while agent['coordinates'] != target_parcel['coordinates']:
        if agent['coordinates'][0] < target_parcel['coordinates'][0]:
            function_2()
            agent['coordinates'][0] += 1
        elif agent['coordinates'][0] > target_parcel['coordinates'][0]:
            function_1()
            agent['coordinates'][0] -= 1
        if agent['coordinates'][1] < target_parcel['coordinates'][1]:
            function_4()
            agent['coordinates'][1] += 1
        elif agent['coordinates'][1] > target_parcel['coordinates'][1]:
            function_3()
            agent['coordinates'][1] -= 1
    function_5()
    while agent['coordinates'] != target_delivery_cell['cell_coordinates']:
        if agent['coordinates'][0] < target_delivery_cell['cell_coordinates'][0
            ]:
            function_2()
            agent['coordinates'][0] += 1
        elif agent['coordinates'][0] > target_delivery_cell['cell_coordinates'
            ][0]:
            function_1()
            agent['coordinates'][0] -= 1
        if agent['coordinates'][1] < target_delivery_cell['cell_coordinates'][1
            ]:
            function_4()
            agent['coordinates'][1] += 1
        elif agent['coordinates'][1] > target_delivery_cell['cell_coordinates'
            ][1]:
            function_3()
            agent['coordinates'][1] -= 1
    function_6()
