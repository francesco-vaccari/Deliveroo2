def function_3(event, belief_set):
    if 'batteries' not in belief_set:
        belief_set['batteries'] = {}
    if event['event_type'] == 'object added':
        belief_set['batteries'][event['object']['id']] = event['object']
    elif event['event_type'] == 'object changed':
        belief_set['batteries'][event['object']['id']].update(event['object'])
    elif event['event_type'] == 'object removed':
        del belief_set['batteries'][event['object']['id']]
    return belief_set
