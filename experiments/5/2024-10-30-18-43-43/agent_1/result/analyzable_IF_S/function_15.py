def function_15():
    global belief_set
    agent = belief_set['agent'][1]
    parcel_spawn = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'parcels_spawn'][0]['cell_coordinates']
    delivery_cell = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'delivery_cell'][0]['cell_coordinates']
    if not agent['parcels_carried_ids']:
        if agent['coordinates'][0] < parcel_spawn[0]:
            function_2()
        elif agent['coordinates'][0] > parcel_spawn[0]:
            function_1()
        elif agent['coordinates'][1] < parcel_spawn[1]:
            function_4()
        elif agent['coordinates'][1] > parcel_spawn[1]:
            function_3()
        else:
            function_5()
    elif agent['coordinates'][0] < delivery_cell[0]:
        function_2()
    elif agent['coordinates'][0] > delivery_cell[0]:
        function_1()
    elif agent['coordinates'][1] < delivery_cell[1]:
        function_4()
    elif agent['coordinates'][1] > delivery_cell[1]:
        function_3()
    else:
        function_6()
