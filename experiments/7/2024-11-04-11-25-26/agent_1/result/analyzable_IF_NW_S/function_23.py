def function_23():
    global belief_set
    counter = 0
    while True:
        counter += 1
        if counter > 100:
            break
        if belief_set['agent'][1]['energy'] < 50:
            function_21()
            continue
        if len(belief_set['agent'][1]['parcels_carried_ids']) > 0:
            function_19()
        else:
            function_17()
