def function_14():
    global belief_set
    max_iterations = 1000
    iteration = 0
    while True:
        if iteration > max_iterations:
            break
        agent_coordinates = belief_set['agent'][1]['coordinates']
        parcel_coordinates = belief_set['parcels'][12]['coordinates']
        delivery_coordinates = [1, 3]
        if agent_coordinates == parcel_coordinates:
            function_5()
        elif agent_coordinates == delivery_coordinates:
            function_6()
            break
        else:
            function_11()
        iteration += 1
