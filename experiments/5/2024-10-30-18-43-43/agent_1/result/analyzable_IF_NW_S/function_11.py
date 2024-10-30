def function_11():
    global belief_set
    agent = belief_set['agent'][1]
    parcels = belief_set['parcels']
    for parcel_id, parcel_info in parcels.items():
        if parcel_info['carried_by_id'] is None:
            if parcel_info['coordinates'][0] < agent['coordinates'][0]:
                function_1()
                break
            elif parcel_info['coordinates'][0] > agent['coordinates'][0]:
                function_2()
                break
            elif parcel_info['coordinates'][1] < agent['coordinates'][1]:
                function_3()
                break
            elif parcel_info['coordinates'][1] > agent['coordinates'][1]:
                function_4()
                break
    function_5()
    for cell_info in belief_set['map']['grid']:
        if cell_info['cell_type'] == 'delivery_cell':
            if cell_info['cell_coordinates'][0] < agent['coordinates'][0]:
                function_1()
                break
            elif cell_info['cell_coordinates'][0] > agent['coordinates'][0]:
                function_2()
                break
            elif cell_info['cell_coordinates'][1] < agent['coordinates'][1]:
                function_3()
                break
            elif cell_info['cell_coordinates'][1] > agent['coordinates'][1]:
                function_4()
                break
