def function_5(event, belief_set):
    if event['object_type'] == 'battery':
        if 'batteries' not in belief_set:
            belief_set['batteries'] = []
        if event['event_type'] == 'object added':
            belief_set['batteries'].append(event['object'])
        elif event['event_type'] == 'object changed':
            for battery in belief_set['batteries']:
                if battery['id'] == event['object']['id']:
                    battery['coordinates'] = event['object']['coordinates']
        elif event['event_type'] == 'object removed':
            belief_set['batteries'] = [battery for battery in belief_set[
                'batteries'] if battery['id'] != event['object']['id']]
    return belief_set
