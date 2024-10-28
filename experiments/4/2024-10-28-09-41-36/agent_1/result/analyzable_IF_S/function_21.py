def function_21():
    global belief_set
    keys = belief_set['keys']
    agent_position = belief_set['agent']['coordinates']
    for key_id, key_details in keys.items():
        if key_details['carried_by_id'] is None:
            key_position = key_details['coordinates']
            while agent_position != key_position:
                if agent_position[0] < key_position[0]:
                    function_2()
                elif agent_position[0] > key_position[0]:
                    function_1()
                if agent_position[1] < key_position[1]:
                    function_4()
                elif agent_position[1] > key_position[1]:
                    function_3()
            function_5()
            break
