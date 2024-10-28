def function_dtf_1(belief_set):
    if 'parcels' in belief_set and belief_set['parcels']:
        return True
    elif 'agent' in belief_set and belief_set['agent'][1]['parcels_carried_ids'
        ]:
        return True
    else:
        return False


