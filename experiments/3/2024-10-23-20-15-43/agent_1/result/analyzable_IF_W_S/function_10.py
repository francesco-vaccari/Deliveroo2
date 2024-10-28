def function_10():
    global belief_set
    key_positions = [key['coordinates'] for key in belief_set['keys'].
        values() if key['carried_by_id'] is None]
    agent_position = belief_set['agent']['coordinates']
    nearest_key_position = min(key_positions, key=lambda pos: abs(pos[0] -
        agent_position[0]) + abs(pos[1] - agent_position[1]))
    while agent_position != nearest_key_position:
        if agent_position[0] < nearest_key_position[0]:
            function_2()
        elif agent_position[0] > nearest_key_position[0]:
            function_1()
        elif agent_position[1] < nearest_key_position[1]:
            function_4()
        elif agent_position[1] > nearest_key_position[1]:
            function_3()
        agent_position = belief_set['agent']['coordinates']
    function_5()
