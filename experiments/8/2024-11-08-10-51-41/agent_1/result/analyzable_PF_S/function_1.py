def function_1(event, belief_set):
    if event['event_type'] == 'object added' or event['event_type'
        ] == 'object changed':
        if 'map' in belief_set:
            belief_set['map'].update(event['object'])
        else:
            belief_set['map'] = event['object']
    elif event['event_type'] == 'object removed':
        if 'map' in belief_set:
            del belief_set['map']
    return belief_set
