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


def function_3(event, belief_set):
    if event['object_type'] == 'key':
        if event['event_type'] == 'object added':
            if 'keys' not in belief_set:
                belief_set['keys'] = [event['object']]
            else:
                belief_set['keys'].append(event['object'])
        elif event['event_type'] == 'object changed':
            for i, key in enumerate(belief_set.get('keys', [])):
                if key['id'] == event['object']['id']:
                    belief_set['keys'][i] = event['object']
        elif event['event_type'] == 'object removed':
            belief_set['keys'] = [key for key in belief_set.get('keys', []) if
                key['id'] != event['object']['id']]
    return belief_set


def function_4(event, belief_set):
    if event['object_type'] != 'door':
        return belief_set
    if event['event_type'] == 'object added':
        if 'doors' not in belief_set:
            belief_set['doors'] = []
        belief_set['doors'].append(event['object'])
    elif event['event_type'] == 'object changed':
        for door in belief_set['doors']:
            if door['id'] == event['object']['id']:
                door.update(event['object'])
    elif event['event_type'] == 'object removed':
        belief_set['doors'] = [door for door in belief_set['doors'] if door
            ['id'] != event['object']['id']]
    return belief_set


def function_5(event, belief_set):
    if event['object_type'] == 'battery':
        if 'batteries' not in belief_set:
            belief_set['batteries'] = []
        if event['event_type'] == 'object added':
            belief_set['batteries'].append(event['object'])
        elif event['event_type'] == 'object changed':
            for battery in belief_set['batteries']:
                if battery['id'] == event['object']['id']:
                    battery['coordinates'] = event['object']['coordinates']
        elif event['event_type'] == 'object removed':
            belief_set['batteries'] = [battery for battery in belief_set[
                'batteries'] if battery['id'] != event['object']['id']]
    return belief_set


def function_6(event, belief_set):
    if event['object_type'] == 'parcel':
        if event['event_type'] == 'object added':
            if 'parcels' not in belief_set:
                belief_set['parcels'] = []
            belief_set['parcels'].append(event['object'])
        elif event['event_type'] == 'object changed':
            for parcel in belief_set['parcels']:
                if parcel['id'] == event['object']['id']:
                    parcel.update(event['object'])
        elif event['event_type'] == 'object removed':
            belief_set['parcels'] = [parcel for parcel in belief_set[
                'parcels'] if parcel['id'] != event['object']['id']]
    return belief_set


