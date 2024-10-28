def function_11():
    global belief_set
    agent = belief_set['agents'][1]
    delivery_cells = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] in ['delivery_cell', 'double_delivery_cell']]
    for cell in delivery_cells:
        if agent['coordinates'][0] < cell['cell_coordinates'][0]:
            function_2()
        elif agent['coordinates'][0] > cell['cell_coordinates'][0]:
            function_1()
        elif agent['coordinates'][1] < cell['cell_coordinates'][1]:
            function_4()
        elif agent['coordinates'][1] > cell['cell_coordinates'][1]:
            function_3()
    function_6()
