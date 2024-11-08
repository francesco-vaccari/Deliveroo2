def function_10():
    global belief_set
    agent = belief_set['agent'][1]
    delivery_cells = [cell['cell_coordinates'] for cell in belief_set['map'
        ]['grid'] if cell['cell_type'] == 'delivery_cell']
    for cell in delivery_cells:
        if agent['coordinates'][0] > cell[0]:
            function_1()
        elif agent['coordinates'][0] < cell[0]:
            function_2()
        elif agent['coordinates'][1] > cell[1]:
            function_3()
        elif agent['coordinates'][1] < cell[1]:
            function_4()
