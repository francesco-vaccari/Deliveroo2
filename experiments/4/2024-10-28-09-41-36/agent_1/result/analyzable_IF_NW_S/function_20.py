def function_20():
    global belief_set
    current_position = belief_set['agent']['coordinates']
    parcels_carried = belief_set['agent']['parcels_carried_ids']
    if parcels_carried:
        delivery_cell = next((cell['cell_coordinates'] for cell in
            belief_set['map']['grid'] if cell['cell_type'] in [
            'delivery_cell', 'double_points_delivery_cell']), None)
        if delivery_cell:
            previous_position = current_position
            while current_position != delivery_cell:
                if current_position[0] < delivery_cell[0]:
                    function_2()
                elif current_position[0] > delivery_cell[0]:
                    function_1()
                elif current_position[1] < delivery_cell[1]:
                    function_4()
                elif current_position[1] > delivery_cell[1]:
                    function_3()
                if current_position == previous_position:
                    break
                previous_position = current_position
            function_6()
    else:
        function_9()
