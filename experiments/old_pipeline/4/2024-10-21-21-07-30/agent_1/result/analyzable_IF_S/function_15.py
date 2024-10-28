def function_15():
    global belief_set
    agt_crd = belief_set['agent']['coordinates']
    map_grid = belief_set['map']['grid']
    walkable_cells = [c['cell_coordinates'] for c in map_grid if c[
        'cell_type'] == 'walkable']
    target_crd = min(walkable_cells, key=lambda c: abs(c[0] - agt_crd[0]) +
        abs(c[1] - agt_crd[1]))
    while agt_crd != target_crd:
        if agt_crd[0] < target_crd[0]:
            function_2()
        elif agt_crd[0] > target_crd[0]:
            function_1()
        elif agt_crd[1] < target_crd[1]:
            function_4()
        elif agt_crd[1] > target_crd[1]:
            function_3()
        function_5()
        function_7()
        function_9()
        agt_crd = belief_set['agent']['coordinates']
