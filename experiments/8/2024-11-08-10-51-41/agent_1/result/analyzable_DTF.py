def function_dtf_1(belief_set):
    agent = belief_set['agent'][1]
    if agent['parcels_carried_ids'] and agent['energy'] > 0:
        return True
    else:
        return False


def function_dtf_2(belief_set):
    agent = belief_set['agent'][1]
    keys = belief_set['keys']
    for key in keys.values():
        if key['carried_by_id'] is None:
            return True
    if not agent['has_key']:
        return True
    return False


def function_dtf_3(belief_set):
    agent = belief_set['agent'][1]
    if len(agent['parcels_carried_ids']) > 0 or agent['has_key'] or agent[
        'energy'] > 50:
        return True
    return False


