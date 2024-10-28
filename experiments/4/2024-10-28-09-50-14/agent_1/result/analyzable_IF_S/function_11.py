def function_11():
    global belief_set
    if not belief_set['agents'][1]['parcels_carried_ids']:
        function_9()
    else:
        parcel_coordinates = belief_set['parcels'][belief_set['agents'][1][
            'parcels_carried_ids'][0]]['coordinates']
        delivery_coordinates = [cell['cell_coordinates'] for cell in
            belief_set['map']['grid'] if 'delivery_cell' in cell['cell_type']][
            0]
        if parcel_coordinates[0] < delivery_coordinates[0]:
            function_2()
        elif parcel_coordinates[0] > delivery_coordinates[0]:
            function_1()
        elif parcel_coordinates[1] < delivery_coordinates[1]:
            function_4()
        elif parcel_coordinates[1] > delivery_coordinates[1]:
            function_3()
        else:
            function_6()
