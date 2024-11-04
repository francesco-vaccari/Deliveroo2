def function_3(event, belief_set):
    if event['object_type'] == 'key':
        if event['event_type'] == 'object added':
            if 'keys' not in belief_set:
                belief_set['keys'] = {}
            belief_set['keys'][event['object']['id']] = event['object']
        elif event['event_type'] == 'object changed':
            if event['object']['id'] in belief_set['keys']:
                belief_set['keys'][event['object']['id']].update(event[
                    'object'])
        elif event['event_type'] == 'object removed':
            if event['object']['id'] in belief_set['keys']:
                del belief_set['keys'][event['object']['id']]
    return belief_set
