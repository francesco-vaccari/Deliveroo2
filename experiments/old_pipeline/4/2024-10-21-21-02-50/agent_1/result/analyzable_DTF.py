def function_dtf_1(belief_set):
    if len(belief_set['parcels']) > 0:
        return True
    if len(belief_set['agents'][1]['parcels_carried_ids']) > 0:
        return True
    if len(belief_set['keys']) > 0:
        return True
    if len(belief_set['doors']) > 0:
        return True
    return False


