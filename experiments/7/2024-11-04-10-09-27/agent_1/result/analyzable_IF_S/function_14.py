def function_14():
    global belief_set
    agent = belief_set['agent'][1]
    if agent['energy'] < 30:
        pass
    else:
        if agent['parcels_carried_ids']:
            function_10()
        else:
            function_11()
        pass
