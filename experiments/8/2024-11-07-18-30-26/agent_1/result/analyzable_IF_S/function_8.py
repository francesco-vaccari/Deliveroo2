def function_8():
    global belief_set
    agent_coordinates = belief_set['agent'][1]['coordinates']
    if belief_set['agent'][1]['parcels_carried_ids']:
        if 'delivery' in [cell['cell_type'] for cell in belief_set['map'][
            'grid'] if cell['cell_coordinates'] == agent_coordinates]:
            function_6()
        else:
            if agent_coordinates[0] > 0:
                function_1()
            elif agent_coordinates[0] < belief_set['map']['width'] - 1:
                function_2()
            if agent_coordinates[1] > 0:
                function_3()
            elif agent_coordinates[1] < belief_set['map']['height'] - 1:
                function_4()
    else:
        function_7()
