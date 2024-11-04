def function_18():
    global belief_set
    delivery_cell = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'delivery_cell']
    agent = belief_set['agent'][1]
    while agent['coordinates'] != delivery_cell[0]['cell_coordinates']:
        if agent['coordinates'][0] < delivery_cell[0]['cell_coordinates'][0]:
            function_2()
        elif agent['coordinates'][0] > delivery_cell[0]['cell_coordinates'][0]:
            function_1()
        elif agent['coordinates'][1] < delivery_cell[0]['cell_coordinates'][1]:
            function_4()
        elif agent['coordinates'][1] > delivery_cell[0]['cell_coordinates'][1]:
            function_3()
    function_6()
