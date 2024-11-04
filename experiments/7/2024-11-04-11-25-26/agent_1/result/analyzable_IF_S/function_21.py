def function_21():
    global belief_set
    battery_spawn = [cell['cell_coordinates'] for cell in belief_set['map']
        ['grid'] if cell['cell_type'] == 'batteries_spawn'][0]
    agent_pos = belief_set['agent'][1]['coordinates']
    while True:
        if agent_pos[0] > battery_spawn[0]:
            function_1()
        elif agent_pos[0] < battery_spawn[0]:
            function_2()
        elif agent_pos[1] > battery_spawn[1]:
            function_3()
        elif agent_pos[1] < battery_spawn[1]:
            function_4()
        agent_pos = belief_set['agent'][1]['coordinates']
        if agent_pos == battery_spawn:
            function_5()
            break
