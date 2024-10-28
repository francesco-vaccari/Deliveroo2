def function_9():
    global belief_set
    agent = belief_set['agent'][1]
    delivery_cell = [cell for cell in belief_set['map']['map']['grid'] if 
        cell['cell_type'] == 'delivery_cell'][0]['cell_coordinates']
    if agent['coordinates'][0] < delivery_cell[0]:
        function_2()
    elif agent['coordinates'][0] > delivery_cell[0]:
        function_1()
    elif agent['coordinates'][1] < delivery_cell[1]:
        function_4()
    elif agent['coordinates'][1] > delivery_cell[1]:
        function_3()
    else:
        function_6()
