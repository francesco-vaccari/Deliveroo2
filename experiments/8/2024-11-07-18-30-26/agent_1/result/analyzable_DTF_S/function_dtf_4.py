def function_dtf_4(belief_set):
    if not belief_set['agent'][1]['has_key']:
        return True
    elif belief_set['doors']:
        return True
    else:
        return False
