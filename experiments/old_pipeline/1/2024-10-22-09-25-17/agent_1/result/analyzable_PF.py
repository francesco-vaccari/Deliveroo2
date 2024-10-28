def function_1(event, belief_set):
    if event['object_type'] == 'map':
        if event['event_type'] == 'object added':
            belief_set['map'] = event['object']
        elif event['event_type'] == 'object changed':
            belief_set['map'].update(event['object'])
        elif event['event_type'] == 'object removed':
            del belief_set['map']
    return belief_set


def function_2(event, belief_set):
    if event['object_type'] != 'parcel':
        return belief_set
    if event['event_type'] == 'object added':
        if 'parcel' not in belief_set:
            belief_set['parcel'] = {}
        belief_set['parcel'][event['object']['id']] = event['object']
    elif event['event_type'] == 'object changed':
        if 'parcel' in belief_set and event['object']['id'] in belief_set[
            'parcel']:
            belief_set['parcel'][event['object']['id']].update(event['object'])
    elif event['event_type'] == 'object removed':
        if 'parcel' in belief_set and event['object']['id'] in belief_set[
            'parcel']:
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


