def function_4(event, belief_set):
    object_id = event['object']['id']
    if event['event_type'] == 'object added':
        if 'key' not in belief_set:
            belief_set['key'] = {}
        belief_set['key'][object_id] = event['object']
    elif event['event_type'] == 'object changed':
        if 'key' in belief_set and object_id in belief_set['key']:
            belief_set['key'][object_id] = event['object']
    elif event['event_type'] == 'object removed':
        if 'key' in belief_set and object_id in belief_set['key']:
            del belief_set['key'][object_id]
    return belief_set
