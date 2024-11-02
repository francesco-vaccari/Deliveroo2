def function_dtf_1(belief_set):
    if len(belief_set['parcels']) > 0:
        return True
    if len(belief_set['agent'][1]['parcels_carried_ids']) > 0:
        return True
    if belief_set['agent'][1]['energy'] < 20:
        return True
    return False
