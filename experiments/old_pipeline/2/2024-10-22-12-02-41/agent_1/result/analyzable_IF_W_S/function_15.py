def function_15():
    global belief_set
    if belief_set['agent']['parcels_carried_ids']:
        parcel_id = belief_set['agent']['parcels_carried_ids'][0]
        for cell in belief_set['map']['grid']:
            if cell['cell_type'] == 'delivery_cell':
                delivery_cell = cell['cell_coordinates']
                break
        while belief_set['agent']['coordinates'] != delivery_cell:
            if belief_set['agent']['coordinates'][0] > delivery_cell[0]:
                function_1()
            elif belief_set['agent']['coordinates'][0] < delivery_cell[0]:
                function_2()
            elif belief_set['agent']['coordinates'][1] > delivery_cell[1]:
                function_3()
            else:
                function_4()
        function_6()
