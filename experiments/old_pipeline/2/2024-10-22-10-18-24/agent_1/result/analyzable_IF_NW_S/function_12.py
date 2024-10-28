def function_12():
    global belief_set
    agent_coordinates = belief_set['agent']['coordinates']
    delivery_cells = [cell['cell_coordinates'] for cell in belief_set['map'
        ]['grid'] if cell['cell_type'] == 'delivery_cell']
    for cell in delivery_cells:
        if cell[0] > agent_coordinates[0]:
            return function_2()
        elif cell[0] < agent_coordinates[0]:
            return function_1()
        elif cell[1] > agent_coordinates[1]:
            return function_4()
        elif cell[1] < agent_coordinates[1]:
            return function_3()
    return function_6()
