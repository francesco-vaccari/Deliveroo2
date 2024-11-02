def function_11():
    global belief_set
    max_iterations = 100
    iteration_count = 0
    agent_id = 1
    while iteration_count < max_iterations:
        agent_coords = belief_set['agent'][agent_id]['coordinates']
        parcel_spawn_coords = [cell['cell_coordinates'] for cell in
            belief_set['map']['grid'] if cell['cell_type'] == 'parcels_spawn'][
            0]
        delivery_cell_coords = [cell['cell_coordinates'] for cell in
            belief_set['map']['grid'] if cell['cell_type'] == 'delivery_cell'][
            0]
        if agent_coords == parcel_spawn_coords and len(belief_set['agent'][
            agent_id]['parcels_carried_ids']) < 1:
            function_5()
        elif agent_coords == delivery_cell_coords and len(belief_set[
            'agent'][agent_id]['parcels_carried_ids']) >= 1:
            function_6()
        elif agent_coords[0] > parcel_spawn_coords[0] and belief_set['map'][
            'grid'][agent_coords[0] - 1][agent_coords[1]]['cell_type'
            ] != 'non_walkable':
            function_1()
        elif agent_coords[0] < parcel_spawn_coords[0] and belief_set['map'][
            'grid'][agent_coords[0] + 1][agent_coords[1]]['cell_type'
            ] != 'non_walkable':
            function_2()
        elif agent_coords[1] > parcel_spawn_coords[1] and belief_set['map'][
            'grid'][agent_coords[0]][agent_coords[1] - 1]['cell_type'
            ] != 'non_walkable':
            function_3()
        elif agent_coords[1] < parcel_spawn_coords[1] and belief_set['map'][
            'grid'][agent_coords[0]][agent_coords[1] + 1]['cell_type'
            ] != 'non_walkable':
            function_4()
        iteration_count += 1
