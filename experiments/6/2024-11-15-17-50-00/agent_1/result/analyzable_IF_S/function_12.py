def function_12():
    global belief_set
    agent = belief_set['agent'][1]
    delivery_cell = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'delivery_cell'][0]['cell_coordinates']
    if agent['coordinates'][0] < delivery_cell[0]:
        function_2()
    elif agent['coordinates'][0] > delivery_cell[0]:
        function_1()
    elif agent['coordinates'][1] < delivery_cell[1]:
        function_4()
    elif agent['coordinates'][1] > delivery_cell[1]:
        function_3()
    if belief_set['batteries'][1]['coordinates'] == agent['coordinates'
        ] and agent['energy'] < 50:
        function_5()
    if any(parcel['coordinates'] == agent['coordinates'] and parcel[
        'carried_by_id'] is None for parcel in belief_set['parcels'].values()):
        function_5()
    if agent['coordinates'] == delivery_cell and agent['parcels_carried_ids']:
        function_6()
