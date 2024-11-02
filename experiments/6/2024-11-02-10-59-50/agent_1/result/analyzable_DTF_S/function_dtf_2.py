def function_dtf_2(belief_set):
    if belief_set['parcels'] or belief_set['agent'][1]['parcels_carried_ids']:
        return True
    elif belief_set['agent'][1]['energy'] < 30 and belief_set['batteries']:
        return True
    else:
        return False
