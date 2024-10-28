def function_1(event, belief_set):
    if event['event_type'] == 'object added':
        if 'map' not in belief_set:
            belief_set['map'] = {}
        belief_set['map'][event['object_type']] = event['object']
    elif event['event_type'] == 'object changed':
        if 'map' in belief_set and event['object_type'] in belief_set['map']:
            belief_set['map'][event['object_type']].update(event['object'])
    elif event['event_type'] == 'object removed':
        if 'map' in belief_set and event['object_type'] in belief_set['map']:
            del belief_set['map'][event['object_type']]
    return belief_set


def function_2(event, belief_set):
    if 'parcel' not in belief_set:
        belief_set['parcel'] = {}
    if event['event_type'] == 'object added' or event['event_type'
        ] == 'object changed':
        belief_set['parcel'][event['object']['id']] = event['object']
    elif event['event_type'] == 'object removed':
        if event['object']['id'] in belief_set['parcel']:
            del belief_set['parcel'][event['object']['id']]
    return belief_set


def function_3(event, belief_set):
    if event['object_type'] == 'agent':
        if event['event_type'] == 'object added':
            belief_set['agent'] = {event['object']['id']: event['object']}
        elif event['event_type'] == 'object changed':
            belief_set['agent'][event['object']['id']] = event['object']
        elif event['event_type'] == 'object removed':
            del belief_set['agent'][event['object']['id']]
    return belief_set


