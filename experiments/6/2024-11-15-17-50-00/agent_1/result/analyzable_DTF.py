def function_dtf_1(belief_set):
    agent = belief_set['agent'][1]
    parcels = belief_set['parcels']
    if agent['energy'] < 30 and belief_set['batteries']:
        return True
    for parcel in parcels.values():
        if parcel['carried_by_id'] is None:
            return True
    if agent['parcels_carried_ids']:
        return True
    return False


