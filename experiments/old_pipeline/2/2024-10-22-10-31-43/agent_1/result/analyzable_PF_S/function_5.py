def function_5(event, belief_set):
    if event['object_type'] == 'door':
        if event['event_type'] == 'object added':
            belief_set['door'] = {event['object']['id']: event['object']}
        elif event['event_type'] == 'object changed':
            if 'door' in belief_set and event['object']['id'] in belief_set[
                'door']:
                belief_set['door'][event['object']['id']].update(event[
                    'object'])
        elif event['event_type'] == 'object removed':
            if 'door' in belief_set and event['object']['id'] in belief_set[
                'door']:
                del belief_set['door'][event['object']['id']]
    return belief_set
