def function_1(event, belief_set):
    if 'map' not in belief_set:
        belief_set['map'] = {}
    if event['event_type'] == 'object added':
        belief_set['map'] = event['object']
    elif event['event_type'] == 'object changed':
        for cell in event['object']['grid']:
            for existing_cell in belief_set['map']['grid']:
                if existing_cell['cell_coordinates'] == cell['cell_coordinates'
                    ]:
                    existing_cell['cell_type'] = cell['cell_type']
    elif event['event_type'] == 'object removed':
        belief_set.pop('map', None)
    return belief_set


def function_2(event, belief_set):
    if event['object_type'] != 'parcel':
        return belief_set
    if 'parcel' not in belief_set:
        belief_set['parcel'] = {}
    if event['event_type'] == 'object added':
        belief_set['parcel'][event['object']['id']] = event['object']
    elif event['event_type'] == 'object changed':
        if event['object']['id'] in belief_set['parcel']:
            belief_set['parcel'][event['object']['id']].update(event['object'])
    elif event['event_type'] == 'object removed':
        if event['object']['id'] in belief_set['parcel']:
            del belief_set['parcel'][event['object']['id']]
    return belief_set


def function_3(event, belief_set):
    if event['object_type'] == 'agent':
        if event['event_type'] == 'object added':
            belief_set['agent'] = event['object']
        elif event['event_type'] == 'object changed':
            for key, value in event['object'].items():
                belief_set['agent'][key] = value
        elif event['event_type'] == 'object removed':
            del belief_set['agent']
    return belief_set


def function_4(event, belief_set):
    object_id = event['object']['id']
    if event['event_type'] == 'object added':
        if 'key' not in belief_set:
            belief_set['key'] = {}
        belief_set['key'][object_id] = event['object']
    elif event['event_type'] == 'object changed':
        if 'key' in belief_set and object_id in belief_set['key']:
            belief_set['key'][object_id] = event['object']
    elif event['event_type'] == 'object removed':
        if 'key' in belief_set and object_id in belief_set['key']:
            del belief_set['key'][object_id]
    return belief_set


def function_5(event, belief_set):
    if 'door' not in belief_set:
        belief_set['door'] = {}
    if event['event_type'] == 'object added':
        belief_set['door'][event['object']['id']] = event['object']
    elif event['event_type'] == 'object changed':
        belief_set['door'][event['object']['id']].update(event['object'])
    elif event['event_type'] == 'object removed':
        belief_set['door'].pop(event['object']['id'], None)
    return belief_set


