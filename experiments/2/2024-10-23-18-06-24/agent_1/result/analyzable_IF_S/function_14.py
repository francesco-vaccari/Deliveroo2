def function_14():
    global belief_set
    delivery_coordinates = [cell['cell_coordinates'] for cell in belief_set
        ['map']['grid'] if cell['cell_type'] == 'delivery_cell'][0]
    agent_coordinates = belief_set['agent']['coordinates']
    max_iterations = belief_set['map']['width'] * belief_set['map']['height']
    counter = 0
    while (agent_coordinates != delivery_coordinates and counter <
        max_iterations):
        if agent_coordinates[1] < delivery_coordinates[1]:
            function_4()
        elif agent_coordinates[0] < delivery_coordinates[0]:
            function_2()
        else:
            function_1()
        counter += 1
        agent_coordinates = belief_set['agent']['coordinates']
