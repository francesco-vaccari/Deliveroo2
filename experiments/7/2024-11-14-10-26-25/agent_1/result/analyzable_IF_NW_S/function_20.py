def function_20():
    global belief_set
    parcel_spawn_cell = next(cell for cell in belief_set['map']['grid'] if 
        cell['cell_type'] == 'parcels_spawn')['cell_coordinates']
    delivery_cell = next(cell for cell in belief_set['map']['grid'] if cell
        ['cell_type'] == 'delivery_cell')['cell_coordinates']
    agent_coords = belief_set['agent']['coordinates']
    for i in range(30):
        if agent_coords[0] < parcel_spawn_cell[0]:
            function_2()
            agent_coords = belief_set['agent']['coordinates']
        elif agent_coords[0] > parcel_spawn_cell[0]:
            function_1()
            agent_coords = belief_set['agent']['coordinates']
        elif agent_coords[1] < parcel_spawn_cell[1]:
            function_4()
            agent_coords = belief_set['agent']['coordinates']
        elif agent_coords[1] > parcel_spawn_cell[1]:
            function_3()
            agent_coords = belief_set['agent']['coordinates']
        function_5()
        if agent_coords[0] < delivery_cell[0]:
            function_2()
            agent_coords = belief_set['agent']['coordinates']
        elif agent_coords[0] > delivery_cell[0]:
            function_1()
            agent_coords = belief_set['agent']['coordinates']
        elif agent_coords[1] < delivery_cell[1]:
            function_4()
            agent_coords = belief_set['agent']['coordinates']
        elif agent_coords[1] > delivery_cell[1]:
            function_3()
            agent_coords = belief_set['agent']['coordinates']
        function_6()
