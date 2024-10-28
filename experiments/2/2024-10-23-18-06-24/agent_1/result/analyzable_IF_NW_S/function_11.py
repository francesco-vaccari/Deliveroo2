def function_11():
    global belief_set
    delivery_cell = [cell['cell_coordinates'] for cell in belief_set['map']
        ['grid'] if cell['cell_type'] == 'delivery_cell'][0]
    agent_coordinates = belief_set['agent']['coordinates']
    max_attempts = 10
    attempts = 0
    while agent_coordinates != delivery_cell and attempts < max_attempts:
        if agent_coordinates[0] < delivery_cell[0]:
            if {'cell_coordinates': [agent_coordinates[0] + 1,
                agent_coordinates[1]], 'cell_type': 'non_walkable'
                } not in belief_set['map']['grid']:
                function_2()
        elif agent_coordinates[0] > delivery_cell[0]:
            if {'cell_coordinates': [agent_coordinates[0] - 1,
                agent_coordinates[1]], 'cell_type': 'non_walkable'
                } not in belief_set['map']['grid']:
                function_1()
        if agent_coordinates[1] < delivery_cell[1]:
            if {'cell_coordinates': [agent_coordinates[0], 
                agent_coordinates[1] + 1], 'cell_type': 'non_walkable'
                } not in belief_set['map']['grid']:
                function_4()
        elif agent_coordinates[1] > delivery_cell[1]:
            if {'cell_coordinates': [agent_coordinates[0], 
                agent_coordinates[1] - 1], 'cell_type': 'non_walkable'
                } not in belief_set['map']['grid']:
                function_3()
        attempts += 1
    function_6()
    return
