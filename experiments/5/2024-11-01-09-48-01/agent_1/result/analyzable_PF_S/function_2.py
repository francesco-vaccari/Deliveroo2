def function_2(event, belief_set):
    if event['object_type'] == 'agent':
        if event['event_type'] == 'object added':
            belief_set['agent'] = {event['object']['id']: event['object']}
        elif event['event_type'] == 'object changed':
            if 'agent' in belief_set and event['object']['id'] in belief_set[
                'agent']:
                belief_set['agent'][event['object']['id']].update(event[
                    'object'])
        elif event['event_type'] == 'object removed':
            if 'agent' in belief_set and event['object']['id'] in belief_set[
                'agent']:
                del belief_set['agent'][event['object']['id']]
    return belief_set
