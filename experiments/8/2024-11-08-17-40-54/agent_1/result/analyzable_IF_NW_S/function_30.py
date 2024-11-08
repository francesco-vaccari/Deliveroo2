def function_30():
    global belief_set
    if belief_set['agent']['has_key']:
        for door in belief_set['doors'].values():
            if door['coordinates'] == belief_set['agent']['coordinates']:
                function_5()
    elif belief_set['agent']['energy'] < 50:
        function_29()
    else:
        function_24()
