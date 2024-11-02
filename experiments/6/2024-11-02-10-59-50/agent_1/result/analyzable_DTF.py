def function_dtf_1(belief_set):
    agent = belief_set['agent'][1]
    parcels = belief_set['parcels']
    batteries = belief_set['batteries']
    if len(parcels) > 0 or len(batteries) > 0 or agent['energy'] < 50:
        return True
    else:
        return False


def function_dtf_2(belief_set):
    if belief_set['parcels'] or belief_set['agent'][1]['parcels_carried_ids']:
        return True
    elif belief_set['agent'][1]['energy'] < 30 and belief_set['batteries']:
        return True
    else:
        return False


