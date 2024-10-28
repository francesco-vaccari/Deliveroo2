def function_10():
    global belief_set
    if belief_set['agent'][1]['parcels_carried_ids']:
        function_2()
        if not belief_set['agent'][1]['parcels_carried_ids']:
            function_5()
    else:
        function_5()
        function_2()
    if belief_set['doors'][1]['coordinates'] == belief_set['agent'][1][
        'coordinates'] and belief_set['agent'][1]['has_key']:
        function_8()
    else:
        function_2()
