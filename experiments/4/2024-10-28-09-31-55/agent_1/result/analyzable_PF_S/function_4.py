def function_4(event, belief_set):
    if event['object_type'] == 'key':
        if event['event_type'] == 'object added':
            belief_set['keys'] = {event['object']['id']: event['object']}
        elif event['event_type'] == 'object changed':
            belief_set['keys'][event['object']['id']] = event['object']
        elif event['event_type'] == 'object removed':
            belief_set['keys'].pop(event['object']['id'], None)
    return belief_set