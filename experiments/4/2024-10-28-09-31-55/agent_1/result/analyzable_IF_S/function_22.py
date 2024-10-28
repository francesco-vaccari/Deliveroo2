def function_22():
    global belief_set
    step_counter = 0
    max_steps = 100
    agent_pos = belief_set['agent']['coordinates']
    delivery_cells = [cell['cell_coordinates'] for cell in belief_set['map'
        ]['grid'] if 'delivery' in cell['cell_type']]
    while step_counter < max_steps and agent_pos not in delivery_cells:
        function_8()
        step_counter += 1
        agent_pos = belief_set['agent']['coordinates']
    if agent_pos in delivery_cells:
        function_6()
    else:
        function_20()
        function_10()
