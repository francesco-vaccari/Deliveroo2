def function_14():
    global belief_set
    delivery_cells = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'delivery_cell']
    agent = belief_set['agent'][1]
    if agent['coordinates'] in [cell['cell_coordinates'] for cell in
        delivery_cells]:
        function_6()
    else:
        function_13()
