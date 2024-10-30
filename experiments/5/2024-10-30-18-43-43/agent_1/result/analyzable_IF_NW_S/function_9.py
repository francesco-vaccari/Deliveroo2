def function_9():
    global belief_set
    agent = belief_set['agent'][1]
    parcel_spawn = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'parcels_spawn'][0]
    delivery_cell = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'delivery_cell'][0]
    while agent['coordinates'] != parcel_spawn['cell_coordinates']:
        if agent['coordinates'][0] < parcel_spawn['cell_coordinates'][0]:
            function_2()
        elif agent['coordinates'][0] > parcel_spawn['cell_coordinates'][0]:
            function_1()
        if agent['coordinates'][1] < parcel_spawn['cell_coordinates'][1]:
            function_4()
        elif agent['coordinates'][1] > parcel_spawn['cell_coordinates'][1]:
            function_3()
        agent['coordinates'] = [agent['coordinates'][0] + (parcel_spawn[
            'cell_coordinates'][0] - agent['coordinates'][0]), agent[
            'coordinates'][1] + (parcel_spawn['cell_coordinates'][1] -
            agent['coordinates'][1])]
    function_5()
    while agent['coordinates'] != delivery_cell['cell_coordinates']:
        if agent['coordinates'][0] < delivery_cell['cell_coordinates'][0]:
            function_2()
        elif agent['coordinates'][0] > delivery_cell['cell_coordinates'][0]:
            function_1()
        if agent['coordinates'][1] < delivery_cell['cell_coordinates'][1]:
            function_4()
        elif agent['coordinates'][1] > delivery_cell['cell_coordinates'][1]:
            function_3()
        agent['coordinates'] = [agent['coordinates'][0] + (delivery_cell[
            'cell_coordinates'][0] - agent['coordinates'][0]), agent[
            'coordinates'][1] + (delivery_cell['cell_coordinates'][1] -
            agent['coordinates'][1])]
    function_6()
