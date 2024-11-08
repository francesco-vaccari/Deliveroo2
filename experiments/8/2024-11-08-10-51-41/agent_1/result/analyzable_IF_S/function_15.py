def function_15():
    global belief_set
    agent_coordinates = belief_set['agent'][1]['coordinates']
    battery_spawn_coordinates = [cell['cell_coordinates'] for cell in
        belief_set['map']['grid'] if cell['cell_type'] == 'batteries_spawn'][0]
    x_diff = battery_spawn_coordinates[0] - agent_coordinates[0]
    y_diff = battery_spawn_coordinates[1] - agent_coordinates[1]
    if x_diff > 0:
        function_2()
    elif x_diff < 0:
        function_1()
    elif y_diff > 0:
        function_4()
    elif y_diff < 0:
        function_3()
    if agent_coordinates == battery_spawn_coordinates:
        function_5()
