def function_26():
    global belief_set
    agent = belief_set['agent'][1]
    if agent['energy'] < 30:
        function_16()
    else:
        parcels = belief_set['parcels']
        keys = belief_set['keys']
        if parcels or keys:
            function_5()
        else:
            function_11()
