def function_dtf_2(belief_set):
    agent = belief_set['agent'][1]
    keys = belief_set['keys']
    for key in keys.values():
        if key['carried_by_id'] is None:
            return True
    if not agent['has_key']:
        return True
    return False
