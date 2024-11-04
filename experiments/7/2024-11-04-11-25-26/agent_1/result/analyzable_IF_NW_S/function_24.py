def function_24():
    global belief_set
    while True:
        if belief_set['agent'][1]['energy'] < 50:
            function_21()
        elif len(belief_set['agent'][1]['parcels_carried_ids']) == 0:
            function_17()
        else:
            function_19()
        if belief_set['agent'][1]['score'] == belief_set['agent'][1]['score']:
            break
