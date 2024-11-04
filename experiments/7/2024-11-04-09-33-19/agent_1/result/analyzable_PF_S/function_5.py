def function_5(event, belief_set):
    if event['object_type'] != 'battery':
        return belief_set
    if event['event_type'] == 'object added':
        if 'batteries' not in belief_set:
            belief_set['batteries'] = []
        belief_set['batteries'].append(event['object'])
    elif event['event_type'] == 'object changed':
        for i, battery in enumerate(belief_set.get('batteries', [])):
            if battery['id'] == event['object']['id']:
                belief_set['batteries'][i] = event['object']
                break
    elif event['event_type'] == 'object removed':
        belief_set['batteries'] = [battery for battery in belief_set.get(
            'batteries', []) if battery['id'] != event['object']['id']]
    return belief_set
