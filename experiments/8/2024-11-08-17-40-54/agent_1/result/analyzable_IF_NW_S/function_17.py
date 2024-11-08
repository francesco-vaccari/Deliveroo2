def function_17():
    global belief_set
    agent_coordinates = belief_set['agent']['coordinates']
    map_grid = belief_set['map']['grid']
    unexplored_cells = [cell for cell in map_grid if cell['cell_type'] ==
        'walkable' and cell['cell_coordinates'] not in belief_set['agent'][
        'visited_cells']]
    if belief_set['agent']['energy'] > 10:
        if unexplored_cells:
            next_cell = unexplored_cells[0]
            if next_cell['cell_coordinates'][0] < agent_coordinates[0]:
                function_1()
            elif next_cell['cell_coordinates'][0] > agent_coordinates[0]:
                function_2()
            elif next_cell['cell_coordinates'][1] < agent_coordinates[1]:
                function_3()
            else:
                function_4()
        else:
            function_5()
    else:
        function_14()
