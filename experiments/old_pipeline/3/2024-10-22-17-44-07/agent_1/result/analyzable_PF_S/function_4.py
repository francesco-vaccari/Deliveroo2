def function_4(event, belief_set):
    if 'keys' not in belief_set:
        belief_set['keys'] = {}
    if event['event_type'] == 'object added':
        belief_set['keys'][event['object']['id']] = event['object']
    elif event['event_type'] == 'object changed':
        if event['object']['id'] in belief_set['keys']:
            belief_set['keys'][event['object']['id']].update(event['object'])
    elif event['event_type'] == 'object removed':
        if event['object']['id'] in belief_set['keys']:
            del belief_set['keys'][event['object']['id']]
    return belief_set
