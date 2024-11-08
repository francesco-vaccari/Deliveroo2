def function_13():
    global belief_set
    agent = belief_set['agent'][1]
    battery = belief_set['batteries'][1]
    x_distance = battery['coordinates'][0] - agent['coordinates'][0]
    y_distance = battery['coordinates'][1] - agent['coordinates'][1]
    iterations = 0
    max_iterations = 10
    while agent['coordinates'] != battery['coordinates'
        ] and iterations < max_iterations:
        if x_distance > 0:
            function_2()
            x_distance -= 1
        elif x_distance < 0:
            function_1()
            x_distance += 1
        if y_distance > 0:
            function_4()
            y_distance -= 1
        elif y_distance < 0:
            function_3()
            y_distance += 1
        iterations += 1
    function_5()
