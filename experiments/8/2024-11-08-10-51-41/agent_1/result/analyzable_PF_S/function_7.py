def function_7(event, belief_set):
    if event['object_type'] != 'key':
        return belief_set
    key_id = event['object']['id']
    if event['event_type'] == 'object added':
        belief_set['keys'][key_id] = event['object']
    elif event['event_type'] == 'object changed':
        belief_set['keys'][key_id].update(event['object'])
    elif event['event_type'] == 'object removed':
        if key_id in belief_set['keys']:
            del belief_set['keys'][key_id]
    return belief_set
