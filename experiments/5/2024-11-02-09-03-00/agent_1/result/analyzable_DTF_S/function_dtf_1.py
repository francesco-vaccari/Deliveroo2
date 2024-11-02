def function_dtf_1(belief_set):
    if not belief_set['parcels']:
        return False
    max_score = sum(parcel['score'] for parcel in belief_set['parcels'].
        values())
    if belief_set['agent'][1]['score'] < max_score:
        return True
    return False
