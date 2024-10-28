def function_dtf_1(belief_set):
    parcels = belief_set['parcels']
    agent = belief_set['agent']
    keys = belief_set['keys']
    if parcels and any(parcel['carried_by_id'] is None for parcel in
        parcels.values()):
        return True
    if agent['has_key'] is False and keys and any(key['carried_by_id'] is
        None for key in keys.values()):
        return True
    if agent['coordinates'] != [1, 3]:
        return True
    return False


