def function_dtf_1(belief_set):
    if 'parcel' in belief_set and belief_set['parcel']:
        return True
    if belief_set['agent']['parcels_carried_ids']:
        return True
    if belief_set['agent']['has_key']:
        return True
    return False


