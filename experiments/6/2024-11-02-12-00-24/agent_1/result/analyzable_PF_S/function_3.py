def function_3(event, belief_set):
    if 'battery' not in belief_set:
        belief_set['battery'] = {}
    if event['object_type'] == 'battery':
        if event['event_type'] == 'object added':
            belief_set['battery'][event['object']['id']] = event['object'][
                'coordinates']
        elif event['event_type'] == 'object changed':
            if event['object']['id'] in belief_set['battery']:
                belief_set['battery'][event['object']['id']] = event['object'][
                    'coordinates']
        elif event['event_type'] == 'object removed':
            if event['object']['id'] in belief_set['battery']:
                del belief_set['battery'][event['object']['id']]
    return belief_set
