def function_19():
    global belief_set
    agent = belief_set['agent'][1]
    door = belief_set['doors'][1]
    agent_coordinates = agent['coordinates']
    door_coordinates = door['coordinates']
    while agent_coordinates != door_coordinates:
        if agent_coordinates[0] < door_coordinates[0]:
            function_2()
            agent_coordinates[0] += 1
        elif agent_coordinates[0] > door_coordinates[0]:
            function_1()
            agent_coordinates[0] -= 1
        if agent_coordinates[1] < door_coordinates[1]:
            function_4()
            agent_coordinates[1] += 1
        elif agent_coordinates[1] > door_coordinates[1]:
            function_3()
            agent_coordinates[1] -= 1
