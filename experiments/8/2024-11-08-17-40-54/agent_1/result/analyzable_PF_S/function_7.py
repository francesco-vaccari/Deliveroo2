def function_7(event, beliefs):
    if event['object_type'] == 'key':
        if event['event_type'] == 'object added':
            beliefs['keys'][event['object']['id']] = event['object']
        elif event['event_type'] == 'object changed':
            beliefs['keys'][event['object']['id']].update(event['object'])
        elif event['event_type'] == 'object removed':
            if event['object']['id'] in beliefs['keys']:
                del beliefs['keys'][event['object']['id']]
    return beliefs
