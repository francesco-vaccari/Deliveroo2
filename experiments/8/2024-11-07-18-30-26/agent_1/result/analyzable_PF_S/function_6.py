def function_6(event, beliefs):
    door_id = event['object']['id']
    if event['event_type'] == 'object added':
        if 'doors' not in beliefs:
            beliefs['doors'] = {}
        beliefs['doors'][door_id] = event['object']
    elif event['event_type'] == 'object changed':
        if 'doors' in beliefs and door_id in beliefs['doors']:
            beliefs['doors'][door_id].update(event['object'])
    elif event['event_type'] == 'object removed':
        if 'doors' in beliefs and door_id in beliefs['doors']:
            del beliefs['doors'][door_id]
    return beliefs
