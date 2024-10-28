def function_9():
    global belief_set
    agent = belief_set['agent']
    delivery_cell = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'delivery_cell'][0]['cell_coordinates']
    while agent['coordinates'] != delivery_cell:
        if agent['coordinates'][0] < delivery_cell[0]:
            function_2()
            agent['coordinates'][0] += 1
        elif agent['coordinates'][0] > delivery_cell[0]:
            function_1()
            agent['coordinates'][0] -= 1
        elif agent['coordinates'][1] < delivery_cell[1]:
            function_4()
            agent['coordinates'][1] += 1
        elif agent['coordinates'][1] > delivery_cell[1]:
            function_3()
            agent['coordinates'][1] -= 1
    function_6()
