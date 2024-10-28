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
        if event['event_type'] == 'object added' or event['event_type'
            ] == 'object changed':
            belief_set['agent'] = event['object']
        elif event['event_type'] == 'object removed':
            if 'agent' in belief_set:
                del belief_set['agent']
    return belief_set


def function_4(event, belief_set):
    if event['object_type'] == 'key':
        if event['event_type'] == 'object added':
            belief_set['key'] = {event['object']['id']: event['object']}
        elif event['event_type'] == 'object changed':
            belief_set['key'][event['object']['id']].update(event['object'])
        elif event['event_type'] == 'object removed':
            del belief_set['key'][event['object']['id']]
    return belief_set


def function_5(event, belief_set):
    if event['object_type'] == 'door':
        if event['event_type'] == 'object added':
            belief_set['door'] = belief_set.get('door', {})
            belief_set['door'][event['object']['id']] = event['object']
        elif event['event_type'] == 'object changed':
            if 'door' in belief_set and event['object']['id'] in belief_set[
                'door']:
                belief_set['door'][event['object']['id']].update(event[
                    'object'])
        elif event['event_type'] == 'object removed':
            if 'door' in belief_set and event['object']['id'] in belief_set[
                'door']:
                del belief_set['door'][event['object']['id']]
    return belief_set


