def function_1(event, belief):
    if event['object_type'] == 'map':
        if event['event_type'] == 'object added':
            belief['map'] = event['object']
        elif event['event_type'] == 'object changed':
            belief['map'].update(event['object'])
        elif event['event_type'] == 'object removed':
            belief.pop('map', None)
    return belief
