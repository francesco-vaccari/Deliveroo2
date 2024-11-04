def function_3(event, belief_set):
    if event['object_type'] == 'key':
        if event['event_type'] == 'object added':
            if 'keys' not in belief_set:
                belief_set['keys'] = [event['object']]
            else:
                belief_set['keys'].append(event['object'])
        elif event['event_type'] == 'object changed':
            for i, key in enumerate(belief_set.get('keys', [])):
                if key['id'] == event['object']['id']:
                    belief_set['keys'][i] = event['object']
        elif event['event_type'] == 'object removed':
            belief_set['keys'] = [key for key in belief_set.get('keys', []) if
                key['id'] != event['object']['id']]
    return belief_set
