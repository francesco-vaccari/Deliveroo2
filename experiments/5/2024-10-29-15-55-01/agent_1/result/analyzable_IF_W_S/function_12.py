def function_12():
    global belief_set
    agent = belief_set['agent'][1]
    map_grid = belief_set['map']['grid']
    agent_x, agent_y = agent['coordinates']
    walkable_cells = [cell for cell in map_grid if cell['cell_type'] ==
        'walkable']
    nearest_walkable_cell = min(walkable_cells, key=lambda cell: abs(cell[
        'cell_coordinates'][0] - agent_x) + abs(cell['cell_coordinates'][1] -
        agent_y))
    if nearest_walkable_cell['cell_coordinates'][0] < agent_x:
        function_1()
    elif nearest_walkable_cell['cell_coordinates'][0] > agent_x:
        function_2()
    elif nearest_walkable_cell['cell_coordinates'][1] < agent_y:
        function_3()
    elif nearest_walkable_cell['cell_coordinates'][1] > agent_y:
        function_4()
