def function_dtf_1(belief_set):
    if 'batteries' in belief_set and len(belief_set['batteries']) > 0:
        return True
    return False
