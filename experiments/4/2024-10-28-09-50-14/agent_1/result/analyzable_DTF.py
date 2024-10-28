def function_dtf_1(belief_set):
    if belief_set['parcels']:
        return True
    if belief_set['agents'][1]['parcels_carried_ids']:
        return True
    if belief_set['keys']:
        for key in belief_set['keys']:
            if belief_set['keys'][key]['carried_by_id'] is None:
                return True
    if belief_set['doors']:
        for door in belief_set['doors']:
            if belief_set['doors'][door]['coordinates'] in [cell[
                'cell_coordinates'] for cell in belief_set['map']['grid'] if
                cell['cell_type'] == 'walkable']:
                return True
    return False


