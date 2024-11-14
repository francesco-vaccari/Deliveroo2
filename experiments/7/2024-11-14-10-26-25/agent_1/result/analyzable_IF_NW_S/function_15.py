def function_15():
    global belief_set
    delivery_cell = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'delivery_cell'][0]['cell_coordinates']
    agent_coordinates = belief_set['agent']['coordinates']
    if agent_coordinates[0] < delivery_cell[0]:
        function_2()
    elif agent_coordinates[0] > delivery_cell[0]:
        function_1()
    elif agent_coordinates[1] < delivery_cell[1]:
        function_4()
    elif agent_coordinates[1] > delivery_cell[1]:
        function_3()
    else:
        function_6()
