def function_22():
    global belief_set
    battery_spawn_location = [cell['cell_coordinates'] for cell in
        belief_set['map']['grid'] if cell['cell_type'] == 'batteries_spawn'][0]
    agent_location = belief_set['agent'][1]['coordinates']
    while agent_location != battery_spawn_location:
        if agent_location[0] < battery_spawn_location[0]:
            function_2()
        elif agent_location[0] > battery_spawn_location[0]:
            function_1()
        elif agent_location[1] < battery_spawn_location[1]:
            function_4()
        elif agent_location[1] > battery_spawn_location[1]:
            function_3()
        if belief_set['agent'][1]['coordinates'] == agent_location:
            break
        else:
            agent_location = belief_set['agent'][1]['coordinates']
    function_5()
