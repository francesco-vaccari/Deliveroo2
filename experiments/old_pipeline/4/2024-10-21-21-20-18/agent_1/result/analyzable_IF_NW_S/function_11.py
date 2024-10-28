def function_11():
    global belief_set
    agent = belief_set['agent']
    grid = belief_set['map']['grid']
    delivery_cells = [cell for cell in grid if cell['cell_type'] in [
        'delivery_cell', 'double_delivery_cell']]
    for cell in delivery_cells:
        if cell['cell_coordinates'][0] > agent['coordinates'][0]:
            function_2()
        elif cell['cell_coordinates'][0] < agent['coordinates'][0]:
            function_1()
        elif cell['cell_coordinates'][1] > agent['coordinates'][1]:
            function_4()
        elif cell['cell_coordinates'][1] < agent['coordinates'][1]:
            function_3()
        else:
            function_6()
