def function_8():
    global belief_set
    agent = belief_set['agent']
    key = belief_set['key']
    while agent['coordinates'] != key[1]['coordinates']:
        if agent['coordinates'][0] < key[1]['coordinates'][0]:
            function_2()
        elif agent['coordinates'][0] > key[1]['coordinates'][0]:
            function_1()
        elif agent['coordinates'][1] < key[1]['coordinates'][1]:
            function_4()
        elif agent['coordinates'][1] > key[1]['coordinates'][1]:
            function_3()
    function_5()

def function_9():
    global belief_set
    key_coordinates = belief_set['key'][1]['coordinates']
    door_coordinates = belief_set['door'][1]['coordinates']
    max_iterations = 100
    iterations = 0
    while belief_set['agent']['coordinates'
        ] != key_coordinates and iterations < max_iterations:
        if belief_set['agent']['coordinates'][0] < key_coordinates[0]:
            function_2()
        elif belief_set['agent']['coordinates'][0] > key_coordinates[0]:
            function_1()
        elif belief_set['agent']['coordinates'][1] < key_coordinates[1]:
            function_4()
        elif belief_set['agent']['coordinates'][1] > key_coordinates[1]:
            function_3()
        iterations += 1
    function_5()
    while belief_set['agent']['coordinates'
        ] != door_coordinates and iterations < max_iterations:
        if belief_set['agent']['coordinates'][0] < door_coordinates[0]:
            function_2()
        elif belief_set['agent']['coordinates'][0] > door_coordinates[0]:
            function_1()
        elif belief_set['agent']['coordinates'][1] < door_coordinates[1]:
            function_4()
        elif belief_set['agent']['coordinates'][1] > door_coordinates[1]:
            function_3()
        iterations += 1
    belief_set['agent']['has_key'] = False
    belief_set['door'][1]['coordinates'] = None

def function_10():
    global belief_set
    delivery_cell = next(cell for cell in belief_set['map']['grid'] if cell
        ['cell_type'] == 'delivery_cell')
    agent = belief_set['agent']
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

