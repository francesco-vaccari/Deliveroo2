def function_3(event, belief_set):
    if event['object_type'] == 'agent':
        if event['event_type'] == 'object added':
            belief_set['agent'] = event['object']
        elif event['event_type'] == 'object changed':
            for key, value in event['object'].items():
                belief_set['agent'][key] = value
        elif event['event_type'] == 'object removed':
            del belief_set['agent']
    return belief_set
