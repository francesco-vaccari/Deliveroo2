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
