def function_dtf_1(belief_set):
    if not belief_set['agent'][1]['parcels_carried_ids'] and not belief_set[
        'parcels']:
        return False
    if belief_set['agent'][1]['parcels_carried_ids']:
        return True
    if belief_set['parcels']:
        return True
    return False
