def function_17():
    global belief_set
    agent = belief_set['agent'][1]
    if agent['energy'] < 50:
        function_14()
    elif agent['coordinates'][0] + 1 < belief_set['map']['width'] and {
        'cell_coordinates': [agent['coordinates'][0] + 1, agent[
        'coordinates'][1]], 'cell_type': 'walkable'} in belief_set['map'][
        'grid']:
        function_2()
    elif agent['coordinates'][0] - 1 >= 0 and {'cell_coordinates': [agent[
        'coordinates'][0] - 1, agent['coordinates'][1]], 'cell_type':
        'walkable'} in belief_set['map']['grid']:
        function_1()
    elif agent['coordinates'][1] + 1 < belief_set['map']['height'] and {
        'cell_coordinates': [agent['coordinates'][0], agent['coordinates'][
        1] + 1], 'cell_type': 'walkable'} in belief_set['map']['grid']:
        function_4()
    elif agent['coordinates'][1] - 1 >= 0 and {'cell_coordinates': [agent[
        'coordinates'][0], agent['coordinates'][1] - 1], 'cell_type':
        'walkable'} in belief_set['map']['grid']:
        function_3()
