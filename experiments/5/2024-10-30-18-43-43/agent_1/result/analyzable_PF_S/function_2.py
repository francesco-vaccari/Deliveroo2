def function_2(event, beliefs):
    if event['object_type'] == 'agent':
        if event['event_type'] == 'object added':
            beliefs['agent'] = {event['object']['id']: event['object']}
        elif event['event_type'] == 'object changed':
            beliefs['agent'][event['object']['id']].update(event['object'])
        elif event['event_type'] == 'object removed':
            del beliefs['agent'][event['object']['id']]
    return beliefs
