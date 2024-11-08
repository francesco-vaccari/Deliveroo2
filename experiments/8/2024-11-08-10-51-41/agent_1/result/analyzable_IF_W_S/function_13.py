def function_13():
    global belief_set
    delivery_cells = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'delivery_cell']
    delivery_cells.sort(key=lambda x: abs(x['cell_coordinates'][0] -
        belief_set['agent'][1]['coordinates'][0]) + abs(x[
        'cell_coordinates'][1] - belief_set['agent'][1]['coordinates'][1]))
    for cell in delivery_cells:
        dx = cell['cell_coordinates'][0] - belief_set['agent'][1]['coordinates'
            ][0]
        dy = cell['cell_coordinates'][1] - belief_set['agent'][1]['coordinates'
            ][1]
        if dx < 0 and belief_set['agent'][1]['energy'] >= 5:
            function_1()
            break
        elif dx > 0 and belief_set['agent'][1]['energy'] >= 5:
            function_2()
            break
        elif dy < 0 and belief_set['agent'][1]['energy'] >= 5:
            function_3()
            break
        elif dy > 0 and belief_set['agent'][1]['energy'] >= 5:
            function_4()
            break
