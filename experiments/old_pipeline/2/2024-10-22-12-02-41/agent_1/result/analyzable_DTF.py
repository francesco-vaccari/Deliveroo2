def function_dtf_1(belief_set):
    for key in belief_set['keys']:
        if belief_set['keys'][key]['carried_by_id'] is None:
            return True
    for cell in belief_set['map']['grid']:
        if cell['cell_type'] == 'walkable' and cell['cell_coordinates'
            ] != belief_set['agent']['coordinates']:
            return True
    return False


def function_dtf_2(belief_set):
    if belief_set['parcels'] or belief_set['keys']:
        return True
    if belief_set['agent']['parcels_carried_ids'] or belief_set['agent'][
        'has_key']:
        return True
    return False


