def function_1(event, belief_set):
    if event['event_type'] == 'object added':
        belief_set[event['object_type']] = event['object']
    elif event['event_type'] == 'object changed':
        for key, value in event['object'].items():
            belief_set[event['object_type']][key] = value
    elif event['event_type'] == 'object removed':
        del belief_set[event['object_type']]
    return belief_set
