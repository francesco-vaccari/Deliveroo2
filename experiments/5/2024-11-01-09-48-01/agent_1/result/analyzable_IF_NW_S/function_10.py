def function_10():
    global belief_set
    max_moves = 100
    moves = 0
    while moves < max_moves:
        if belief_set['agent'][1]['coordinates'] == [0, 0]:
            function_5()
            moves += 1
        elif belief_set['agent'][1]['coordinates'][1] > 0:
            function_3()
            moves += 1
        elif belief_set['agent'][1]['coordinates'][0] > 0:
            function_1()
            moves += 1
        elif belief_set['agent'][1]['coordinates'] == [1, 3]:
            function_6()
            moves += 1
        elif belief_set['agent'][1]['coordinates'][1] < 3:
            function_4()
            moves += 1
        elif belief_set['agent'][1]['coordinates'][0] < 1:
            function_2()
            moves += 1
    if moves == max_moves:
        return 'Max moves reached, goal not achieved'
