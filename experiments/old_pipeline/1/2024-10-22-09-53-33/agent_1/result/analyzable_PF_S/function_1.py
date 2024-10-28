def function_1(event, belief_set):
    if event['event_type'] == 'object added':
        if 'map' not in belief_set:
            belief_set['map'] = {}
        belief_set['map'][event['object_type']] = event['object']
    elif event['event_type'] == 'object changed':
        if 'map' in belief_set and event['object_type'] in belief_set['map']:
            belief_set['map'][event['object_type']].update(event['object'])
    elif event['event_type'] == 'object removed':
        if 'map' in belief_set and event['object_type'] in belief_set['map']:
            del belief_set['map'][event['object_type']]
    return belief_set
