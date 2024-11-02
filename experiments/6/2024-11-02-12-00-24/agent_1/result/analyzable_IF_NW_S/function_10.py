def function_10():
    global belief_set
    current_position = belief_set['agent']['coordinates']
    parcels_position = belief_set['map']['grid'][0]['cell_coordinates']
    batteries_position = belief_set['map']['grid'][8]['cell_coordinates']
    energy = belief_set['agent']['energy']
    if energy < 30:
        if current_position[0] > batteries_position[0]:
            function_1()
        elif current_position[0] < batteries_position[0]:
            function_2()
        elif current_position[1] > batteries_position[1]:
            function_3()
        elif current_position[1] < batteries_position[1]:
            function_4()
    else:
        if current_position[0] > parcels_position[0]:
            function_1()
        elif current_position[0] < parcels_position[0]:
            function_2()
        elif current_position[1] > parcels_position[1]:
            function_3()
        elif current_position[1] < parcels_position[1]:
            function_4()
        if current_position == parcels_position:
            function_5()
