def function_1(event, belief_set):
    if event['object_type'] == 'map':
        if event['event_type'] == 'object added':
            belief_set['map'] = event['object']
        elif event['event_type'] == 'object changed':
            for key, value in event['object'].items():
                belief_set['map'][key] = value
        elif event['event_type'] == 'object removed':
            del belief_set['map']
    return belief_set
