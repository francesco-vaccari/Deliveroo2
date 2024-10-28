def function_9():
    global belief_set
    delivery_cell = next(cell for cell in belief_set['map']['grid'] if cell
        ['cell_type'] == 'delivery_cell')
    agent = belief_set['agent'][1]
    while agent['coordinates'] != delivery_cell['cell_coordinates']:
        if agent['coordinates'][0] > delivery_cell['cell_coordinates'][0]:
            function_1()
        elif agent['coordinates'][0] < delivery_cell['cell_coordinates'][0]:
            function_2()
        elif agent['coordinates'][1] > delivery_cell['cell_coordinates'][1]:
            function_3()
        else:
            function_4()
    function_6()
