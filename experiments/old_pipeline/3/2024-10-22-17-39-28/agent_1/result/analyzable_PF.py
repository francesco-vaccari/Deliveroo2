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
            belief_set['agent'] = {event['object']['id']: event['object']}
        elif event['event_type'] == 'object changed':
            belief_set['agent'][event['object']['id']] = event['object']
        elif event['event_type'] == 'object removed':
            del belief_set['agent'][event['object']['id']]
    return belief_set


def function_4(event, belief_set):
    object_type = event['object_type']
    event_type = event['event_type']
    object = event['object']
    if object_type == 'key':
        if object_type not in belief_set:
            belief_set[object_type] = {}
        if event_type == 'object added':
            belief_set[object_type][object['id']] = object
        elif event_type == 'object changed':
            belief_set[object_type][object['id']].update(object)
        elif event_type == 'object removed':
            del belief_set[object_type][object['id']]
    return belief_set


def function_5(event, belief_set):
    if event['object_type'] != 'door':
        return belief_set
    if event['event_type'] == 'object added':
        belief_set['doors'] = belief_set.get('doors', {})
        belief_set['doors'][event['object']['id']] = event['object']
    elif event['event_type'] == 'object changed':
        if 'doors' not in belief_set or event['object']['id'
            ] not in belief_set['doors']:
            raise ValueError('Door does not exist')
        belief_set['doors'][event['object']['id']] = event['object']
    elif event['event_type'] == 'object removed':
        if 'doors' not in belief_set or event['object']['id'
            ] not in belief_set['doors']:
            raise ValueError('Door does not exist')
        del belief_set['doors'][event['object']['id']]
    return belief_set


