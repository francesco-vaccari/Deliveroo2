def function_9():
    global belief_set
    agent_position = belief_set['agent']['coordinates']
    nearest_door = min(belief_set['doors'].values(), key=lambda d: abs(d[
        'coordinates'][0] - agent_position[0]) + abs(d['coordinates'][1] -
        agent_position[1]))
    path = [cell for cell in belief_set['map']['grid'] if 'walkable' in
        cell['cell_type']]
    if nearest_door['coordinates'] in [cell['cell_coordinates'] for cell in
        path]:
        while agent_position != nearest_door['coordinates']:
            if agent_position[0] > nearest_door['coordinates'][0]:
                function_1()
                agent_position[0] -= 1
            elif agent_position[0] < nearest_door['coordinates'][0]:
                function_2()
                agent_position[0] += 1
            if agent_position[1] > nearest_door['coordinates'][1]:
                function_3()
                agent_position[1] -= 1
            elif agent_position[1] < nearest_door['coordinates'][1]:
                function_4()
                agent_position[1] += 1
