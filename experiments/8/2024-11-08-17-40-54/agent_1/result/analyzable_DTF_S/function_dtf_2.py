def function_dtf_2(belief_set):
    if belief_set['agent']['energy'] > 50 and not belief_set['agent']['has_key'
        ] and len(belief_set['keys']) > 0:
        return True
    return False
