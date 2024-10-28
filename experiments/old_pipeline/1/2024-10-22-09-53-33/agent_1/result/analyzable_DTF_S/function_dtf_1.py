def function_dtf_1(belief_set):
    if 'parcel' in belief_set and belief_set['parcel'] != {}:
        return True
    elif belief_set['agent'][1]['parcels_carried_ids'] != []:
        return True
    else:
        return False
