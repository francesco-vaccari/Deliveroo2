def function_11():
    global belief_set
    key_coord = belief_set['keys'][0]['coordinates']
    bat_coord = belief_set['batteries'][0]['coordinates']
    agent_coord = belief_set['agent']['coordinates']
    while belief_set['agent']['energy'] > 30:
        if agent_coord[0] < key_coord[0]:
            function_2()
        elif agent_coord[0] > key_coord[0]:
            function_1()
        elif agent_coord[1] < key_coord[1]:
            function_4()
        elif agent_coord[1] > key_coord[1]:
            function_3()
        if agent_coord == key_coord:
            function_5()
            break
    while belief_set['agent']['energy'] <= 30:
        if agent_coord[0] < bat_coord[0]:
            function_2()
        elif agent_coord[0] > bat_coord[0]:
            function_1()
        elif agent_coord[1] < bat_coord[1]:
            function_4()
        elif agent_coord[1] > bat_coord[1]:
            function_3()
        if agent_coord == bat_coord:
            function_5()
            break
