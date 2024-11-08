def function_8():
    global belief_set
    agent = belief_set['agent'][1]
    parcels = belief_set['parcels']
    map = belief_set['map']['grid']
    delivery_point = [cell for cell in map if cell['cell_type'] ==
        'parcels_spawn'][0]['cell_coordinates']
    for parcel_id, parcel in parcels.items():
        if parcel['carried_by_id'] is None:
            if agent['coordinates'] == parcel['coordinates']:
                function_5()
            elif agent['coordinates'][0] < parcel['coordinates'][0]:
                function_2()
            elif agent['coordinates'][0] > parcel['coordinates'][0]:
                function_1()
            elif agent['coordinates'][1] < parcel['coordinates'][1]:
                function_4()
            else:
                function_3()
        elif parcel['carried_by_id'] == agent['id']:
            if agent['coordinates'] == delivery_point:
                function_6()
            elif agent['coordinates'][0] < delivery_point[0]:
                function_2()
            elif agent['coordinates'][0] > delivery_point[0]:
                function_1()
            elif agent['coordinates'][1] < delivery_point[1]:
                function_4()
            else:
                function_3()
