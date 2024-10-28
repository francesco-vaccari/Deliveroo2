def function_13():
    global belief_set
    delivery_cells = [cell for cell in belief_set['map']['grid'] if 
        'delivery' in cell['cell_type']]
    agent_coordinates = belief_set['agents'][1]['coordinates']
    nearest_delivery_cell = None
    min_distance = float('inf')
    for cell in delivery_cells:
        distance = abs(cell['cell_coordinates'][0] - agent_coordinates[0]
            ) + abs(cell['cell_coordinates'][1] - agent_coordinates[1])
        if distance < min_distance:
            min_distance = distance
            nearest_delivery_cell = cell
    delta_x = nearest_delivery_cell['cell_coordinates'][0] - agent_coordinates[
        0]
    delta_y = nearest_delivery_cell['cell_coordinates'][1] - agent_coordinates[
        1]
    if delta_x < 0:
        for _ in range(abs(delta_x)):
            function_1()
    elif delta_x > 0:
        for _ in range(delta_x):
            function_2()
    if delta_y < 0:
        for _ in range(abs(delta_y)):
            function_3()
    elif delta_y > 0:
        for _ in range(delta_y):
            function_4()
    function_6()
