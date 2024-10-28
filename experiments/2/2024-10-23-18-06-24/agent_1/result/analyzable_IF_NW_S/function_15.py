def function_15():
    global belief_set
    agent = belief_set['agent']
    map_cells = belief_set['map']['grid']
    agent_coords = agent['coordinates']
    delivery_cell_coords = next(cell['cell_coordinates'] for cell in
        map_cells if cell['cell_type'] == 'delivery_cell')
    delta_x = delivery_cell_coords[0] - agent_coords[0]
    delta_y = delivery_cell_coords[1] - agent_coords[1]
    if delta_x > 0 and next(cell for cell in map_cells if cell[
        'cell_coordinates'] == [agent_coords[0] + 1, agent_coords[1]])[
        'cell_type'] == 'walkable':
        function_2()
    elif delta_x < 0 and next(cell for cell in map_cells if cell[
        'cell_coordinates'] == [agent_coords[0] - 1, agent_coords[1]])[
        'cell_type'] == 'walkable':
        function_1()
    elif delta_y > 0 and next(cell for cell in map_cells if cell[
        'cell_coordinates'] == [agent_coords[0], agent_coords[1] + 1])[
        'cell_type'] == 'walkable':
        function_4()
    elif delta_y < 0 and next(cell for cell in map_cells if cell[
        'cell_coordinates'] == [agent_coords[0], agent_coords[1] - 1])[
        'cell_type'] == 'walkable':
        function_3()
    if belief_set['key'][1]['coordinates'] == agent_coords and not agent[
        'has_key']:
        function_5()
