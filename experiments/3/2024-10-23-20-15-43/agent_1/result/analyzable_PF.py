def function_1(event, belief_set):
    if event['object_type'] == 'map':
        if event['event_type'] == 'object added' or event['event_type'
            ] == 'object changed':
            belief_set['map'] = event['object']
        elif event['event_type'] == 'object removed':
            if 'map' in belief_set:
                del belief_set['map']
    return belief_set


def function_2(event, beliefs):
    if event['object_type'] == 'parcel':
        if event['event_type'] == 'object added':
            if 'parcels' not in beliefs:
                beliefs['parcels'] = {}
            beliefs['parcels'][event['object']['id']] = event['object']
        elif event['event_type'] == 'object changed':
            if 'parcels' in beliefs and event['object']['id'] in beliefs[
                'parcels']:
                beliefs['parcels'][event['object']['id']].update(event[
                    'object'])
        elif event['event_type'] == 'object removed':
            if 'parcels' in beliefs and event['object']['id'] in beliefs[
                'parcels']:
                del beliefs['parcels'][event['object']['id']]
    return beliefs


def function_3(event, beliefs):
    if event['object_type'] == 'agent':
        if event['event_type'] == 'object added':
            beliefs['agent'] = event['object']
        elif event['event_type'] == 'object changed':
            beliefs['agent'].update(event['object'])
        elif event['event_type'] == 'object removed':
            del beliefs['agent']
    return beliefs


def function_4(event, beliefs):
    if event['object_type'] == 'key':
        if event['event_type'] == 'object added':
            beliefs['keys'] = {event['object']['id']: event['object']}
        elif event['event_type'] == 'object changed':
            beliefs['keys'][event['object']['id']] = event['object']
        elif event['event_type'] == 'object removed':
            del beliefs['keys'][event['object']['id']]
    return beliefs


def function_5(event, belief_set):
    if event['object_type'] != 'door':
        return belief_set
    if event['event_type'] == 'object added':
        if 'doors' not in belief_set:
            belief_set['doors'] = {}
        belief_set['doors'][event['object']['id']] = event['object']
    elif event['event_type'] == 'object changed':
        if 'doors' in belief_set and event['object']['id'] in belief_set[
            'doors']:
            belief_set['doors'][event['object']['id']].update(event['object'])
    elif event['event_type'] == 'object removed':
        if 'doors' in belief_set and event['object']['id'] in belief_set[
            'doors']:
            del belief_set['doors'][event['object']['id']]
    return belief_set

