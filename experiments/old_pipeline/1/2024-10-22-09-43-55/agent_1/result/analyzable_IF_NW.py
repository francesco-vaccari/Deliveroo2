def function_8():
    global belief_set
    agent_position = belief_set['agent']['coordinates']
    delivery_position = [cell['cell_coordinates'] for cell in belief_set[
        'map']['grid'] if cell['cell_type'] == 'delivery_cell'][0]
    if agent_position[0] < delivery_position[0]:
        function_2()
    elif agent_position[0] > delivery_position[0]:
        function_1()
    elif agent_position[1] < delivery_position[1]:
        function_4()
    elif agent_position[1] > delivery_position[1]:
        function_3()
    else:
        function_6()

def function_9():
    global belief_set
    delivery_cell = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'delivery_cell'][0]['cell_coordinates']
    agent_position = belief_set['agent']['coordinates']
    if delivery_cell[0] < agent_position[0]:
        function_1()
    elif delivery_cell[0] > agent_position[0]:
        function_2()
    elif delivery_cell[1] < agent_position[1]:
        function_3()
    elif delivery_cell[1] > agent_position[1]:
        function_4()
    else:
        function_6()

def function_10():
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

