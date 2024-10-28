def function_5(event, belief_set):
    if event['object_type'] == 'door':
        if event['event_type'] == 'object added':
            belief_set['doors'] = {event['object']['id']: event['object']}
        elif event['event_type'] == 'object changed':
            belief_set['doors'][event['object']['id']] = event['object']
        elif event['event_type'] == 'object removed':
            del belief_set['doors'][event['object']['id']]
    return belief_set
