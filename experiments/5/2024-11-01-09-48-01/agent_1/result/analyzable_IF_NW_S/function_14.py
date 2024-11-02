def function_14():
    global belief_set
    max_iterations = 100
    iteration = 0
    while iteration < max_iterations:
        function_8()
        if belief_set['agent'][1]['parcels_carried_ids']:
            function_6()
        iteration += 1
