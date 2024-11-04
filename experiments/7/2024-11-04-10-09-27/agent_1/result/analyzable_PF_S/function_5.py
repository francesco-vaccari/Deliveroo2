def function_5(event, belief_set):
    if event['object_type'] == 'battery':
        if event['event_type'] == 'object added':
            if 'batteries' not in belief_set:
                belief_set['batteries'] = {}
            belief_set['batteries'][event['object']['id']] = event['object']
        elif event['event_type'] == 'object changed':
            if 'batteries' in belief_set and event['object']['id'
                ] in belief_set['batteries']:
                belief_set['batteries'][event['object']['id']].update(event
                    ['object'])
        elif event['event_type'] == 'object removed':
            if 'batteries' in belief_set and event['object']['id'
                ] in belief_set['batteries']:
                del belief_set['batteries'][event['object']['id']]
    return belief_set
