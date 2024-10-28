def function_dtf_1(belief_set):
    if belief_set['parcels'] or belief_set['keys']:
        return True
    if belief_set['agent']['parcels_carried_ids']:
        return True
    if belief_set['agent']['has_key']:
        return True
    return False


