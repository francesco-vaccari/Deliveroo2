def function_19():
    global belief_set
    agent_coords = belief_set['agent']['coordinates']
    if belief_set['agent']['energy'] > 50:
        if agent_coords[0] > 0 and belief_set['map']['grid'][agent_coords[0
            ] - 1][agent_coords[1]]['cell_type'] == 'walkable':
            function_1()
        elif agent_coords[0] < belief_set['map']['width'] - 1 and belief_set[
            'map']['grid'][agent_coords[0] + 1][agent_coords[1]]['cell_type'
            ] == 'walkable':
            function_2()
        elif agent_coords[1] > 0 and belief_set['map']['grid'][agent_coords[0]
            ][agent_coords[1] - 1]['cell_type'] == 'walkable':
            function_3()
        elif agent_coords[1] < belief_set['map']['height'] - 1 and belief_set[
            'map']['grid'][agent_coords[0]][agent_coords[1] + 1]['cell_type'
            ] == 'walkable':
            function_4()
    else:
        pass
