def function_13():
    global belief_set
    agent = belief_set['agent']
    parcel = belief_set['parcel'][1]
    if agent['coordinates'] == parcel['coordinates']:
        function_5()
    delivery_cells = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] in ['delivery_cell', 'double_delivery_cell']]
    for cell in delivery_cells:
        if agent['coordinates'][0] < cell['cell_coordinates'][0]:
            while agent['coordinates'][0] != cell['cell_coordinates'][0]:
                function_2()
        elif agent['coordinates'][0] > cell['cell_coordinates'][0]:
            while agent['coordinates'][0] != cell['cell_coordinates'][0]:
                function_1()
        if agent['coordinates'][1] < cell['cell_coordinates'][1]:
            while agent['coordinates'][1] != cell['cell_coordinates'][1]:
                function_4()
        elif agent['coordinates'][1] > cell['cell_coordinates'][1]:
            while agent['coordinates'][1] != cell['cell_coordinates'][1]:
                function_3()
    function_6()
