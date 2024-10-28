def function_17():
    global belief_set
    if not belief_set['agent'][1]['parcels_carried_ids']:
        function_9()
    if belief_set['agent'][1]['coordinates'] != [1, 3]:
        while belief_set['agent'][1]['coordinates'][1] != 3:
            function_4()
    function_14()
    while belief_set['agent'][1]['coordinates'][1] != 0:
        function_3()
