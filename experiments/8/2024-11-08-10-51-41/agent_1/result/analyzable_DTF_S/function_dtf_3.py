def function_dtf_3(belief_set):
    agent = belief_set['agent'][1]
    if len(agent['parcels_carried_ids']) > 0 or agent['has_key'] or agent[
        'energy'] > 50:
        return True
    return False
