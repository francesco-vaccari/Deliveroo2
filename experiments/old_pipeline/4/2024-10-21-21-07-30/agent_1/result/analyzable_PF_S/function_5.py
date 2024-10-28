def function_5(event, belief_set):
    if 'door' not in belief_set:
        belief_set['door'] = {}
    if event['event_type'] == 'object added':
        belief_set['door'][event['object']['id']] = event['object']
    elif event['event_type'] == 'object changed':
        belief_set['door'][event['object']['id']].update(event['object'])
    elif event['event_type'] == 'object removed':
        belief_set['door'].pop(event['object']['id'], None)
    return belief_set
