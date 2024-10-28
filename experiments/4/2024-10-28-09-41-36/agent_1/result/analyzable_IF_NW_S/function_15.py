def function_15():
    global belief_set
    delivery_cells = [cell['cell_coordinates'] for cell in belief_set['map'
        ]['grid'] if 'delivery' in cell['cell_type']]
    agent_coordinates = belief_set['agent']['coordinates']
    if agent_coordinates in delivery_cells:
        function_6()
    else:
        target_cell = delivery_cells[0]
        if agent_coordinates[0] < target_cell[0]:
            function_2()
        elif agent_coordinates[0] > target_cell[0]:
            function_1()
        elif agent_coordinates[1] < target_cell[1]:
            function_4()
        elif agent_coordinates[1] > target_cell[1]:
            function_3()
