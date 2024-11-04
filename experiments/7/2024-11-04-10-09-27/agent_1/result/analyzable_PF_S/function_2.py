def function_2(event, belief_set):
    if event['object_type'] == 'agent':
        if event['event_type'] == 'object added':
            belief_set['agent'] = {event['object']['id']: event['object']}
        elif event['event_type'] == 'object changed':
            belief_set['agent'][event['object']['id']] = event['object']
        elif event['event_type'] == 'object removed':
            del belief_set['agent'][event['object']['id']]
    return belief_set
