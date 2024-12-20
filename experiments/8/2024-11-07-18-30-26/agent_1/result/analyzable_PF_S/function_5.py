def function_5(event, belief_set):
    if event['object_type'] != 'key':
        return belief_set
    if event['event_type'] == 'object added' or event['event_type'
        ] == 'object changed':
        if 'keys' not in belief_set:
            belief_set['keys'] = {}
        belief_set['keys'][event['object']['id']] = event['object']
    elif event['event_type'] == 'object removed':
        if 'keys' in belief_set and event['object']['id'] in belief_set['keys'
            ]:
            del belief_set['keys'][event['object']['id']]
    return belief_set
