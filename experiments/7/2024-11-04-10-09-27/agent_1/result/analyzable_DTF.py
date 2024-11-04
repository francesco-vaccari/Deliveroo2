def function_dtf_1(belief_set):
    if belief_set['parcels'] or belief_set['agent'][1]['energy'] < 25:
        return True
    else:
        return False


def function_dtf_2(belief_set):
    agent = belief_set['agent'][1]
    if agent['has_key'] and agent['energy'] > 50:
        return True
    if belief_set['doors'] and not agent['has_key'] and agent['energy'] > 50:
        return True
    return False


