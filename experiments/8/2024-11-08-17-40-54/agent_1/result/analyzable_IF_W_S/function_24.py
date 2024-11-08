def function_24():
    global belief_set
    if belief_set['agent']['energy'] > 50:
        new_coordinates = [belief_set['agent']['coordinates'][0] + 1,
            belief_set['agent']['coordinates'][1]]
        for cell in belief_set['map']['grid']:
            if cell['cell_coordinates'] == new_coordinates and cell['cell_type'
                ] == 'walkable':
                function_2()
                break
