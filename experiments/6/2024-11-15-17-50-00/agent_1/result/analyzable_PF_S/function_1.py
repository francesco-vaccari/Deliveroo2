def function_1(event, current_beliefs):
    if event['object_type'] == 'map':
        if event['event_type'] == 'object added':
            current_beliefs['map'] = event['object']
        elif event['event_type'] == 'object changed':
            current_beliefs['map'].update(event['object'])
        elif event['event_type'] == 'object removed':
            current_beliefs.pop('map', None)
    return current_beliefs
