def function_4(event, belief_set):
    if event['object_type'] != 'key':
        return belief_set
    if 'keys' not in belief_set:
        belief_set['keys'] = {}
    if event['event_type'] == 'object added':
        belief_set['keys'][event['object']['id']] = event['object']
    elif event['event_type'] == 'object changed':
        belief_set['keys'][event['object']['id']].update(event['object'])
    elif event['event_type'] == 'object removed':
        del belief_set['keys'][event['object']['id']]
    return belief_set
