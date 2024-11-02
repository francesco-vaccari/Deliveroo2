def function_21():
    global belief_set
    function_20()
    agent = belief_set['agent'][1]
    if agent['energy'] < 50:
        for cell in belief_set['map']['grid']:
            if cell['cell_type'] == 'batteries_spawn' and cell[
                'cell_coordinates'] == agent['coordinates']:
                function_5()
    function_11()
