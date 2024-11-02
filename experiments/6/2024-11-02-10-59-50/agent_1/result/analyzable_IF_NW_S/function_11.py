def function_11():
    global belief_set
    agent_coordinates = belief_set['agent'][1]['coordinates']
    for cell in belief_set['map']['grid']:
        if cell['cell_type'] == 'parcels_spawn':
            spawn_coordinates = cell['cell_coordinates']
            break
    if agent_coordinates == spawn_coordinates:
        function_5()
    else:
        function_9()
