def function_15():
    global belief_set
    agent_coordinates = belief_set['agent'][1]['coordinates']
    delivery_coordinates = [1, 3]
    iteration_counter = 0
    while (agent_coordinates != delivery_coordinates and iteration_counter <
        100):
        if agent_coordinates[0] < delivery_coordinates[0]:
            function_2()
        elif agent_coordinates[0] > delivery_coordinates[0]:
            function_1()
        if agent_coordinates[1] < delivery_coordinates[1]:
            function_4()
        elif agent_coordinates[1] > delivery_coordinates[1]:
            function_3()
        iteration_counter += 1
        if iteration_counter == 99:
            break
    function_5()
    while (agent_coordinates != delivery_coordinates and iteration_counter <
        200):
        if agent_coordinates[0] < delivery_coordinates[0]:
            function_2()
        elif agent_coordinates[0] > delivery_coordinates[0]:
            function_1()
        if agent_coordinates[1] < delivery_coordinates[1]:
            function_4()
        elif agent_coordinates[1] > delivery_coordinates[1]:
            function_3()
        iteration_counter += 1
        if iteration_counter == 199:
            break
    function_6()
