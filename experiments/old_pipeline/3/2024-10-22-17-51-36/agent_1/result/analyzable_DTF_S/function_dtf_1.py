def function_dtf_1(belief_set):
    for parcel in belief_set['parcels'].values():
        if parcel['carried_by_id'] != belief_set['agent']['id']:
            return True
    if len(belief_set['agent']['parcels_carried_ids']) > 0:
        return True
    return False
