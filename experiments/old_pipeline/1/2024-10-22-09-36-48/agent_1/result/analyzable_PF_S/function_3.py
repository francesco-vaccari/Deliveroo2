def function_3(event, belief_set):
    event_type = event['event_type']
    object_type = event['object_type']
    if object_type == 'agent':
        if event_type == 'object added':
            belief_set['agent'] = {event['object']['id']: event['object']}
        elif event_type == 'object changed':
            belief_set['agent'][event['object']['id']] = event['object']
        elif event_type == 'object removed':
            del belief_set['agent'][event['object']['id']]
    return belief_set
