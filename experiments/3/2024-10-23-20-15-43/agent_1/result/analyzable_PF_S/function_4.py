def function_4(event, beliefs):
    if event['object_type'] == 'key':
        if event['event_type'] == 'object added':
            beliefs['keys'] = {event['object']['id']: event['object']}
        elif event['event_type'] == 'object changed':
            beliefs['keys'][event['object']['id']] = event['object']
        elif event['event_type'] == 'object removed':
            del beliefs['keys'][event['object']['id']]
    return beliefs
