def function_26():
    global belief_set
    agent_coordinates = belief_set['agent']['coordinates']
    agent_energy = belief_set['agent']['energy']
    map_grid = belief_set['map']['grid']
    if agent_energy > 50:
        for cell in map_grid:
            if cell['cell_coordinates'] == [agent_coordinates[0], 
                agent_coordinates[1] + 1] and cell['cell_type'] == 'walkable':
                function_4()
                function_5()
                break
