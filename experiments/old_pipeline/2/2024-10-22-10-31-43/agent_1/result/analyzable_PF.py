def function_1(event, belief_set):
    if event['event_type'] == 'object added':
        if 'map' not in belief_set:
            belief_set['map'] = {}
        belief_set['map'] = event['object']
    elif event['event_type'] == 'object changed':
        if 'map' in belief_set:
            belief_set['map'].update(event['object'])
    elif event['event_type'] == 'object removed':
        if 'map' in belief_set:
            del belief_set['map']
    return belief_set


def function_2(event, belief_set):
    object_type = event['object_type']
    if object_type == 'parcel':
        if event['event_type'] == 'object added':
            if object_type not in belief_set:
                belief_set[object_type] = {}
            belief_set[object_type][event['object']['id']] = event['object']
        elif event['event_type'] == 'object changed':
            if event['object']['id'] in belief_set[object_type]:
                belief_set[object_type][event['object']['id']].update(event
                    ['object'])
        elif event['event_type'] == 'object removed':
            if event['object']['id'] in belief_set[object_type]:
                del belief_set[object_type][event['object']['id']]
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


def function_4(event, belief_set):
    if event['object_type'] == 'key':
        if event['event_type'] == 'object added':
            belief_set['key'] = {event['object']['id']: event['object']}
        elif event['event_type'] == 'object changed':
            belief_set['key'][event['object']['id']] = event['object']
        elif event['event_type'] == 'object removed':
            del belief_set['key'][event['object']['id']]
    return belief_set


def function_5(event, belief_set):
    if event['object_type'] == 'door':
        if event['event_type'] == 'object added':
            belief_set['door'] = {event['object']['id']: event['object']}
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


