def function_9():
    global belief_set
    agent_location = belief_set['agent']['coordinates']
    parcel_location = belief_set['parcel'][1]['coordinates']
    delivery_location = [cell['cell_coordinates'] for cell in belief_set[
        'map']['grid'] if 'delivery' in cell['cell_type']][0]
    if agent_location[0] < delivery_location[0]:
        function_2()
    elif agent_location[0] > delivery_location[0]:
        function_1()
    elif agent_location[1] < delivery_location[1]:
        function_4()
    elif agent_location[1] > delivery_location[1]:
        function_3()
    else:
        function_6()
