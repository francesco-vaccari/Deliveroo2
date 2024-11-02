def function_14():
    global belief_set
    agent = belief_set['agent'][1]
    if agent['energy'] < 50:
        function_2()
    else:
        function_12()
