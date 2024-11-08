def function_dtf_2(belief_set):
    if 'batteries' in belief_set and belief_set['batteries'] and belief_set[
        'agent'][1]['energy'] < 100:
        return True
    return False
