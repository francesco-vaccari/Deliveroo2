def function_14():
    global belief_set
    agent_coords = belief_set['agent']['coordinates']
    parcel_coords = belief_set['parcel'][1]['coordinates']
    delivery_coords = [cell['cell_coordinates'] for cell in belief_set[
        'map']['grid'] if cell['cell_type'] in ['delivery_cell',
        'double_delivery_cell']][0]
    while agent_coords != delivery_coords:
        if agent_coords[0] < delivery_coords[0]:
            function_2()
            agent_coords[0] += 1
        elif agent_coords[0] > delivery_coords[0]:
            function_1()
            agent_coords[0] -= 1
        elif agent_coords[1] < delivery_coords[1]:
            function_4()
            agent_coords[1] += 1
        elif agent_coords[1] > delivery_coords[1]:
            function_3()
            agent_coords[1] -= 1
    function_6()
