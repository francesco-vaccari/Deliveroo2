def function_9():
    global belief_set
    agent_coordinates = belief_set['agent']['coordinates']
    for cell in belief_set['map']['grid']:
        if cell['cell_type'] == 'walkable':
            cell_coordinates = cell['cell_coordinates']
            while agent_coordinates != cell_coordinates:
                if agent_coordinates[0] < cell_coordinates[0]:
                    function_2()
                    agent_coordinates[0] += 1
                elif agent_coordinates[0] > cell_coordinates[0]:
                    function_1()
                    agent_coordinates[0] -= 1
                if agent_coordinates[1] < cell_coordinates[1]:
                    function_4()
                    agent_coordinates[1] += 1
                elif agent_coordinates[1] > cell_coordinates[1]:
                    function_3()
                    agent_coordinates[1] -= 1
            function_5()
            break
