def function_dtf_1(belief_set):
    if belief_set['agent']['energy'] > 5 and any(parcel['carried_by_id'] is
        None for parcel in belief_set['parcels'].values()):
        return True
    else:
        return False
