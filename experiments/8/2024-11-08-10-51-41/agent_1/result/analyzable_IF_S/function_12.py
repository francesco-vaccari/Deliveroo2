def function_12():
    global belief_set
    delivery_cells = [cell['cell_coordinates'] for cell in belief_set['map'
        ]['grid'] if cell['cell_type'] == 'delivery_cell']
    agent_position = belief_set['agent'][1]['coordinates']
    agent_energy = belief_set['agent'][1]['energy']
    if agent_energy >= 5:
        for cell in delivery_cells:
            if cell[0] < agent_position[0] and belief_set['map']['grid'][
                agent_position[0] - 1][agent_position[1]]['cell_type'
                ] == 'walkable':
                function_1()
                break
            elif cell[0] > agent_position[0] and belief_set['map']['grid'][
                agent_position[0] + 1][agent_position[1]]['cell_type'
                ] == 'walkable':
                function_2()
                break
            elif cell[1] < agent_position[1] and belief_set['map']['grid'][
                agent_position[0]][agent_position[1] - 1]['cell_type'
                ] == 'walkable':
                function_3()
                break
            elif cell[1] > agent_position[1] and belief_set['map']['grid'][
                agent_position[0]][agent_position[1] + 1]['cell_type'
                ] == 'walkable':
                function_4()
                break
