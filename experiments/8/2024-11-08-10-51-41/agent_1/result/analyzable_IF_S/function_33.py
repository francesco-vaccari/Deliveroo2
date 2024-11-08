def function_33():
    global belief_set
    if belief_set['agent'][1]['coordinates'] == [0, 0]:
        function_6()
    elif belief_set['agent'][1]['energy'] < 20:
        function_14()
    else:
        function_13()
