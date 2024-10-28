def function_7():
    global belief_set
    target = belief_set['parcel'][1]['coordinates']
    agent_position = belief_set['agent'][1]['coordinates']
    while agent_position != target:
        if agent_position[0] < target[0] and belief_set['map']['grid'][
            agent_position[0] + 1][agent_position[1]]['cell_type'
            ] == 'walkable':
            function_2()
        elif agent_position[0] > target[0] and belief_set['map']['grid'][
            agent_position[0] - 1][agent_position[1]]['cell_type'
            ] == 'walkable':
            function_1()
        elif agent_position[1] < target[1] and belief_set['map']['grid'][
            agent_position[0]][agent_position[1] + 1]['cell_type'
            ] == 'walkable':
            function_4()
        elif agent_position[1] > target[1] and belief_set['map']['grid'][
            agent_position[0]][agent_position[1] - 1]['cell_type'
            ] == 'walkable':
            function_3()
    function_5()
