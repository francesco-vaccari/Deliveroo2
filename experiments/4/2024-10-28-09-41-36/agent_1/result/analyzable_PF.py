def function_1(event, belief_set):
    if event['object_type'] == 'map':
        if event['event_type'] == 'object added' or event['event_type'
            ] == 'object changed':
            belief_set['map'] = event['object']
        elif event['event_type'] == 'object removed':
            del belief_set['map']
    return belief_set


def function_2(event, belief):
    if event['object_type'] == 'parcel':
        if event['event_type'] == 'object added':
            if 'parcels' not in belief:
                belief['parcels'] = {}
            belief['parcels'][event['object']['id']] = event['object']
        elif event['event_type'] == 'object changed':
            if 'parcels' in belief and event['object']['id'] in belief[
                'parcels']:
                belief['parcels'][event['object']['id']].update(event['object']
                    )
        elif event['event_type'] == 'object removed':
            if 'parcels' in belief and event['object']['id'] in belief[
                'parcels']:
                del belief['parcels'][event['object']['id']]
    return belief


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
    if event['object_type'] != 'key':
        return belief_set
    if 'keys' not in belief_set:
        belief_set['keys'] = {}
    if event['event_type'] == 'object added':
        belief_set['keys'][event['object']['id']] = event['object']
    elif event['event_type'] == 'object changed':
        belief_set['keys'][event['object']['id']].update(event['object'])
    elif event['event_type'] == 'object removed':
        del belief_set['keys'][event['object']['id']]
    return belief_set


def function_5(event, belief_set):
    if event['object_type'] == 'door':
        if event['event_type'] == 'object added':
            belief_set['doors'] = belief_set.get('doors', {})
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


