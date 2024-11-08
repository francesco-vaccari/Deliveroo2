def function_dtf_1(belief_set):
    agent_energy = belief_set['agent'][1]['energy']
    parcels = belief_set['parcels']
    if agent_energy < 10:
        return False
    if parcels:
        for parcel in parcels.values():
            if parcel['carried_by_id'] is None:
                return True
    return False


def function_dtf_2(belief_set):
    if 'batteries' in belief_set and belief_set['batteries'] and belief_set[
        'agent'][1]['energy'] < 100:
        return True
    return False


def function_dtf_3(belief_set):
    keys = belief_set['keys']
    agent = belief_set['agent'][1]
    for key_id, key in keys.items():
        if key['carried_by_id'] is None or key['carried_by_id'] != agent['id']:
            return True
    return False


def function_dtf_4(belief_set):
    if not belief_set['agent'][1]['has_key']:
        return True
    elif belief_set['doors']:
        return True
    else:
        return False


