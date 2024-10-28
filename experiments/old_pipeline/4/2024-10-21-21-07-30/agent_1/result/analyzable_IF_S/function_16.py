def function_16():
    global belief_set
    agent_position = belief_set['agent']['coordinates']
    parcel_position = belief_set['parcel'][1]['coordinates']
    delivery_cell_position = [cell['cell_coordinates'] for cell in
        belief_set['map']['grid'] if cell['cell_type'] in [
        'double_delivery_cell', 'delivery_cell']][0]
    while agent_position != parcel_position:
        if agent_position[0] < parcel_position[0]:
            function_2()
        elif agent_position[0] > parcel_position[0]:
            function_1()
        elif agent_position[1] < parcel_position[1]:
            function_4()
        elif agent_position[1] > parcel_position[1]:
            function_3()
    function_5()
    while agent_position != delivery_cell_position:
        if agent_position[0] < delivery_cell_position[0]:
            function_2()
        elif agent_position[0] > delivery_cell_position[0]:
            function_1()
        elif agent_position[1] < delivery_cell_position[1]:
            function_4()
        elif agent_position[1] > delivery_cell_position[1]:
            function_3()
    function_6()
