def function_1(event, belief_set):
    if 'object_type' in event and event['object_type'] == 'map':
        if event['event_type'] == 'object added' or event['event_type'
            ] == 'object changed':
            belief_set['map'] = event['object']
        elif event['event_type'] == 'object removed':
            if 'map' in belief_set:
                del belief_set['map']
    return belief_set
