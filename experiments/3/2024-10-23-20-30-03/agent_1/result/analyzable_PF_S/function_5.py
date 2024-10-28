def function_5(event, belief_set):
    if event['object_type'] != 'door':
        return belief_set
    if event['event_type'] == 'object added':
        if 'doors' not in belief_set:
            belief_set['doors'] = {}
        belief_set['doors'][event['object']['id']] = event['object']
    elif event['event_type'] == 'object changed':
        if 'doors' in belief_set and event['object']['id'] in belief_set[
            'doors']:
            belief_set['doors'][event['object']['id']] = event['object']
    elif event['event_type'] == 'object removed':
        if 'doors' in belief_set and event['object']['id'] in belief_set[
            'doors']:
            del belief_set['doors'][event['object']['id']]
    return belief_set
