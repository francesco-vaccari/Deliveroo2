def function_20():
    global belief_set
    while belief_set['agent']['energy'] > 30:
        function_4()
    if belief_set['agent']['energy'] <= 30:
        function_14()
