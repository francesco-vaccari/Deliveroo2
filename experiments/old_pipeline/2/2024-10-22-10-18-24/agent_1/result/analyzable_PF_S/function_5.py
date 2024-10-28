def function_5(event, belief_set):
    if event['object_type'] == 'door':
        if event['event_type'] == 'object added':
            belief_set['door'] = {event['object']['id']: event['object']}
        elif event['event_type'] == 'object changed':
            if 'door' in belief_set:
                belief_set['door'][event['object']['id']] = event['object']
        elif event['event_type'] == 'object removed':
            if 'door' in belief_set:
                belief_set['door'].pop(event['object']['id'], None)
    return belief_set
