def function_1(event, belief_set):
    if event['object_type'] == 'map':
        if event['event_type'] == 'object added':
            belief_set['map'] = event['object']
        elif event['event_type'] == 'object changed':
            belief_set['map'].update(event['object'])
        elif event['event_type'] == 'object removed':
            belief_set.pop('map', None)
    return belief_set


def function_2(event, beliefs):
    if event['object_type'] == 'agent':
        if event['event_type'] == 'object added':
            beliefs['agent'] = {event['object']['id']: event['object']}
        elif event['event_type'] == 'object changed':
            beliefs['agent'][event['object']['id']].update(event['object'])
        elif event['event_type'] == 'object removed':
            del beliefs['agent'][event['object']['id']]
    return beliefs


def function_3(event, belief_set):
    if event['object_type'] == 'parcel':
        if 'parcels' not in belief_set:
            belief_set['parcels'] = {}
        if event['event_type'] == 'object added':
            belief_set['parcels'][event['object']['id']] = event['object']
        elif event['event_type'] == 'object changed':
            belief_set['parcels'][event['object']['id']].update(event['object']
                )
        elif event['event_type'] == 'object removed':
            del belief_set['parcels'][event['object']['id']]
    return belief_set


