def function_11():
    global belief_set
    parcels = belief_set['parcels']
    agent_location = belief_set['agent']['coordinates']
    delivery_location = [cell for cell in belief_set['map']['grid'] if cell
        ['cell_type'] == 'delivery_cell'][0]['cell_coordinates']
    closest_parcel = min(parcels.values(), key=lambda x: abs(x[
        'coordinates'][0] - agent_location[0]) + abs(x['coordinates'][1] -
        agent_location[1]))
    parcel_location = closest_parcel['coordinates']
    while agent_location != parcel_location:
        if agent_location[0] < parcel_location[0]:
            function_2()
        elif agent_location[0] > parcel_location[0]:
            function_1()
        if agent_location[1] < parcel_location[1]:
            function_4()
        elif agent_location[1] > parcel_location[1]:
            function_3()
    function_5()
    while agent_location != delivery_location:
        if agent_location[0] < delivery_location[0]:
            function_2()
        elif agent_location[0] > delivery_location[0]:
            function_1()
        if agent_location[1] < delivery_location[1]:
            function_4()
        elif agent_location[1] > delivery_location[1]:
            function_3()
    function_6()
