def function_9():
    global belief_set
    max_iterations = 100
    i = 0
    agent = belief_set['agents'][1]
    delivery_cell = [3, 0]
    while i < max_iterations and agent['coordinates'] != delivery_cell:
        if agent['coordinates'][0] < delivery_cell[0]:
            function_2()
            agent['coordinates'][0] += 1
        elif agent['coordinates'][0] > delivery_cell[0]:
            function_1()
            agent['coordinates'][0] -= 1
        elif agent['coordinates'][1] < delivery_cell[1]:
            function_4()
            agent['coordinates'][1] += 1
        elif agent['coordinates'][1] > delivery_cell[1]:
            function_3()
            agent['coordinates'][1] -= 1
        i += 1
    if agent['coordinates'] == delivery_cell:
        function_6()
    return
