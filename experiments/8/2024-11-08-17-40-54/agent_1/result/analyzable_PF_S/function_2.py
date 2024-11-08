def function_2(event, beliefs):
    if event['object_type'] == 'agent':
        if event['event_type'] == 'object added':
            beliefs['agent'] = event['object']
        elif event['event_type'] == 'object changed':
            beliefs['agent'].update(event['object'])
        elif event['event_type'] == 'object removed':
            del beliefs['agent']
    return beliefs
