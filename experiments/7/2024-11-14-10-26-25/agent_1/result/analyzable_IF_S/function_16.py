def function_16():
    global belief_set
    agent = belief_set['agent']
    delivery_cell = next(cell for cell in belief_set['map']['grid'] if cell
        ['cell_type'] == 'delivery_cell')
    while agent['coordinates'] != delivery_cell['cell_coordinates']:
        if agent['coordinates'][0] < delivery_cell['cell_coordinates'][0]:
            function_2()
        elif agent['coordinates'][0] > delivery_cell['cell_coordinates'][0]:
            function_1()
        elif agent['coordinates'][1] < delivery_cell['cell_coordinates'][1]:
            function_4()
        elif agent['coordinates'][1] > delivery_cell['cell_coordinates'][1]:
            function_3()
    function_6()
