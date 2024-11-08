def function_dtf_1(belief_set):
    if belief_set['agent']['energy'] > 50 and len(belief_set['agent'][
        'parcels_carried_ids']) < 5:
        for parcel in belief_set['parcels'].values():
            if parcel['carried_by_id'] is None:
                return True
    return False
