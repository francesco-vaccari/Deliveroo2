def function_15():
    global belief_set
    max_attempts = 100
    attempts = 0
    while not belief_set['agents'][1]['has_key'] and attempts < max_attempts:
        function_9()
        function_5()
        attempts += 1
    if belief_set['agents'][1]['has_key']:
        while belief_set['doors'] and attempts < max_attempts:
            function_9()
            attempts += 1
    else:
        while belief_set['parcels'] and attempts < max_attempts:
            function_9()
            attempts += 1
