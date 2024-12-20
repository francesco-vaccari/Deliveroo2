def function_1(event, belief_set):
    if event['object_type'] == 'map':
        if event['event_type'] == 'object added':
            belief_set['map'] = event['object']
        elif event['event_type'] == 'object changed':
            for cell in event['object']['grid']:
                for belief_cell in belief_set['map']['grid']:
                    if belief_cell['cell_coordinates'] == cell[
                        'cell_coordinates']:
                        belief_cell['cell_type'] = cell['cell_type']
        elif event['event_type'] == 'object removed':
            del belief_set['map']
    return belief_set


def function_2(event, belief_set):
    if event['object_type'] == 'agent':
        if event['event_type'] == 'object added':
            belief_set['agent'] = {event['object']['id']: event['object']}
        elif event['event_type'] == 'object changed':
            belief_set['agent'][event['object']['id']].update(event['object'])
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
            if 'batteries' in belief_set:
                if event['object']['id'] in belief_set['batteries']:
                    belief_set['batteries'][event['object']['id']][
                        'coordinates'] = event['object']['coordinates']
        elif event['event_type'] == 'object removed':
            if 'batteries' in belief_set:
                if event['object']['id'] in belief_set['batteries']:
                    del belief_set['batteries'][event['object']['id']]
    return belief_set


def function_5(event, belief_set):
    if event['object_type'] != 'key':
        return belief_set
    if event['event_type'] == 'object added' or event['event_type'
        ] == 'object changed':
        if 'keys' not in belief_set:
            belief_set['keys'] = {}
        belief_set['keys'][event['object']['id']] = event['object']
    elif event['event_type'] == 'object removed':
        if 'keys' in belief_set and event['object']['id'] in belief_set['keys'
            ]:
            del belief_set['keys'][event['object']['id']]
    return belief_set


def function_6(event, beliefs):
    door_id = event['object']['id']
    if event['event_type'] == 'object added':
        if 'doors' not in beliefs:
            beliefs['doors'] = {}
        beliefs['doors'][door_id] = event['object']
    elif event['event_type'] == 'object changed':
        if 'doors' in beliefs and door_id in beliefs['doors']:
            beliefs['doors'][door_id].update(event['object'])
    elif event['event_type'] == 'object removed':
        if 'doors' in beliefs and door_id in beliefs['doors']:
            del beliefs['doors'][door_id]
    return beliefs


