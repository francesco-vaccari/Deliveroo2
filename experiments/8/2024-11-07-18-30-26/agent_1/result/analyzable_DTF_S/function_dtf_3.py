def function_dtf_3(belief_set):
    keys = belief_set['keys']
    agent = belief_set['agent'][1]
    for key_id, key in keys.items():
        if key['carried_by_id'] is None or key['carried_by_id'] != agent['id']:
            return True
    return False
