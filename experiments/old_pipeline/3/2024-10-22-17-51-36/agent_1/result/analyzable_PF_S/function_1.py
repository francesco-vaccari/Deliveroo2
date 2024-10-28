def function_1(event, belief_set):
    if 'map' in belief_set:
        if event['event_type'] == 'object added':
            belief_set['map'] = event['object']
        elif event['event_type'] == 'object changed':
            belief_set['map'].update(event['object'])
        elif event['event_type'] == 'object removed':
            del belief_set['map']
    elif event['event_type'] == 'object added':
        belief_set['map'] = event['object']
    return belief_set
