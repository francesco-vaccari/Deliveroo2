def function_1(event, belief_set):
    if 'object_type' in event and event['object_type'] == 'map':
        if event['event_type'] == 'object added' or event['event_type'
            ] == 'object changed':
            belief_set['map'] = event['object']
        elif event['event_type'] == 'object removed':
            if 'map' in belief_set:
                del belief_set['map']
    return belief_set


def function_2(event, belief_set):
    if event['object_type'] == 'agent':
        if event['event_type'] == 'object added':
            belief_set['agent'] = event['object']
        elif event['event_type'] == 'object changed':
            belief_set['agent'].update(event['object'])
        elif event['event_type'] == 'object removed':
            del belief_set['agent']
    return belief_set


def function_3(event, belief_set):
    if 'battery' not in belief_set:
        belief_set['battery'] = {}
    if event['object_type'] == 'battery':
        if event['event_type'] == 'object added':
            belief_set['battery'][event['object']['id']] = event['object'][
                'coordinates']
        elif event['event_type'] == 'object changed':
            if event['object']['id'] in belief_set['battery']:
                belief_set['battery'][event['object']['id']] = event['object'][
                    'coordinates']
        elif event['event_type'] == 'object removed':
            if event['object']['id'] in belief_set['battery']:
                del belief_set['battery'][event['object']['id']]
    return belief_set


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


