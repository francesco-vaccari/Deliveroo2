def function_19():
    global belief_set
    delivery_cell = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] in ['delivery_cell', 'double_points_delivery_cell']][0]
    agent_position = belief_set['agent']['coordinates']
    parcel_carried = belief_set['agent']['parcels_carried_ids']
    if parcel_carried:
        while agent_position != delivery_cell['cell_coordinates']:
            if agent_position[0] < delivery_cell['cell_coordinates'][0]:
                function_2()
            elif agent_position[0] > delivery_cell['cell_coordinates'][0]:
                function_1()
            if agent_position[1] < delivery_cell['cell_coordinates'][1]:
                function_4()
            elif agent_position[1] > delivery_cell['cell_coordinates'][1]:
                function_3()
            if agent_position == belief_set['agent']['coordinates']:
                break
        function_6()
    else:
        function_10()
