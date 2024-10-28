def function_7():
    global belief_set
    agent_pos = belief_set['agent']['coordinates']
    key_pos = belief_set['keys'][1]['coordinates']
    while agent_pos != key_pos:
        if agent_pos[0] > key_pos[0]:
            function_1()
        elif agent_pos[0] < key_pos[0]:
            function_2()
        if agent_pos[1] > key_pos[1]:
            function_3()
        elif agent_pos[1] < key_pos[1]:
            function_4()
    function_5()

def function_10():
    global belief_set
    agent_coord = belief_set['agent']['coordinates']
    keys = belief_set['keys']
    for key in keys.values():
        if key['coordinates'] == agent_coord and key['carried_by_id'] is None:
            function_5()
            break
    if agent_coord[0] > 0 and belief_set['map']['grid'][agent_coord[0] - 1][
        agent_coord[1]]['cell_type'] == 'walkable':
        function_1()
    elif agent_coord[0] < belief_set['map']['width'] - 1 and belief_set['map'][
        'grid'][agent_coord[0] + 1][agent_coord[1]]['cell_type'] == 'walkable':
        function_2()
    elif agent_coord[1] > 0 and belief_set['map']['grid'][agent_coord[0]][
        agent_coord[1] - 1]['cell_type'] == 'walkable':
        function_3()
    elif agent_coord[1] < belief_set['map']['height'] - 1 and belief_set['map'
        ]['grid'][agent_coord[0]][agent_coord[1] + 1]['cell_type'
        ] == 'walkable':
        function_4()

