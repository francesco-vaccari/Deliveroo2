def function_dtf_1(belief_set):
    agent = belief_set['agent'][1]
    if agent['parcels_carried_ids'] and agent['energy'] > 0:
        return True
    else:
        return False
