def function_1(event, belief_set):
    if event['object_type'] != 'map':
        return belief_set
    if event['event_type'] == 'object added':
        if 'map' not in belief_set:
            belief_set['map'] = {}
        belief_set['map'].update(event['object'])
    elif event['event_type'] == 'object changed':
        if 'map' in belief_set:
            belief_set['map'].update(event['object'])
    elif event['event_type'] == 'object removed':
        if 'map' in belief_set:
            del belief_set['map']
    return belief_set


def function_2(event, belief_set):
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


def function_3(event, belief_set):
    if event['object_type'] == 'agent':
        if event['event_type'] == 'object added':
            belief_set['agent'] = event['object']
        elif event['event_type'] == 'object changed':
            belief_set['agent'].update(event['object'])
        elif event['event_type'] == 'object removed':
            del belief_set['agent']
    return belief_set


def function_4(event, current_beliefs):
    if event['object_type'] != 'key':
        return current_beliefs
    if 'keys' not in current_beliefs:
        current_beliefs['keys'] = {}
    if event['event_type'] == 'object added':
        current_beliefs['keys'][event['object']['id']] = event['object']
    elif event['event_type'] == 'object changed':
        current_beliefs['keys'][event['object']['id']].update(event['object'])
    elif event['event_type'] == 'object removed':
        del current_beliefs['keys'][event['object']['id']]
    return current_beliefs


def function_5(event, belief_set):
    if event['object_type'] == 'door':
        if event['event_type'] == 'object added':
            belief_set['doors'] = {event['object']['id']: event['object']}
        elif event['event_type'] == 'object changed':
            belief_set['doors'][event['object']['id']] = event['object']
        elif event['event_type'] == 'object removed':
            del belief_set['doors'][event['object']['id']]
    return belief_set


