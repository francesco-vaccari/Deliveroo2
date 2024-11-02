def function_dtf_1(belief_set):
    spawn_cells = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'parcels_spawn']
    delivery_cells = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'delivery_cell']
    walkable_cells = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'walkable']
    agent_position = belief_set['agent'][1]['coordinates']
    parcels_carried = belief_set['agent'][1]['parcels_carried_ids']
    if len(spawn_cells) == 0 or len(delivery_cells) == 0 or len(walkable_cells
        ) == 0:
        return False
    elif agent_position in [cell['cell_coordinates'] for cell in delivery_cells
        ] and len(parcels_carried) > 0:
        return False
    else:
        return True


def function_dtf_2(belief_set):
    if not belief_set['parcels']:
        return False
    if belief_set['agent'][1]['coordinates'] == [1, 3] and belief_set['agent'][
        1]['parcels_carried_ids']:
        return True
    return True


