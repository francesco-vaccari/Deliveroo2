def function_dtf_2(belief_set):
    if not belief_set['parcels']:
        return False
    if belief_set['agent'][1]['coordinates'] == [1, 3] and belief_set['agent'][
        1]['parcels_carried_ids']:
        return True
    return True
