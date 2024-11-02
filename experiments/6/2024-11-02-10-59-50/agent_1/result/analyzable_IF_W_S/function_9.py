def function_9():
    global belief_set
    agent = belief_set['agent'][1]
    target_cell = None
    for cell in belief_set['map']['grid']:
        if cell['cell_type'] == 'parcels_spawn':
            target_cell = cell['cell_coordinates']
    if target_cell is None:
        return
    x_diff = target_cell[0] - agent['coordinates'][0]
    y_diff = target_cell[1] - agent['coordinates'][1]
    attempt_count = 0
    while agent['coordinates'] != target_cell and attempt_count < 100:
        if x_diff > 0:
            function_2()
            x_diff -= 1
        elif x_diff < 0:
            function_1()
            x_diff += 1
        if y_diff > 0:
            function_4()
            y_diff -= 1
        elif y_diff < 0:
            function_3()
            y_diff += 1
        attempt_count += 1
