def function_4(event, current_beliefs):
    if event['object_type'] != 'key':
        return current_beliefs
    if 'keys' not in current_beliefs:
        current_beliefs['keys'] = {}
    if event['event_type'] == 'object added':
        current_beliefs['keys'][event['object']['id']] = event['object']
    elif event['event_type'] == 'object changed':
        current_beliefs['keys'][event['object']['id']].update(event['object'])
    elif event['event_type'] == 'object removed':
        del current_beliefs['keys'][event['object']['id']]
    return current_beliefs
