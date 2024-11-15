def function_3(event, beliefs):
    if event['object_type'] == 'battery':
        if event['event_type'] == 'object added':
            if 'batteries' not in beliefs:
                beliefs['batteries'] = {}
            beliefs['batteries'][event['object']['id']] = event['object']
        elif event['event_type'] == 'object changed':
            if 'batteries' in beliefs and event['object']['id'] in beliefs[
                'batteries']:
                beliefs['batteries'][event['object']['id']] = event['object']
        elif event['event_type'] == 'object removed':
            if 'batteries' in beliefs and event['object']['id'] in beliefs[
                'batteries']:
                del beliefs['batteries'][event['object']['id']]
    return beliefs
