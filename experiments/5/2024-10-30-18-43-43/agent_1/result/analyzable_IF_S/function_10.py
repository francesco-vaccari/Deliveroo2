def function_10():
    global belief_set
    parcel_spawn = [item for item in belief_set['map']['grid'] if item[
        'cell_type'] == 'parcels_spawn'][0]['cell_coordinates']
    delivery_cell = [item for item in belief_set['map']['grid'] if item[
        'cell_type'] == 'delivery_cell'][0]['cell_coordinates']
    agent_location = belief_set['agent'][1]['coordinates']
    while agent_location != parcel_spawn:
        if parcel_spawn[0] < agent_location[0]:
            function_1()
        elif parcel_spawn[0] > agent_location[0]:
            function_2()
        elif parcel_spawn[1] < agent_location[1]:
            function_3()
        elif parcel_spawn[1] > agent_location[1]:
            function_4()
    function_5()
    while agent_location != delivery_cell:
        if delivery_cell[0] < agent_location[0]:
            function_1()
        elif delivery_cell[0] > agent_location[0]:
            function_2()
        elif delivery_cell[1] < agent_location[1]:
            function_3()
        elif delivery_cell[1] > agent_location[1]:
            function_4()
    function_6()
