def function_dtf_2(belief_set):
    agent = belief_set['agent'][1]
    has_parcels_on_map = bool(belief_set['parcels'])
    has_batteries_on_map = bool(belief_set['batteries'])
    has_energy = agent['energy'] > 0
    return has_parcels_on_map or has_batteries_on_map and has_energy
