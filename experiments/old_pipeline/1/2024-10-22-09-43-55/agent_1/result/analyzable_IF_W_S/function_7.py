def function_7():
    global belief_set
    spawn_point = [cell['cell_coordinates'] for cell in belief_set['map'][
        'grid'] if cell['cell_type'] == 'parcels_spawn'][0]
    agent_position = belief_set['agent']['coordinates']
    while agent_position != spawn_point:
        if agent_position[0] > spawn_point[0]:
            function_1()
        elif agent_position[0] < spawn_point[0]:
            function_2()
        elif agent_position[1] > spawn_point[1]:
            function_3()
        else:
            function_4()
        agent_position = belief_set['agent']['coordinates']
    function_5()
