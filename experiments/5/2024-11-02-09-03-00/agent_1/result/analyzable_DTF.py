def function_dtf_1(belief_set):
    if not belief_set['parcels']:
        return False
    max_score = sum(parcel['score'] for parcel in belief_set['parcels'].
        values())
    if belief_set['agent'][1]['score'] < max_score:
        return True
    return False


def function_dtf_2(belief_set):
    agent = belief_set['agent'][1]
    if agent['score'] >= 260:
        return False
    else:
        walkable_cells = sum(1 for cell in belief_set['map']['grid'] if 
            cell['cell_type'] == 'walkable')
        parcels_spawn_cells = sum(1 for cell in belief_set['map']['grid'] if
            cell['cell_type'] == 'parcels_spawn')
        delivery_cells = sum(1 for cell in belief_set['map']['grid'] if 
            cell['cell_type'] == 'delivery_cell')
        if (walkable_cells > 0 and parcels_spawn_cells > 0 and 
            delivery_cells > 0):
            return True
    return False


