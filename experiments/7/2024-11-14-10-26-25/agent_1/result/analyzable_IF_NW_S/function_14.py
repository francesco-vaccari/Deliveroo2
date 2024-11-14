def function_14():
    global belief_set
    agent_coordinates = belief_set['agent']['coordinates']
    next_cell_coordinates = [agent_coordinates[0] - 1, agent_coordinates[1]]
    next_cell = next((cell for cell in belief_set['map']['grid'] if cell[
        'cell_coordinates'] == next_cell_coordinates), None)
    if next_cell and next_cell['cell_type'] == 'walkable':
        function_1()
