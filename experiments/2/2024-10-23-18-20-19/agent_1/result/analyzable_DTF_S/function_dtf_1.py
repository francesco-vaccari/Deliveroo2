def function_dtf_1(belief_set):
    if belief_set['agent']['has_key'] and belief_set['parcel']:
        return True
    elif belief_set['key'] and not belief_set['agent']['has_key']:
        return True
    elif belief_set['parcel'] and belief_set['agent']['parcels_carried_ids']:
        return True
    else:
        return False
