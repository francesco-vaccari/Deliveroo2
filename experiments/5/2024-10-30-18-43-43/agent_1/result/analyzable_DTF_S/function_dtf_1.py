def function_dtf_1(belief_set):
    if len(belief_set['parcels']) > 0 or len(belief_set['agent'][1][
        'parcels_carried_ids']) > 0:
        return True
    else:
        return False
