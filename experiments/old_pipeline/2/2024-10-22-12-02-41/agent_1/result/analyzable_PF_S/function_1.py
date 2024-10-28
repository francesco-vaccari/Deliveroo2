def function_1(event, belief_set):
    if event['object_type'] != 'map':
        return belief_set
    if event['event_type'] == 'object added':
        if 'map' not in belief_set:
            belief_set['map'] = {}
        belief_set['map'].update(event['object'])
    elif event['event_type'] == 'object changed':
        if 'map' in belief_set:
            belief_set['map'].update(event['object'])
    elif event['event_type'] == 'object removed':
        if 'map' in belief_set:
            del belief_set['map']
    return belief_set
