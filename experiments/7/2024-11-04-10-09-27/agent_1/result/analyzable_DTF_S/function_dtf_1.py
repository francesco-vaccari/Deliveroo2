def function_dtf_1(belief_set):
    if belief_set['parcels'] or belief_set['agent'][1]['energy'] < 25:
        return True
    else:
        return False
