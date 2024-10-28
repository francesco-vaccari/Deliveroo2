def function_1(event, belief_set):
    if event['event_type'] == 'object added':
        belief_set[event['object_type']] = event['object']
    elif event['event_type'] == 'object changed':
        belief_set[event['object_type']].update(event['object'])
    elif event['event_type'] == 'object removed':
        del belief_set[event['object_type']]
    return belief_set


def function_2(event, belief_set):
    if 'parcel' not in belief_set:
        belief_set['parcel'] = {}
    if event['event_type'] == 'object added':
        belief_set['parcel'][event['object']['id']] = event['object']
    elif event['event_type'] == 'object changed':
        belief_set['parcel'][event['object']['id']].update(event['object'])
    elif event['event_type'] == 'object removed':
        del belief_set['parcel'][event['object']['id']]
    return belief_set


def function_3(event, belief_set):
    if event['object_type'] == 'agent':
        if event['event_type'] == 'object added':
            belief_set['agent'] = event['object']
        elif event['event_type'] == 'object changed':
            belief_set['agent'].update(event['object'])
        elif event['event_type'] == 'object removed':
            belief_set.pop('agent', None)
    return belief_set


