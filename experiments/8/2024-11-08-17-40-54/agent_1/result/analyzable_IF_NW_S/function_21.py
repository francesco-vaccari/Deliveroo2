def function_21():
    global belief_set
    while belief_set['agent']['coordinates'][1] < belief_set['map']['height'
        ] - 1 and belief_set['agent']['energy'] > 30:
        function_4()
    if belief_set['agent']['energy'] <= 30:
        function_14()
