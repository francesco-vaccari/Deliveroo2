def function_7():
    global belief_set
    agent_coords = belief_set['agent']['coordinates']
    if not belief_set['agent']['parcels_carried_ids']:
        parcel_coords = belief_set['parcels'][1]['coordinates']
        if agent_coords[0] < parcel_coords[0]:
            function_2()
        elif agent_coords[0] > parcel_coords[0]:
            function_1()
        elif agent_coords[1] < parcel_coords[1]:
            function_4()
        elif agent_coords[1] > parcel_coords[1]:
            function_3()
        else:
            function_5()
    else:
        delivery_coords = [cell['cell_coordinates'] for cell in belief_set[
            'map']['grid'] if 'delivery' in cell['cell_type']][0]
        if agent_coords[0] < delivery_coords[0]:
            function_2()
        elif agent_coords[0] > delivery_coords[0]:
            function_1()
        elif agent_coords[1] < delivery_coords[1]:
            function_4()
        elif agent_coords[1] > delivery_coords[1]:
            function_3()
        else:
            function_6()
