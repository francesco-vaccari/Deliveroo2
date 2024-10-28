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
    object_type = event['object_type']
    event_type = event['event_type']
    object = event['object']
    if object_type == 'parcel':
        if event_type == 'object added':
            belief_set.setdefault(object_type, {})[object['id']] = object
        elif event_type == 'object changed':
            if object['id'] in belief_set.get(object_type, {}):
                belief_set[object_type][object['id']].update(object)
        elif event_type == 'object removed':
            if object['id'] in belief_set.get(object_type, {}):
                del belief_set[object_type][object['id']]
    return belief_set


def function_3(event, belief_set):
    if event['object_type'] == 'agent':
        if event['event_type'] == 'object added':
            belief_set['agent'] = event['object']
        elif event['event_type'] == 'object changed':
            belief_set['agent'].update(event['object'])
        elif event['event_type'] == 'object removed':
            del belief_set['agent']
    return belief_set


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


def function_5(event, belief_set):
    if event['object_type'] == 'door':
        if event['event_type'] == 'object added':
            belief_set['door'] = {event['object']['id']: event['object']}
        elif event['event_type'] == 'object changed':
            if 'door' in belief_set and event['object']['id'] in belief_set[
                'door']:
                belief_set['door'][event['object']['id']] = event['object']
        elif event['event_type'] == 'object removed':
            if 'door' in belief_set and event['object']['id'] in belief_set[
                'door']:
                del belief_set['door'][event['object']['id']]
    return belief_set


