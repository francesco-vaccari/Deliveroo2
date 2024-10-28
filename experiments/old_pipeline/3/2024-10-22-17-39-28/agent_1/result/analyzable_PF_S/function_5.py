def function_5(event, belief_set):
    if event['object_type'] != 'door':
        return belief_set
    if event['event_type'] == 'object added':
        belief_set['doors'] = belief_set.get('doors', {})
        belief_set['doors'][event['object']['id']] = event['object']
    elif event['event_type'] == 'object changed':
        if 'doors' not in belief_set or event['object']['id'
            ] not in belief_set['doors']:
            raise ValueError('Door does not exist')
        belief_set['doors'][event['object']['id']] = event['object']
    elif event['event_type'] == 'object removed':
        if 'doors' not in belief_set or event['object']['id'
            ] not in belief_set['doors']:
            raise ValueError('Door does not exist')
        del belief_set['doors'][event['object']['id']]
    return belief_set
