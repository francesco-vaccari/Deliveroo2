def function_dtf_1(belief_set):
    if 'parcels' in belief_set and belief_set['parcels'
        ] and 'agent' in belief_set and belief_set['agent']['score'] < sum(
        parcel['score'] for parcel in belief_set['parcels'].values()):
        return True
    return False
