def function_4(event, belief_set):
    if event['object_type'] == 'key':
        if event['event_type'] == 'object added':
            belief_set['key'] = {event['object']['id']: event['object']}
        elif event['event_type'] == 'object changed':
            belief_set['key'][event['object']['id']] = event['object']
        elif event['event_type'] == 'object removed':
            del belief_set['key'][event['object']['id']]
    return belief_set
