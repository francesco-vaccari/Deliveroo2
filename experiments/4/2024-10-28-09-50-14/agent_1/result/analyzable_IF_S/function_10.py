def function_10():
    global belief_set
    agent_location = belief_set['agents'][1]['coordinates']
    delivery_cells = [cell['cell_coordinates'] for cell in belief_set['map'
        ]['grid'] if 'delivery' in cell['cell_type']]
    delivery_cells.sort(key=lambda x: abs(x[0] - agent_location[0]) + abs(x
        [1] - agent_location[1]))
    target_cell = delivery_cells[0]
    if agent_location[0] < target_cell[0]:
        function_2()
    elif agent_location[0] > target_cell[0]:
        function_1()
    elif agent_location[1] < target_cell[1]:
        function_4()
    elif agent_location[1] > target_cell[1]:
        function_3()
    else:
        function_6()
