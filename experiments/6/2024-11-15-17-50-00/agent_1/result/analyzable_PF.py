def function_1(event, current_beliefs):
    if event['object_type'] == 'map':
        if event['event_type'] == 'object added':
            current_beliefs['map'] = event['object']
        elif event['event_type'] == 'object changed':
            current_beliefs['map'].update(event['object'])
        elif event['event_type'] == 'object removed':
            current_beliefs.pop('map', None)
    return current_beliefs


def function_2(event, belief_set):
    if event['object_type'] == 'agent':
        if event['event_type'] == 'object added':
            belief_set['agent'] = {event['object']['id']: event['object']}
        elif event['event_type'] == 'object changed':
            if 'agent' in belief_set and event['object']['id'] in belief_set[
                'agent']:
                belief_set['agent'][event['object']['id']].update(event[
                    'object'])
        elif event['event_type'] == 'object removed':
            if 'agent' in belief_set and event['object']['id'] in belief_set[
                'agent']:
                del belief_set['agent'][event['object']['id']]
    return belief_set


def function_3(event, beliefs):
    if event['object_type'] == 'battery':
        if event['event_type'] == 'object added':
            if 'batteries' not in beliefs:
                beliefs['batteries'] = {}
            beliefs['batteries'][event['object']['id']] = event['object']
        elif event['event_type'] == 'object changed':
            if 'batteries' in beliefs and event['object']['id'] in beliefs[
                'batteries']:
                beliefs['batteries'][event['object']['id']] = event['object']
        elif event['event_type'] == 'object removed':
            if 'batteries' in beliefs and event['object']['id'] in beliefs[
                'batteries']:
                del beliefs['batteries'][event['object']['id']]
    return beliefs


def function_4(event, belief_set):
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


