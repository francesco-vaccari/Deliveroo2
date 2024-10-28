def function_1(event, belief_set):
    if 'map' not in belief_set:
        belief_set['map'] = {}
    if event['event_type'] == 'object added' or event['event_type'
        ] == 'object changed':
        belief_set['map'] = event['object']
    elif event['event_type'] == 'object removed':
        belief_set['map'] = {}
    return belief_set
