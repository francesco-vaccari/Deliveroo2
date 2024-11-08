def function_27():
    global belief_set
    x, y = belief_set['agent']['coordinates']
    if belief_set['agent']['energy'] > 50:
        if belief_set['map']['grid'][y][x - 1]['cell_type'] == 'walkable':
            function_1()
        if belief_set['map']['grid'][y - 1][x]['cell_type'] == 'walkable':
            function_3()
        if belief_set['map']['grid'][y][x + 1]['cell_type'] == 'walkable':
            function_2()
        if belief_set['map']['grid'][y + 1][x]['cell_type'] == 'walkable':
            function_4()
