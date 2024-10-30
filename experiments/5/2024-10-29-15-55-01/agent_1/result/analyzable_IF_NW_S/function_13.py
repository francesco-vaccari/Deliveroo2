def function_13():
    global belief_set
    agent = belief_set['agent'][1]
    if belief_set['parcels']:
        parcel = list(belief_set['parcels'].values())[0]
        while agent['coordinates'] != parcel['coordinates']:
            if agent['coordinates'][0] < parcel['coordinates'][0]:
                function_2()
            elif agent['coordinates'][0] > parcel['coordinates'][0]:
                function_1()
            if agent['coordinates'][1] < parcel['coordinates'][1]:
                function_4()
            elif agent['coordinates'][1] > parcel['coordinates'][1]:
                function_3()
        function_5()
    delivery_cell = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'delivery_cell'][0]
    while agent['coordinates'] != delivery_cell['cell_coordinates']:
        if agent['coordinates'][0] < delivery_cell['cell_coordinates'][0]:
            function_2()
        elif agent['coordinates'][0] > delivery_cell['cell_coordinates'][0]:
            function_1()
        if agent['coordinates'][1] < delivery_cell['cell_coordinates'][1]:
            function_4()
        elif agent['coordinates'][1] > delivery_cell['cell_coordinates'][1]:
            function_3()
    function_6()
