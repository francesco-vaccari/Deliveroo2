def function_3(event, belief_set):
    if event['object_type'] != 'agent':
        return belief_set
    if event['event_type'] == 'object added' or event['event_type'
        ] == 'object changed':
        belief_set['agent'] = event['object']
    elif event['event_type'] == 'object removed':
        if 'agent' in belief_set:
            del belief_set['agent']
    return belief_set
