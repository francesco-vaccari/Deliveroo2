def function_1(event, belief_set):
    if event['object_type'] == 'map':
        if event['event_type'] == 'object added':
            belief_set['map'] = event['object']
        elif event['event_type'] == 'object changed':
            belief_set['map'].update(event['object'])
        elif event['event_type'] == 'object removed':
            if 'map' in belief_set:
                del belief_set['map']
    return belief_set


def function_2(event, belief_set):
    if event['object_type'] == 'parcel':
        if event['event_type'] == 'object added':
            belief_set.setdefault('parcels', {})[event['object']['id']
                ] = event['object']
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


def function_3(event, beliefs):
    if event['object_type'] == 'agent':
        if event['event_type'] == 'object added':
            beliefs['agent'] = event['object']
        elif event['event_type'] == 'object changed':
            beliefs['agent'].update(event['object'])
        elif event['event_type'] == 'object removed':
            del beliefs['agent']
    return beliefs


def function_4(event, belief_set):
    if event['object_type'] == 'key':
        if event['event_type'] == 'object added':
            belief_set['keys'] = {event['object']['id']: event['object']}
        elif event['event_type'] == 'object changed':
            belief_set['keys'][event['object']['id']] = event['object']
        elif event['event_type'] == 'object removed':
            belief_set['keys'].pop(event['object']['id'], None)
    return belief_set


def function_5(event, belief_set):
    if event['object_type'] == 'door':
        if event['event_type'] == 'object added':
            belief_set.setdefault('doors', {})[event['object']['id']] = {'id':
                event['object']['id'], 'coordinates': event['object'][
                'coordinates']}
        elif event['event_type'] == 'object changed':
            if 'doors' in belief_set and event['object']['id'] in belief_set[
                'doors']:
                belief_set['doors'][event['object']['id']]['coordinates'
                    ] = event['object']['coordinates']
        elif event['event_type'] == 'object removed':
            if 'doors' in belief_set and event['object']['id'] in belief_set[
                'doors']:
                del belief_set['doors'][event['object']['id']]
    return belief_set


