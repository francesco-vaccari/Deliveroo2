def function_10():
    global belief_set
    function_7()
    for cell in belief_set['map']['grid']:
        if cell['cell_coordinates'] == belief_set['agent'][1]['coordinates'
            ] and 'spawn' in cell['cell_type']:
            function_5()
    return
