def function_12():
    global belief_set
    current_position = belief_set['agent'][1]['coordinates']
    parcel_spawn = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'parcels_spawn'][0]['cell_coordinates']
    delivery_cell = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'delivery_cell'][0]['cell_coordinates']
    while current_position != parcel_spawn:
        if parcel_spawn[0] < current_position[0]:
            function_1()
        elif parcel_spawn[0] > current_position[0]:
            function_2()
        if parcel_spawn[1] < current_position[1]:
            function_3()
        elif parcel_spawn[1] > current_position[1]:
            function_4()
        current_position = belief_set['agent'][1]['coordinates']
    function_5()
    while current_position != delivery_cell:
        if delivery_cell[0] < current_position[0]:
            function_1()
        elif delivery_cell[0] > current_position[0]:
            function_2()
        if delivery_cell[1] < current_position[1]:
            function_3()
        elif delivery_cell[1] > current_position[1]:
            function_4()
        current_position = belief_set['agent'][1]['coordinates']
    function_6()
