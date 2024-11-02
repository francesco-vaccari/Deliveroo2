def function_10():
    global belief_set
    agent = belief_set['agent'][1]
    parcels = belief_set['parcels']
    map_grid = belief_set['map']['grid']
    spawn_cells = [cell for cell in map_grid if cell['cell_type'] ==
        'parcels_spawn']
    delivery_cells = [cell for cell in map_grid if cell['cell_type'] ==
        'delivery_cell']
    if len(agent['parcels_carried_ids']) == 0:
        for cell in spawn_cells:
            while agent['coordinates'] != cell['cell_coordinates']:
                if agent['coordinates'][0] > cell['cell_coordinates'][0]:
                    function_1()
                elif agent['coordinates'][0] < cell['cell_coordinates'][0]:
                    function_2()
                elif agent['coordinates'][1] > cell['cell_coordinates'][1]:
                    function_3()
                elif agent['coordinates'][1] < cell['cell_coordinates'][1]:
                    function_4()
            function_5()
    else:
        for cell in delivery_cells:
            while agent['coordinates'] != cell['cell_coordinates']:
                if agent['coordinates'][0] > cell['cell_coordinates'][0]:
                    function_1()
                elif agent['coordinates'][0] < cell['cell_coordinates'][0]:
                    function_2()
                elif agent['coordinates'][1] > cell['cell_coordinates'][1]:
                    function_3()
                elif agent['coordinates'][1] < cell['cell_coordinates'][1]:
                    function_4()
            function_6()
