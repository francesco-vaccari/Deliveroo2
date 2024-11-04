def function_dtf_2(belief_set):
    agent = belief_set['agent']
    if agent['energy'] < 20:
        return False
    if len(belief_set['parcels']) == 0 and len(agent['parcels_carried_ids']
        ) == 0:
        return False
    return True
