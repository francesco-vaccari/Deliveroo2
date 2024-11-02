def function_dtf_1(belief_set):
    if len(belief_set['parcels']) > 0:
        return True
    if len(belief_set['agent'][1]['parcels_carried_ids']) > 0:
        return True
    if belief_set['agent'][1]['energy'] < 20:
        return True
    return False


def function_dtf_2(belief_set):
    agent = belief_set['agent'][1]
    has_parcels_on_map = bool(belief_set['parcels'])
    has_batteries_on_map = bool(belief_set['batteries'])
    has_energy = agent['energy'] > 0
    return has_parcels_on_map or has_batteries_on_map and has_energy


