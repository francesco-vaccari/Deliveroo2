def function_12():
    global belief_set
    spawn_location = [cell['cell_coordinates'] for cell in belief_set['map'
        ]['grid'] if cell['cell_type'] == 'parcels_spawn'][0]
    delivery_location = [cell['cell_coordinates'] for cell in belief_set[
        'map']['grid'] if cell['cell_type'] == 'delivery_cell'][0]
    agent_location = belief_set['agent'][1]['coordinates']
    while agent_location != spawn_location:
        if agent_location[0] > spawn_location[0]:
            function_1()
        elif agent_location[0] < spawn_location[0]:
            function_2()
        if agent_location[1] > spawn_location[1]:
            function_3()
        elif agent_location[1] < spawn_location[1]:
            function_4()
        agent_location = belief_set['agent'][1]['coordinates']
    function_5()
    while agent_location != delivery_location:
        if agent_location[0] > delivery_location[0]:
            function_1()
        elif agent_location[0] < delivery_location[0]:
            function_2()
        if agent_location[1] > delivery_location[1]:
            function_3()
        elif agent_location[1] < delivery_location[1]:
            function_4()
        agent_location = belief_set['agent'][1]['coordinates']
    function_6()
