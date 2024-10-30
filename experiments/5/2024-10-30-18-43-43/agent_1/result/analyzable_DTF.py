def function_dtf_1(belief_set):
    if len(belief_set['parcels']) > 0 or len(belief_set['agent'][1][
        'parcels_carried_ids']) > 0:
        return True
    else:
        return False


def function_dtf_2(belief_set):
    if len(belief_set['parcels']) == 0:
        return False
    agent_coords = belief_set['agent'][1]['coordinates']
    for cell in belief_set['map']['grid']:
        if cell['cell_type'] == 'non_walkable' and cell['cell_coordinates'
            ] == agent_coords:
            return False
    return True


