def function_8():
    global belief_set
    agent = belief_set['agent'][1]
    parcels = belief_set['parcel']
    map_grid = belief_set['map']['map']['grid']
    delivery_cell = [cell for cell in map_grid if cell['cell_type'] ==
        'delivery_cell'][0]['cell_coordinates']
    if agent['parcels_carried_ids']:
        if agent['coordinates'] == delivery_cell:
            function_6()
        elif agent['coordinates'][0] > delivery_cell[0]:
            function_1()
        elif agent['coordinates'][0] < delivery_cell[0]:
            function_2()
        elif agent['coordinates'][1] > delivery_cell[1]:
            function_3()
        elif agent['coordinates'][1] < delivery_cell[1]:
            function_4()
    else:
        for parcel in parcels.values():
            if agent['coordinates'] == parcel['coordinates']:
                function_5()
                break
            elif agent['coordinates'][0] > parcel['coordinates'][0]:
                function_1()
                break
            elif agent['coordinates'][0] < parcel['coordinates'][0]:
                function_2()
                break
            elif agent['coordinates'][1] > parcel['coordinates'][1]:
                function_3()
                break
            elif agent['coordinates'][1] < parcel['coordinates'][1]:
                function_4()
                break
