def function_1(event, belief_set):
    if event['event_type'] == 'object added' or event['event_type'
        ] == 'object changed':
        if 'map' in belief_set:
            belief_set['map'].update(event['object'])
        else:
            belief_set['map'] = event['object']
    elif event['event_type'] == 'object removed':
        if 'map' in belief_set:
            del belief_set['map']
    return belief_set


def function_2(event, belief_set):
    if event['object_type'] != 'agent':
        return belief_set
    if event['event_type'] == 'object added':
        belief_set['agent'] = {event['object']['id']: event['object']}
    elif event['event_type'] == 'object changed':
        belief_set['agent'][event['object']['id']] = event['object']
    elif event['event_type'] == 'object removed':
        del belief_set['agent'][event['object']['id']]
    return belief_set


def function_3(event, belief_set):
    if event['object_type'] == 'parcel':
        if event['event_type'] == 'object added':
            if 'parcels' not in belief_set:
                belief_set['parcels'] = {}
            belief_set['parcels'][event['object']['id']] = event['object']
        elif event['event_type'] == 'object changed':
            if 'parcels' in belief_set and event['object']['id'] in belief_set[
                'parcels']:
                belief_set['parcels'][event['object']['id']].update(event[
                    'object'])
        elif event['event_type'] == 'object removed':
            if 'parcels' in belief_set and event['object']['id'] in belief_set[
                'parcels']:
                del belief_set['parcels'][event['object']['id']]
    return belief_set


def function_4(event, belief_set):
    if event['object_type'] == 'battery':
        if event['event_type'] == 'object added':
            if 'batteries' not in belief_set:
                belief_set['batteries'] = {}
            belief_set['batteries'][event['object']['id']] = {'coordinates':
                event['object']['coordinates']}
        elif event['event_type'] == 'object changed':
            if 'batteries' in belief_set and event['object']['id'
                ] in belief_set['batteries']:
                belief_set['batteries'][event['object']['id']]['coordinates'
                    ] = event['object']['coordinates']
        elif event['event_type'] == 'object removed':
            if 'batteries' in belief_set and event['object']['id'
                ] in belief_set['batteries']:
                del belief_set['batteries'][event['object']['id']]
    return belief_set


def function_5(event, belief_set):
    if event['object_type'] == 'key':
        if event['event_type'] == 'object added':
            belief_set['keys'] = {event['object']['id']: event['object']}
        elif event['event_type'] == 'object changed':
            belief_set['keys'][event['object']['id']] = event['object']
        elif event['event_type'] == 'object removed':
            del belief_set['keys'][event['object']['id']]
    return belief_set


def function_7(event, belief_set):
    if event['object_type'] != 'key':
        return belief_set
    key_id = event['object']['id']
    if event['event_type'] == 'object added':
        belief_set['keys'][key_id] = event['object']
    elif event['event_type'] == 'object changed':
        belief_set['keys'][key_id].update(event['object'])
    elif event['event_type'] == 'object removed':
        if key_id in belief_set['keys']:
            del belief_set['keys'][key_id]
    return belief_set


def function_6(event, belief_set):
    if event['object_type'] == 'door':
        if event['event_type'] == 'object added':
            if 'doors' not in belief_set:
                belief_set['doors'] = {}
            belief_set['doors'][event['object']['id']] = event['object']
        elif event['event_type'] == 'object changed':
            if 'doors' in belief_set and event['object']['id'] in belief_set[
                'doors']:
                belief_set['doors'][event['object']['id']].update(event[
                    'object'])
        elif event['event_type'] == 'object removed':
            if 'doors' in belief_set and event['object']['id'] in belief_set[
                'doors']:
                del belief_set['doors'][event['object']['id']]
    return belief_set


