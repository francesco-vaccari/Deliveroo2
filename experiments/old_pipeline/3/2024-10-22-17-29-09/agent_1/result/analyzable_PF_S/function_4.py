def function_4(event, belief_set):
    if event['object_type'] == 'key':
        if event['event_type'] == 'object added':
            belief_set['key'] = {event['object']['id']: event['object']}
        elif event['event_type'] == 'object changed':
            if 'key' in belief_set and event['object']['id'] in belief_set[
                'key']:
                belief_set['key'][event['object']['id']].update(event['object']
                    )
        elif event['event_type'] == 'object removed':
            if 'key' in belief_set and event['object']['id'] in belief_set[
                'key']:
                del belief_set['key'][event['object']['id']]
    return belief_set
