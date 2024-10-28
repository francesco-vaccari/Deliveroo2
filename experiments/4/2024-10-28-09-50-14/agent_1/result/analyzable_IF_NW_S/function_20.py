def function_20():
    global belief_set
    max_iterations = 1000
    iteration = 0
    while iteration < max_iterations:
        iteration += 1
        previous_location = belief_set['agents'][1]['coordinates']
        if len(belief_set['agents'][1]['parcels_carried_ids']) == 0:
            function_9()
        else:
            function_18()
        if belief_set['agents'][1]['coordinates'] == previous_location:
            break
