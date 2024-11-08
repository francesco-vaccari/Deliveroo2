def function_10():
    global belief_set
    agent = belief_set['agent'][1]
    map = belief_set['map']['grid']
    walkable_cells = [cell for cell in map if cell['cell_type'] == 'walkable']
    current_coordinates = agent['coordinates']
    nearest_walkable_cell = min(walkable_cells, key=lambda cell: abs(cell[
        'cell_coordinates'][0] - current_coordinates[0]) + abs(cell[
        'cell_coordinates'][1] - current_coordinates[1]))
    target_coordinates = nearest_walkable_cell['cell_coordinates']
    while agent['coordinates'] != target_coordinates:
        if agent['coordinates'][0] < target_coordinates[0]:
            function_2()
            agent['coordinates'][0] += 1
        elif agent['coordinates'][0] > target_coordinates[0]:
            function_1()
            agent['coordinates'][0] -= 1
        if agent['coordinates'][1] < target_coordinates[1]:
            function_4()
            agent['coordinates'][1] += 1
        elif agent['coordinates'][1] > target_coordinates[1]:
            function_3()
            agent['coordinates'][1] -= 1
    function_6()
