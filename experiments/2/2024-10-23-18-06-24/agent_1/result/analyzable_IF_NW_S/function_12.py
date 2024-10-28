def function_12():
    global belief_set
    agent_coords = belief_set['agent']['coordinates']
    parcel_coords = belief_set['parcel'][1]['coordinates']
    delivery_coords = [x for x in belief_set['map']['grid'] if x[
        'cell_type'] == 'delivery_cell'][0]['cell_coordinates']
    while agent_coords != parcel_coords:
        if agent_coords[0] < parcel_coords[0]:
            function_2()
        elif agent_coords[0] > parcel_coords[0]:
            function_1()
        elif agent_coords[1] < parcel_coords[1]:
            function_4()
        else:
            function_3()
    function_5()
    while agent_coords != delivery_coords:
        if agent_coords[0] < delivery_coords[0]:
            function_2()
        elif agent_coords[0] > delivery_coords[0]:
            function_1()
        elif agent_coords[1] < delivery_coords[1]:
            function_4()
        else:
            function_3()
    function_6()
